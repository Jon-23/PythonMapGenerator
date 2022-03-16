from map_generator import *


Chronometre = modules_pratiques.Chrono()
Generateur = MapGenerator()
Generateur.genere_une_map(15,15)
print(Generateur.get_map())
print(Chronometre.stop())
