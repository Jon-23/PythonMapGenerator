import time

def est_dans_liste(element,liste):
    for i in range(len(liste)):
        if liste[i] == element:
            return {'reponse':True,'position':i}
    return {'reponse':False,'position':-1}

class Calendrier:

    def _retire_le_reste_du_divisible(self,somme,divisible,rendu_simple=True):
        if somme < 0:
            somme%0
        reste_du_divisible = somme%divisible
        somme -= reste_du_divisible
        if rendu_simple:
            return {'restant_somme':somme,'reste_du_divisible':reste_du_divisible}
        else:
            return somme,reste_du_divisible
        
    def secondes_en_date(self,secondes_p):
        valeur_en_secondes = {'minute':60,
                              'heure':(60*60),
                              'jour':((60*60)*24)}
        secondes_p = int(secondes_p)
        secondes_p,secondes = self._retire_le_reste_du_divisible(secondes_p,valeur_en_secondes['minute'],False)
        secondes_p,minutes = self._retire_le_reste_du_divisible(secondes_p,valeur_en_secondes['heure'],False)
        secondes_p,heure = self._retire_le_reste_du_divisible(secon<des_p,valeur_en_secondes['jour'],False)
        
        return {'heures':heure,'minutes':minutes,'secondes':secondes}
    
    def maintenant(self):
        print("TODO")
            
    def est_bixestille(self,annee):
        if (annee%4)==0:
            if (annee%100) == 0:
                if (annee%400)==0:
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False
            

class Chrono:
    def __init__(self):
        self.start()

    def start(self):
        self.debut = time.time()
    
    def stop(self):
        self.fin = time.time()
        duree = self.fin-self.debut
        return duree
    def __del__(self):
        print(self.stop())
        
Date = Calendrier()
