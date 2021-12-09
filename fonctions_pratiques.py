def est_dans_liste(element,liste):
    for i in range(len(liste)):
        if liste[i] == element:
            return {'reponse':True,'position':i}
    return {'reponse':False,'position':-1}
