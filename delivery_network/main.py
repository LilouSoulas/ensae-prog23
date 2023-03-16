from graph import Graph, graph_from_file, element_en_commun, pas_de_doublons, indice_min, kruskal
import copy


data_path = "input/"
file_name = "network.1.in"

"""

a=sorted([[1,2,4,5], [0,3,5,7], [0,0,0,0]])
print(a)
"""


g = graph_from_file(data_path + file_name)
#print(g)

#print(g.temps_necessaire())

print(g.get_path_with_power(2, 18, ))
"""


chemin = g.min_power(9, 10)
print(chemin)


chemin = g.get_path_with_power2(1, 3, 20)
print(chemin)




a=element_en_commun([1,2,4,5], [0,3,8,7])
print(a)

a=pas_de_doublons([1,2,4,5], [0,3,8,7])
print(a)

"""
