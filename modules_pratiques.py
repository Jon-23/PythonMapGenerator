import time

def est_dans_liste(element,liste):
    for i in range(len(liste)):
        if liste[i] == element:
            return {'reponse':True,'position':i}
    return {'reponse':False,'position':-1}

class Calendrier:
        
    def secondes_en_date(self,secondes_p):
        valeur_en_secondes = {'minute':60,
                              'heure':(60*60),
                              'jour':((60*60)*24)}
        annee = 1970
        secondes_p = int(secondes_p)
        secondes = secondes_p%60
        secondes_p = secondes_p-secondes
        minutes = (secondes_p%(60*60))//60
        secondes_p = secondes_p-(secondes_p%(60*60))

        heure = (secondes_p%((60*60*24)))//(60*60)
        secondes_p = secondes_p-(secondes_p%(60*60*24))
        jours = secondes_p//(60*60*24)

        
        annee_minimum = secondes_p//31536000
        jours_par_annee = []
        
        return {'jours':jours,'heures':heure,'minutes':minutes,'secondes':secondes}

    def _zero_devant(self,nombre):
        nombre = int(nombre)
        if nombre < 10:
            return "0"+str(nombre)
        return nombre
    def maintenant(self,format_zero = False):
        date = time.localtime()
        retour_date = {}
        retour_date['annee'] = date[0]
        retour_date['mois'] = date[1]
        retour_date['jour'] = date[2]
        retour_date['heure'] = self._zero_devant(date[3])
        retour_date['minute'] = self._zero_devant(date[4])
        retour_date['seconde'] = self._zero_devant(date[5])
        return retour_date

            
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
