import tkinter as tk

# ── Palette "Révisions" ────────────────────────────────────
FOND        = "#F7F3EC"   # Crème chaud (comme une page de carnet)
FOND_CARD   = "#EDE8DE"   # Légèrement plus foncé
BLEU        = "#4A7FA5"   # Bleu ardoise doux
BLEU_HOVER  = "#3A6A8E"   # Bleu survol
VERT        = "#6BAF8B"   # Vert sauge (pause)
TEXTE       = "#2C3E50"   # Anthracite lisible
TEXTE_DOUX  = "#7F8C8D"   # Gris secondaire
BLANC       = "#FFFFFF"

# ── Fonctions (à compléter ensemble) ──────────────────────
def demarrer():
    pass  # TODO : logique Pomodoro

def arreter():
    pass  # TODO : arrêter le timer

# ── Fenêtre principale ────────────────────────────────────
racine = tk.Tk()
racine.title("Timer")
racine.geometry("380x460")
racine.configure(bg=FOND)
racine.resizable(False, False)
racine.attributes("-topmost", True)

# ── En-tête ───────────────────────────────────────────────
frameEntete = tk.Frame(racine, bg=FOND)
frameEntete.pack(pady=(35, 0))

labelEmoji = tk.Label(
    frameEntete,
    text="📚",
    font=("Helvetica", 28),
    bg=FOND
)
labelEmoji.pack()

labelTitre = tk.Label(
    frameEntete,
    text="Pomodoro Révisions",
    font=("Georgia", 15, "bold"),
    fg=TEXTE,
    bg=FOND
)
labelTitre.pack(pady=(4, 0))

# ── Séparateur ────────────────────────────────────────────
tk.Frame(racine, height=1, bg=FOND_CARD).pack(fill="x", padx=40, pady=(18, 0))

# ── Label session ─────────────────────────────────────────
labelSession = tk.Label(
    racine,
    text="Session de travail",
    font=("Georgia", 10, "italic"),
    fg=TEXTE_DOUX,
    bg=FOND
)
labelSession.pack(pady=(18, 0))

# ── Affichage du timer ────────────────────────────────────
labelTimer = tk.Label(
    racine,
    text="25:00",
    font=("Courier", 68, "bold"),
    fg=TEXTE,
    bg=FOND
)
labelTimer.pack(pady=(6, 4))

# ── Numéro du cycle ───────────────────────────────────────
labelCycle = tk.Label(
    racine,
    text="● ○ ○ ○   Cycle 1 / 4",
    font=("Helvetica", 9),
    fg=TEXTE_DOUX,
    bg=FOND
)
labelCycle.pack(pady=(0, 20))

# ── Séparateur ────────────────────────────────────────────
tk.Frame(racine, height=1, bg=FOND_CARD).pack(fill="x", padx=40, pady=(0, 22))

# ── Bouton Démarrer ───────────────────────────────────────
boutonDemarrer = tk.Button(
    racine,
    text="▶   Démarrer la session",
    font=("Helvetica", 12, "bold"),
    fg=BLANC,
    bg=BLEU,
    activebackground=BLEU_HOVER,
    activeforeground=BLANC,
    relief="flat",
    padx=28,
    pady=11,
    cursor="hand2",
    command=demarrer
)
boutonDemarrer.pack(pady=(0, 10))

# ── Bouton Arrêter ────────────────────────────────────────
boutonArreter = tk.Button(
    racine,
    text="⏹   Arrêter",
    font=("Helvetica", 10),
    fg=TEXTE_DOUX,
    bg=FOND,
    activebackground=FOND_CARD,
    activeforeground=TEXTE,
    relief="flat",
    padx=20,
    pady=6,
    cursor="hand2",
    command=arreter
)
boutonArreter.pack()

# ── Lancer la fenêtre ─────────────────────────────────────
racine.mainloop()