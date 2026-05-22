import time

DUREE_TRAVAIL = 5
DUREE_PAUSE = 2


def afficher_compte_a_rebours(duree):
    while duree != 0:
        minutes, secondes = cal_cul_temps(duree)
        print(f"{minutes}:{secondes:02d}")
        duree -= 1
        time.sleep(1)


def cal_cul_temps(temps):
    minutes = temps // 60
    secondes = temps % 60
    return minutes, secondes


def demander_pause():
    choix = input("veux tu faire une pause ? oui/non ")
    return choix == "oui"


def lancer_cycle():
    while True:
        afficher_compte_a_rebours(1500)
        veut_pause = demander_pause()
        if veut_pause:
            afficher_compte_a_rebours(400)
