import time

def afficherCompteARebours(temps):
    
    while temps!=0 :
            minutes=temps//60
            secondes=temps%60
            print(f"{minutes}:{secondes:02d}")
            temps-=1
            time.sleep(1)
        


def demanderPause():
    choix = input("veux tu faire une pause ? oui/non ")
    return choix =="oui"

def lancerCycle() :
    while True:
        afficherCompteARebours(1500)
        veutPause=demanderPause()
        if veutPause:
            afficherCompteARebours(400)
        
