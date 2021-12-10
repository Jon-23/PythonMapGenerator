import Sprites.sprites as sprites
from math import floor
from random import randint,shuffle
import os
import modules_pratiques

import sys
sys.setrecursionlimit(10000)


class MapGenerator:
    format_sauvegarde = "map_interface"
    repertoire_maps = "Maps"
    interface_map = None
    donnee_map = None
    fichier = None
    Boucle_numero = 1

    def mise_a_jour_interface(self):
        self.interface_map = self.map_char_to_sprite(self.donnee_map)

    def _get_specefic_positions(self,element):
        donnee_retour = []
        for y in range(len(self.donnee_map)):
            for x in range(len(self.donnee_map[y])):
                if self.donnee_map[y][x]['value'] == element:
                    donnee_retour.append({'x':x,'y':y})
        return donnee_retour
    
    def get_available_positions(self):
        return self._get_specefic_positions(0)
        
    
    def place_les_items(self,items_p=[]):
        """
        item_p[x] = {'valeur':'x','position'={'x':0,'y':0}}
        """
        for i in range(len(items_p)):
            element = items_p[i]
            valeur = element.get('value')
            if valeur != None:
                position = element.get('position')
                if position != None:
                    self.add_item(position['x'],position['y'],str(valeur))
                else:
                    position = {}
                    
                    
                
        
        
    def add_item(self,x,y,type_p):
        if x < 0 and y <0:
            raise ValueError(f' x et y doivent être superieur à 0 x:{x} y:{y}')
        elif x > len(self.donnee_map[0])-1 or y > len(self.donnee_map)-1:
            raise ValueError(f' x et y doivent être inferieur à (x:{len(self.donnee_map[0])} ou y:{len(self.donnee_map)}) données saisie : x:{x} y:{y}')
        elif self.donnee_map[y][x]['value'] == 1:
            return 'La position contient un mur'
            #raise ValueError(f' La position contient un mur')
        elif self.donnee_map[y][x]['value'] == 0:
            self.donnee_map[y][x]['value'] = sprites.Items[type_p]
            self.mise_a_jour_interface()
            return "Fait"
        else:
            return f"Deja un item {self.donnee_map[y][x]['value']}"
        

    def save(self,fichier=None):
        if fichier == None:
            fichier = self.repertoire_maps+"/Map"+str(len(os.listdir(self.repertoire_maps)))
        else:
            if os.path.isfile(fichier+"."+self.format_sauvegarde):
                print("map deja existante")
                return False
        with open(fichier+"."+self.format_sauvegarde,'w',encoding="utf-8") as file:
            file.write(self.interface_map)
            
    
    def get_map(self):
        if self.donnee_map == None:
            print("Aucune map générée")
        else:
            return self.interface_map
        
    def genere_une_map(self,taillex,tailley):
        self.donnee_map = self.map_generate(taillex,tailley)
        self.interface_map = self.map_char_to_sprite(self.donnee_map)
        return self.get_map()
        
    def marche(self,x,y,map_p,numero):
        if x == -1 or y == -1 :
            raise ValueError(f'Position impossible x:{x} y:{y}')
        
        direction = [-1,0,1]
        
        #if(numero == 1):
        #    map_p[y][x]['value'] = 'x'
        #    map_p[y][x]['modifiable'] = False
        #elif(numero ==2):
        #    return map_p
        #    map_p[y][x]['value'] = 'U'
        #    map_p[y][x]['modifiable'] = False
        #else:
        #    return map_p
        
        y_max = len(map_p)
        x_max = len(map_p[y])
        a_mis_un_zero = False

        direction_possible = []
        for y_next in direction :
            for x_next in direction:
                if (x_next == (0-y_next) ) or (x_next == y_next) or (x_next == 0 and y_next == 0) or (x+x_next) <= 0 or (y+y_next) <= 0 or (x+x_next) >= x_max-1 or (y+y_next) >= y_max-1:
                    #print(f'Annule Position x:{x+x_next} y:{y+y_next}')
                    continue
                elif map_p[y+y_next][x+x_next]['modifiable'] == False :
                    continue
                else:
                    direction_possible.append({'x':x_next,'y':y_next})

            

        shuffle(direction_possible)
        #print(direction_possible)   
        position_disponible = []
        
        probabilitee = floor(len(direction_possible)/2)+1

        if(numero >10) :
            probabilitee += 1

        for i in range(len(direction_possible)):
            p = direction_possible[i]
            map_p[y+p['y']][x+p['x']]['modifiable'] = False
            if randint(1,probabilitee) == 1:
                map_p[y+p['y']][x+p['x']]['value'] = 0
                position_disponible.append({'x':x+p['x'],'y':y+p['y']})
            else:
                if probabilitee > 1:
                    probabilitee -=1

        for i in range(len(position_disponible)):
            p = direction_possible[i]
            map_p = self.marche(x+p['x'],y+p['y'],map_p,self.Boucle_numero+1)
            

        
        return map_p    
        


    def map_generate(self,sizeX,sizeY):
        if sizeX < 5:
            raise ValueError(f'La valeur de taille en x: {sizeX} est inferieur à {5} ')
        if sizeY < 5:
            raise ValueError(f'La valeur de taille en y: {sizeY} est inferieur à {5} ')
        map_binaire = [[{'value':1,'modifiable':True} for _ in range(sizeX)] for _ in range(sizeY)]
        map_binaire = self.marche(randint(1,floor(sizeX-2)),randint(1,floor(sizeY-2)),map_binaire,self.Boucle_numero)
        return map_binaire

    def map_char_to_sprite(self,map_binaire):
        sizeX = len(map_binaire[0])
        sizeY = len(map_binaire)
        affiche = ""
        for y in range(sizeY):
            for x in range(sizeX):
                if map_binaire[y][x]['value'] == 0:
                    affiche += ' '
                elif map_binaire[y][x]['value'] == 1:
                    appel = []
                    
                    if  y < (sizeY-1) :
                        if map_binaire[y+1][x]['value'] == 1:
                            appel.append('bas')
                    if y > 0:
                        if map_binaire[y-1][x]['value'] == 1:
                            appel.append('haut')
                    if x > 0:
                        if map_binaire[y][x-1]['value'] == 1:
                            appel.append('gauche')
                    if x < (sizeX-1):
                        if map_binaire[y][x+1]['value'] == 1:
                            appel.append('droite')
        
                    nom_appel = "-".join(appel)
                    if nom_appel == 'droite' or nom_appel == 'gauche':
                        nom_appel = 'gauche-droite'
                    elif nom_appel == 'bas' or nom_appel == 'haut' :
                        nom_appel = 'bas-haut'
                    #print(nom_appel)
                    affiche += sprites.Mur[nom_appel]
                else:
                    affiche += map_binaire[y][x]['value']
                
            
            affiche += "\n"
        return affiche

    def map_char_to_sprite_basic(self,map_binaire):
        sizeX = len(map_binaire[0])
        sizeY = len(map_binaire)
        affiche = ""
        for y in range(sizeY):
            for x in range(sizeX):
                if map_binaire[y][x]['value'] == 1 :
                    affiche += "#"
                else:
                    affiche += " "
                #affiche += str(map_binaire[y][x]['value'])
            affiche += "\n"
        
        return affiche
#MapGenerator()
#
#for i in range(10):
#    mapX = map_generate(randint(15,100),randint(15,100))
#    with open(repertoire_maps+'/map'+str(len(os.listdir(repertoire_maps)))+'.txt','w',encoding="utf-8") as fichier:
#        fichier.write(map_char_to_sprite(mapX))
#    #print(map_char_to_sprite_basic(mapX))
#    print(map_char_to_sprite(mapX))
    



#print(map_char_to_sprite(mapX2) == map_char_to_sprite(mapX))

Chronometre = modules_pratiques.Chrono()
Generateur = MapGenerator()
Generateur.genere_une_map(15,15)
print(Generateur.get_map())
print(Chronometre.stop())
