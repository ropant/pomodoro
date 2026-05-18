import tkinter as tk
import math

# ── Palette Hokusai authentique ────────────────────────────
FOND_NUIT    = "#0D1F3C"
BLEU_PRUSSE  = "#1A3A6B"
BLEU_VAGUE   = "#2B5BA0"
BLEU_CLAIR   = "#4A8AC0"
BLANC_CREME  = "#F5F0E8"
BLANC_PUR    = "#FFFFFF"
ROUGE_JAPON  = "#C0392B"
ROUGE_FONCE  = "#A93226"
FUJI_GRIS    = "#8AAEC8"
FUJI_NEIGE   = "#E8EDF5"

# ── Constantes ─────────────────────────────────────────────
LARGEUR       = 400
HAUTEUR       = 520
DUREE_TRAVAIL = 1500
DUREE_PAUSE   = 420

# ── Variables globales ─────────────────────────────────────
cycle  = 0
offset = 0

# ── Logique Pomodoro ───────────────────────────────────────
def demarrer():
    global cycle
    cycle += 1
    canvas.itemconfig(textCycle,   text=f"間  cycle {cycle}")
    canvas.itemconfig(textSession, text="— travail —")
    boutonDemarrer.config(state="disabled")
    boutonPause.place_forget()
    miseAJour(DUREE_TRAVAIL)

def miseAJour(temps):
    minutes  = temps // 60
    secondes = temps % 60
    temps   -= 1
    canvas.itemconfig(textTimer, text=f"{minutes:02d}:{secondes:02d}")
    if temps < 0:
        sessionTerminee()
    else:
        racine.after(1000, lambda: miseAJour(temps))

def sessionTerminee():
    canvas.itemconfig(textTimer, text="00:00")
    boutonDemarrer.config(state="normal")
    boutonPause.place(x=LARGEUR // 2 - 90, y=428)

def lancerPause():
    boutonPause.place_forget()
    boutonDemarrer.config(state="disabled")
    canvas.itemconfig(textSession, text="— pause —")
    miseAJour(DUREE_PAUSE)

# ── Animation vagues ───────────────────────────────────────
def animer():
    global offset
    offset += 1.5
    canvas.delete("vague")

    dessinerVague(offset * 0.55, BLEU_PRUSSE, 20, 358, "vague")
    dessinerVague(offset * 0.85, BLEU_VAGUE,  25, 372, "vague")
    dessinerVague(offset * 1.20, BLEU_CLAIR,  15, 388, "vague")

    canvas.tag_raise("ui")
    racine.after(40, animer)

def dessinerVague(decalage, couleur, amplitude, yBase, tag):
    points = []
    for x in range(0, LARGEUR + 10, 5):
        y = yBase + amplitude * math.sin((x + decalage) * 0.026)
        points.extend([x, y])
    points.extend([LARGEUR, HAUTEUR, 0, HAUTEUR])
    canvas.create_polygon(
        points, fill=couleur, outline="", smooth=True, tags=tag
    )

# ── Fond statique ──────────────────────────────────────────
def dessinerFond():
    # Ciel dégradé : bleu nuit → bleu profond
    nbBandes = 28
    for i in range(nbBandes):
        t = i / nbBandes
        r = int(13  + t * 15)
        g = int(31  + t * 45)
        b = int(60  + t * 95)
        canvas.create_rectangle(
            0, i * (360 // nbBandes),
            LARGEUR, (i + 1) * (360 // nbBandes),
            fill=f"#{r:02x}{g:02x}{b:02x}", outline=""
        )

    # Mont Fuji
    canvas.create_polygon(
        [200, 75, 318, 315, 82, 315],
        fill=FUJI_GRIS, outline="", smooth=False
    )
    # Ombre gauche du Fuji
    canvas.create_polygon(
        [200, 75, 240, 200, 82, 315],
        fill="#6A8EA8", outline="", smooth=False
    )
    # Neige au sommet
    canvas.create_polygon(
        [200, 75, 232, 148, 168, 148],
        fill=FUJI_NEIGE, outline="", smooth=False
    )
    # Base mer
    canvas.create_rectangle(0, 315, LARGEUR, HAUTEUR, fill=BLEU_PRUSSE, outline="")

# ── Fenêtre ────────────────────────────────────────────────
racine = tk.Tk()
racine.title("北斎 Pomodoro")
racine.geometry(f"{LARGEUR}x{HAUTEUR}")
racine.resizable(False, False)
racine.attributes("-topmost", True)

canvas = tk.Canvas(racine, width=LARGEUR, height=HAUTEUR, highlightthickness=0)
canvas.pack()

dessinerFond()

# ── Textes ─────────────────────────────────────────────────
canvas.create_text(
    LARGEUR // 2, 32,
    text=" Pomodoro",
    font=("Georgia", 13, "italic"),
    fill=BLANC_CREME, tags="ui"
)

textTimer = canvas.create_text(
    LARGEUR // 2, 222,
    text="25:00",
    font=("Courier", 58, "bold"),
    fill=BLANC_PUR, tags="ui"
)

textSession = canvas.create_text(
    LARGEUR // 2, 268,
    text="— travail —",
    font=("Georgia", 10, "italic"),
    fill=FUJI_NEIGE, tags="ui"
)

textCycle = canvas.create_text(
    LARGEUR // 2, 292,
    text=" cycle 0",
    font=("Helvetica", 8),
    fill=FUJI_GRIS, tags="ui"
)

# ── Boutons ─────────────────────────────────────────────────
boutonDemarrer = tk.Button(
    racine,
    text="▶ Démarrer",
    font=("Georgia", 12, "bold"),
    fg=BLANC_PUR,
    bg=ROUGE_JAPON,
    activebackground=ROUGE_FONCE,
    activeforeground=BLANC_PUR,
    relief="flat",
    padx=22, pady=9,
    cursor="hand2",
    bd=0,
    command=demarrer
)
canvas.create_window(LARGEUR // 2, 382, window=boutonDemarrer, tags="ui")

boutonPause = tk.Button(
    racine,
    text="☕ Faire une pause",
    font=("Georgia", 10),
    fg=BLANC_PUR,
    bg=BLEU_VAGUE,
    activebackground=BLEU_PRUSSE,
    activeforeground=BLANC_PUR,
    relief="flat",
    padx=18, pady=7,
    cursor="hand2",
    bd=0,
    command=lancerPause
)

# ── Lancement ──────────────────────────────────────────────
animer()
racine.mainloop()