import time

DUREE_TRAVAIL = 5
DUREE_PAUSE   = 2

def afficherCompteARebours(duree):
    
    while duree!=0 :
            minutes,secondes=calCulTemps(duree)
            print(f"{minutes}:{secondes:02d}")
            duree-=1
            time.sleep(1)
        
def calCulTemps (temps):
    minutes=temps//60
    secondes=temps%60
    return minutes,secondes
     

def demanderPause():
    choix = input("veux tu faire une pause ? oui/non ")
    return choix =="oui"

def lancerCycle() :
    while True:
        afficherCompteARebours(1500)
        veutPause=demanderPause()
        if veutPause:
            afficherCompteARebours(400)
        
