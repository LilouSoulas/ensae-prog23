from graph import Graph, graph_from_file, element_en_commun, pas_de_doublons, indice_min, kruskal
import copy


data_path = "input/"
file_name = "network.03.in"

"""

a=sorted([[1,2,4,5], [0,3,5,7], [0,0,0,0]])
print(a)
"""


g = graph_from_file(data_path + file_name)


a = kruskal(g)
print(a.graph)