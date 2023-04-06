from graph import Graph, graph_from_file, element_en_commun, pas_de_doublons, indice_min, kruskal, routes_out, selection_camion, routes_to_dico, truck_to_dico, new_kruskal
import copy


data_path = "input/"
file_name = "network.00.in"


g = graph_from_file(data_path + file_name)
k=kruskal(g)
#g.montre_le_chemin("petitcouleur", 8, 10, 20)
g.montre_le_chemin_sans("avant kruskal", 4, 8, 11)



"""
#traj, power=g.min_power(6,11)
#print(traj)
#print(power)
#print(routes_out(file_name))

#print(g)

#print(g.temps_necessaire())




chemin = g.min_power(9, 10)
print(chemin)


chemin = g.get_path_with_power2(1, 3, 20)
print(chemin)




a=element_en_commun([1,2,4,5], [0,3,8,7])
print(a)

a=pas_de_doublons([1,2,4,5], [0,3,8,7])
print(a)

"""





