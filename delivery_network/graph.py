import copy, time
from graphviz import Graph as gr
 

class Graph:
    def __init__(self, nodes=[]):
        self.nodes = nodes
        self.graph = dict([(n, []) for n in nodes])
        self.nb_nodes = len(nodes)
        self.nb_edges = 0
    

    def __str__(self):
        """Prints the graph as a list of neighbors for each node (one per line)"""
        if not self.graph:
            output = "The graph is empty"            
        else:
            output = f"The graph has {self.nb_nodes} nodes and {self.nb_edges} edges.\n"
            for source, destination in self.graph.items():
                output += f"{source}-->{destination}\n"
        return output
    
    def add_edge(self, node1, node2, power_min, dist=1):
        """
        Adds an edge to the graph. Graphs are not oriented, hence an edge is added to the adjacency list of both end nodes. 

        Parameters: 
        -----------
        node1: NodeType
            First end (node) of the edge
        node2: NodeType
            Second end (node) of the edge
        power_min: numeric (int or float)
            Minimum power on this edge
        dist: numeric (int or float), optional
            Distance between node1 and node2 on the edge. Default is 1.
        """
        
        self.graph[node1].append( (node2, power_min, dist) )
        self.graph[node2].append( (node1, power_min, dist) )
        self.nb_edges += 1



    """
    def get_path_with_power(self, dep, dest, power):
    
        print("la fonction get_path_with_power est lancée")

        position=dep                                        # on se place à la positio de départ
                            
        le_chemin_optimal=[[dep]]   
        distance=[0]                        # on creer un liste qui va contenir tous les chemins possibles en partant de départ
        while le_chemin_optimal!=[]:                        # tant que la grosse liste qui contiet tous les chemins possibles n'est pas vide:
            
            print("--------------------DEPART-boucle while-------------------------")
            print("le chemin optimal départ", le_chemin_optimal)
            sauv=copy.deepcopy(le_chemin_optimal)           # on stock dans sauv les chemins possibles déja établis
            
            for j in range(0,len(sauv)): 
                print("---------DEPART-boucle for chemin étudié: j=", j)
                chemin_simple=sauv[j]                       # on récupere chaque chemin et on fait:
                print(" chemin étudié:", chemin_simple) 
                position=chemin_simple[-1]                  # on récupere la derniere postion de ce chemin
                voisin=self.graph[position]                 # on recupere dans la variable voisin les voisins proches de position
                print("les voisins de position", position, "sont", voisin)

                for i in voisin:                            #pour chaque voisin:
                    print("--------------DEPART - boucle for chaque voisin")
                    print("le voisin considéré est:", i)
                    print("power_camion=", power, "puissance_route=", i[1])

                    chem=copy.deepcopy(chemin_simple) 
                    liste_voisins=chem
                    print("le chemin consideré est", chem)

                    if len(chem)==1 and i[0]!=dest and power >= i[1]:       # si le camion est a son premier tronçon et que la power est ok
                        print("premier chemin fait")
                        liste_voisins.append( i[0])                         # on met dans liste_voisins la position suivante
                        print("nouveau chemin:", liste_voisins)
                        le_chemin_optimal.append(liste_voisins) 
                        print("ancienne distance=", distance[0])
                        distance.append(distance[0]+i[2])
                        print("nouvelle distance=", distance[0]+i[2])            # on met dans le chemin optimal le nouveau trajet possible
                        print("le chemin optimal=", le_chemin_optimal)
                        print("la nouvelle distance=", distance)

                    elif len(chem)>1 and i[0] != chem[-2] and i[0]!=dest and power >= i[1]: # si le camion va en avant, n'est pas arrivé a destination, et a une puissance suffisante
                        print("Camion va en avant + assez de puissance + trajet non fini")
                        liste_voisins.append( i[0])
                        print("nouveau chemin", liste_voisins)
                        le_chemin_optimal.append(liste_voisins)
                        print("ancienne distance=", distance[0])
                        print("l'ancien vecteur de distance", distance)
                        print("nouvelle distance=", distance[0]+i[2])            # on met dans le chemin optimal le nouveau trajet possible
                        
                        distance.append(distance[0]+i[2])
                        print("chem opti=", le_chemin_optimal)
                        print("la nouvelle distance=", distance)


                    elif len(chem)>1 and i[0] != chem[-2] and i[0]==dest and power >= i[1]:  # si le camion va en avant, est arrivé a dest et la puissance est ok
                        print("Camion en avant + assez de puissance + trajet terminé")
                        liste_voisins.append( i[0])
                        print("ancienne distance=", distance[0])
                        print("nouvelle distance=", distance[0]+i[2])
                        distance.append(distance[0]+i[2])
                        le_chemin_optimal.append(liste_voisins)
                        le_chemin_optimal.pop(0)  #on enlève le chemin d'avant
                        distance.pop(0)
                        print("nouvelle distance=", distance)
                        print("chem opti=", le_chemin_optimal)


                        return liste_voisins, distance[-1]
                    
                    elif len(chem)>1 and i[0] == chem[-2]:
                        print("le camion ne veut pas reculer")
                    
                print("------------fin boucle chemin considéré ---------------- ")
                print("------------fin boucle chaque voisin--------------------")
                le_chemin_optimal.pop(0)  #on enlève le chemin d'avant
                distance.pop(0)
                print("distancefinale", distance)
                print("le chemin optimalfinal", le_chemin_optimal)
                
        return None # si le_chemin_optimal est vide, on retourne None

   
    #-----------------------get path with power avec distance---------------------------------------------
"""
           
    def chemin_optimal_avec_distance(self, dep, dest, power):
        """
        Pour un graph donné, on prend en entréé le départ dep, la destination dest et la puissance du camion power.
        Renvoi le chemin optimal si le camion est assez puissant pour passer, ou renvoi None si jamais aucun chemin n'est valide.
        Si plusieurs chemins sont possibles, il renvoi le chemin le plus court en terme de distance
        Pour répondre a la question il faudrait analyser la complexité de l'algorythme
        
        """
        #print("la fonction get_path_with_power est lancée")


        t1=time.perf_counter()
        print("--------------------------------------")
        position=dep                                        # on se place à la positio de départ
                            
        le_chemin_optimal=[[dep]]   
        distance=[0]                        # on creer un liste qui va contenir tous les chemins possibles en partant de départ
        chemins_qui_marchent=[]
        distances_qui_marchent=[]

        while le_chemin_optimal!=[]:                        # tant que la grosse liste qui contiet tous les chemins possibles n'est pas vide:
            
            #print("--------------------DEPART-boucle while-------------------------")
            #print("le chemin optimal départ", le_chemin_optimal)
            sauv=copy.deepcopy(le_chemin_optimal)           # on stock dans sauv les chemins possibles déja établis
            
            for j in range(0,len(sauv)): 
                #print("---------DEPART-boucle for chemin étudié: j=", j)
                chemin_simple=sauv[j]                       # on récupere chaque chemin et on fait:
                #print(" chemin étudié:", chemin_simple) 
                position=chemin_simple[-1]                  # on récupere la derniere postion de ce chemin
                voisin=self.graph[position]                 # on recupere dans la variable voisin les voisins proches de position
                #print("les voisins de position", position, "sont", voisin)

                for i in voisin:                            #pour chaque voisin:
                    #print("--------------DEPART - boucle for chaque voisin")
                    #print("le voisin considéré est:", i)
                    #print("power_camion=", power, "puissance_route=", i[1])

                    chem=copy.deepcopy(chemin_simple) 
                    liste_voisins=chem
                    #print("le chemin consideré est", chem)

                    if len(chem)==1 and i[0]!=dest and power >= i[1] and i[0]!=dep:       # si le camion est a son premier tronçon et que la power est ok
                        #print("premier chemin fait")
                        liste_voisins.append( i[0])                         # on met dans liste_voisins la position suivante
                        #print("nouveau chemin:", liste_voisins)
                        le_chemin_optimal.append(liste_voisins) 
                        #print("ancienne distance=", distance[0])
                        distance.append(distance[0]+i[2])
                        #print("nouvelle distance=", distance[0]+i[2])            # on met dans le chemin optimal le nouveau trajet possible
                        #print("le chemin optimal=", le_chemin_optimal)
                        #print("la nouvelle distance=", distance)

                    elif len(chem)>1 and i[0] != chem[-2] and i[0]!=dest and power >= i[1] and i[0]!=dep: # si le camion va en avant, n'est pas arrivé a destination, et a une puissance suffisante pas de boucle, le camion ne peut pas repasser par l'endroit de départ
                        #print("Camion va en avant + assez de puissance + trajet non fini + pas de boucle")
                        liste_voisins.append( i[0])
                        #print("nouveau chemin", liste_voisins)
                        le_chemin_optimal.append(liste_voisins)
                        #print("ancienne distance=", distance[0])
                        #print("l'ancien vecteur de distance", distance)
                        #print("nouvelle distance=", distance[0]+i[2])            # on met dans le chemin optimal le nouveau trajet possible
                        
                        distance.append(distance[0]+i[2])
                        #print("chem opti=", le_chemin_optimal)
                        #print("la nouvelle distance=", distance)


                    elif len(chem)>1 and i[0] != chem[-2] and i[0]==dest and power >= i[1] and i[0]!=dep:  # si le camion va en avant, est arrivé a dest et la puissance est ok + pas de boucle
                        #print("Camion en avant + assez de puissance + trajet terminé + pas de boucle")
                        liste_voisins.append( i[0])
                        #print("ancienne distance=", distance[0])
                        #print("nouvelle distance=", distance[0]+i[2])
                        #print("nouvelle distance=", distance)
                        #print("chem opti=", le_chemin_optimal)

                        chemins_qui_marchent.append(liste_voisins)   #on stock dans chemin_qui_marchent les chemins possibles et on met la distance associée dans distance_qui_marche
                        distances_qui_marchent.append(distance[0]+i[2])

                        #return liste_voisins, distance[-1]
                    
                    elif len(chem)>1 and i[0] == chem[-2]:
                        print("le camion ne veut pas reculer")
                    
                #print("------------fin boucle chemin considéré ---------------- ")
                #print("------------fin boucle chaque voisin--------------------")
                le_chemin_optimal.pop(0)  #on enlève le chemin d'avant
                distance.pop(0)
                #print("distancefinale", distance)
                #print("le chemin optimalfinal", le_chemin_optimal)

                #print("distances_qui_marchent=", distances_qui_marchent)
                #print("chemn qui ùarchent=", chemins_qui_marchent)

        
        if len(chemins_qui_marchent) > 1:  #on récupere le chemin avec le moins de distance possible
            indice_du_min=indice_min(distances_qui_marchent)
            t2=time.perf_counter()
            print("time:", t2-t1)
            print("time:", t2-t1)

            print("t2-----------------------")
            return chemins_qui_marchent[indice_du_min]


        if len(chemins_qui_marchent)==1:
            t2=time.perf_counter()
            print("t2-----------------------")
            print("time:", t2-t1)
            return chemins_qui_marchent[0]
        
       
                      
        return None # si le_chemin_optimal est vide, on retourne None




    def get_path_with_power(self, dep, dest, power):
        ancetre={}   # le dictionnaire des ancètres
        ou_est_on=[dep] # notre liste des positions
        position=dep # notre posotion de départ
        
        recul=[] # notre liste des endroits ou l'on est déja allés pour éviter de faire demi tour

        while position!=dest: # tant que notre position actuelle n'est pas égale à la destination on fait:
            les_voisin=self.graph[position] # on récupere tous les voisins de notre position considérée
            for voisin in les_voisin: # pour chaque voisin
                if voisin[0] not in recul and power > voisin[2]: # si la puissance est o et qu'on ne recule pas:
                    ou_est_on.append(voisin[0]) # on ajoute les positions suivante a notre liste de positions
                    ancetre[voisin[0]]=position # on ajoute au dictionnaire des ancètres l'ancetre du voisin considéré


            ou_est_on.pop(0) # on retire la position traitée de la liste de positions
            recul.append(position) # on ajoute la position traitée à la liste des positions déja traitée
            if ou_est_on!=[]: # juste pour le dernier tour sinon out of range
                position=ou_est_on[0]
            

        # on retrace le chemin inverse
        chemin_opti=[dest]
        pose=dest
        while pose != dep:
            chemin_opti.append(ancetre[pose])
            pose=ancetre[pose]

        # on retourne la liste
        chemin_opti.reverse()

        return chemin_opti

                






            




    




        #liste on on rajoute tous les voisins et on pop le truc d'avant

    def connected_components(self):  
        """
        Pour un graph donné, renvoi des listes contenant tous les élements relié ensembles
        """
        print("début de la fonction connected_components")

        # PREMIERE ETAPE: On fait des paquets de noeuds connectés ensemble.

        tous_les_chemins=[]   
        for cle in self.nodes:  # pour chaque noeud donné:
            chemin=[cle]        # on creer une liste "chemin" ou on stock le noeud ue l'on étudie
            liste=self.graph[cle]  # on récupere la liste des noeuds connectés avec notre noeud donné
            for i in liste:      # pour chaque noeud connecté à la clé:
                chemin.append(i[0])   #on ajoute a notre liste chemin tous les neouds qui sont connecté a la clé
            tous_les_chemins.append(sorted(chemin)) #on ajoute a la grosse liste des chemins la liste de tous les neouds connectés associé a la clé

        # DEUXIEME ETAPE: On creer les paquets finaux d'éléments en commun

        tous_les_chemins=sorted(tous_les_chemins)
        compteur=0

        while compteur < 5:  #le compteur calcul si les listes a l'étape n et n-1 sont les memes. Si elles sont les meme 5 fois de suites, on peut penser que la boule est fini et qu'il n'y a plus rien a fusionner

            if len(tous_les_chemins)!=1:   #si tous les chemins contient plusiseurs paquets:

                sauvegarde=copy.deepcopy(tous_les_chemins)  # on fait une sauvegarde qui servira a comparer si il y a eu un changement
                liste1=tous_les_chemins[0]  #on recupere les deux premiers paquets de tous les chemins
                liste2=tous_les_chemins[1]

                if element_en_commun(liste1, liste2) == 1: #si les deux paquest ont un element en commun:
                    new= pas_de_doublons(liste1, liste2) #on fusionne les deux listes et on enlève les doublons puis...
                    tous_les_chemins.remove(liste1)  #... on supprime les deux paquets originaux pour mettre dans tous les chemins le paquets conctitué de la fusion
                    tous_les_chemins.remove(liste2)
                    tous_les_chemins.append(new)
            
                else:                                  # si les deux paquets n'ont aucuns elements en commun:
                    tous_les_chemins.remove(liste1)  # on passe au fond de tous les chemins le premier paquet
                    tous_les_chemins.append(liste1)

                sauvegarde=sorted(sauvegarde)  #on trie les deux sauvagarde pour les comparer
                sauvegarde1=tous_les_chemins
                sauvegarde1=sorted(sauvegarde1)

                print("tous les chemins=", tous_les_chemins)
                if sauvegarde==sauvegarde1: #si les deux sauvegardes avant et après la manipulation des paquets sont identiques: pas de modifs
                    compteur+=1 #on ajoute 1 au compteur pour savoir si c'est vraiment fini et la boucle tourne sur elle meme ou c'était juste pas de chance avec ces deux pauets la

                else:  # sinon on remet le compteur a 0
                    compteur=0
                
            
            elif len(tous_les_chemins)==1: #si il n'y a qu'un seul element on le renvoi, c'est que le smilblick est fini
                return tous_les_chemins
            
        return tous_les_chemins


    def connected_components_set(self):
        """
        Prend ma fonction connected_components et transforme le resultat en frozensets
        The result should be a set of frozensets (one per component), 
        For instance, for network01.in: {frozenset({1, 2, 3}), frozenset({4, 5, 6, 7})}
        """
        return set(map(frozenset, self.connected_components()))
    



    def min_power(self, dep, dest):
        
        trajet=self.get_path_with_power2(dep, dest, power=999999999999999999)
        puissance=0
        for k in range(0, len(trajet)-1): #trajet=[1,2,3,4]

            pt1=trajet[k]  #1
            pt2=trajet[k+1] #2
            liste=self.graph[pt1] #[(2, 11, 1), (6, 12, 1), (8, 0, 1)]

            for i in liste:         #(2,11,1)
                if i[0]==pt2:   #2==2
                    pui=i[1]
            
            if pui>puissance:
                puissance=pui
            

        return trajet, puissance 

            
    def representation(self, nom):

        graphe = gr(format='png', engine="circo")

        key=self.graph.keys()
        sauv=[]

        for i in key: # on creer tous les sommets
            print(i)
            graphe.node(f"{i}",f"{i}")
            for voisin in self.graph[i]:
                if voisin[0] not in sauv:
                    graphe.edge(f"{i}", f"{voisin[0]}", label=f"p={voisin[1]},\n d={voisin[2]}")
            
            sauv.append(i)


        graphe.render(f"{nom}.dot")
        print(graphe)

        return()
    

# ------------------ NOUVEL ESSAI -------------------------------

    def montre_le_chemin(self, nom,  dep, dest, power):

        graphe = gr(format='png', engine="circo") # on creer un graph
        trajet=self.get_path_with_power2(dep, dest, power)
        key=self.graph.keys() # on récupere tous les sommets
        sauv=[]
        print("trajet=", trajet)

        for i in key: # on creer tous les sommets
            print(i)
            if i==dep: # si le sommet considéré est le départ
                print("le depart=", i)
                graphe.node(f"{i}",f"{i} \n départ", color="red")   # si le sommet est le départ, on le met en rouge
                for voisin in self.graph[i]:
                    print("le voisin est=", voisin)
                    print("trajet[1]=", trajet[1])
                                              
                    if voisin[0] not in sauv: # si le voisin n'as pas déja étét traité
                        print("entrée dans la boucle")
                        if voisin[0]==trajet[1]:
                            graphe.edge(f"{i}", f"{voisin[0]}", label=f"p={voisin[1]},\n d={voisin[2]}", color="red")
                            print("on met en rouge")
                        else: 
                            graphe.edge(f"{i}", f"{voisin[0]}", label=f"p={voisin[1]},\n d={voisin[2]}")

            
            elif i==dest: # si le sommet considéré est l'arrivée
                graphe.node(f"{i}",f"{i} \n arrivée", color="red")  
                for voisin in self.graph[i]:
                    if voisin[0] not in sauv: # si le voisin n'as pas déja étét traité
                        if voisin[0]==trajet[-2]:
                            graphe.edge(f"{i}", f"{voisin[0]}", label=f"p={voisin[1]},\n d={voisin[2]}", color="red")
                        else: 
                            graphe.edge(f"{i}", f"{voisin[0]}", label=f"p={voisin[1]},\n d={voisin[2]}")


            elif i in trajet: # si le voisin considéré est dans le trajet
                print("position du voisin dans trajet=", i)
                graphe.node(f"{i}",f"{i} ", color="orange")
                rang=trajet.index(i)
                for voisin in self.graph[i]:
                    if voisin[0] not in sauv: # si le voisin n'as pas déja étét traité
                        if voisin[0]==trajet[rang+1] or voisin[0]==trajet[rang-1]:
                            graphe.edge(f"{i}", f"{voisin[0]}", label=f"p={voisin[1]},\n d={voisin[2]}", color="red")
                            print("on met en rouge")
                        else: 
                            graphe.edge(f"{i}", f"{voisin[0]}", label=f"p={voisin[1]},\n d={voisin[2]}")


            else: # sinon
                graphe.node(f"{i}",f"{i}")
                for voisin in self.graph[i]:
                    if voisin[0] not in sauv: # si le voisin n'as pas déja étét traité
                        graphe.edge(f"{i}", f"{voisin[0]}", label=f"p={voisin[1]},\n d={voisin[2]}")
            
            sauv.append(i)


        graphe.render(f"{nom}.dot")
        print(graphe)

        return()
    

     

        


def graph_from_file(filename):
    """
    Reads a text file and returns the graph as an object of the Graph class.

    The file should have the following format: 
        The first line of the file is 'n m'
        The next m lines have 'node1 node2 power_min dist' or 'node1 node2 power_min' (if dist is missing, it will be set to 1 by default)
        The nodes (node1, node2) should be named 1..n
        All values are integers.

    Parameters: 
    -----------
    filename: str
        The name of the file

    Outputs: 
    -----------
    G: Graph
        An object of the class Graph with the graph from file_name.
    """


    fichier = open(filename, "r")
    first_line=fichier.readline()
    nb_node=int(first_line[:first_line.find(" ")])
    print(nb_node)
    nb_edge=int(first_line[first_line.find(" "):-1])
    print(nb_edge)
    

    G = Graph(range(1, nb_node+1))


    line=[]
    for i in range( nb_edge):
        print(i)
        line=fichier.readline()
        ligne_split=line.split(" ")
        print(ligne_split)
        noeud1=ligne_split[0]
        noeud2=ligne_split[1]
        power=ligne_split[2]
        print("len=",len(ligne_split))
        if len(ligne_split)==4:
            distance=ligne_split[3]
            G.add_edge(int(noeud1), int(noeud2) ,  int(power), int(distance))
        else:
            G.add_edge(int(noeud1), int(noeud2) ,  int(power))

    return G


def element_en_commun(liste1, liste2):
    "compare deux listes et renvoi 1 si des elements sont communs aux deux listes, renvoi 0 sinon"
    sauv=0   #compteur pour savoir element en commun
    liste1=sorted(liste1)
    liste2=sorted(liste2)
  
  
    for i in liste1:         #on regarde si il y a des éléments en commun
        for j in liste2:
            if j==i:
                sauv=sauv+1

    if sauv > 0:
        return 1
    else:
        return 0
    


def pas_de_doublons(liste1, liste2):
    "enlève les doublons d'une liste composée de deux listes"
    final = liste1 + liste2
    final = list(set(final))
    final=sorted(final)
    return final
            
	
def indice_min(liste):
    min = liste[0]
    indice = 0
    for i in range(len(liste)):
        if liste[i] <= min:
            min = liste[i]
            indice= i
    return indice




def kruskal(g):
    "renvoi un graph dont il ne reste que les arretes qui ne font pas de cycle et dont es arretes sont de poids minimal"

    sommets=list(g.graph.keys()) # on récupere tous les sommets
    print("sommets=", sommets)
    new_sommets=[]


    # On récupere les chemins et les puissances dans deux listes
    chemin=[]
    power=[]
    sauv=[]

    for i in sommets: # on creer tous les sommets
        print("i=",i)
        for voisin in g.graph[i]:
            print(voisin[0])
            if voisin[0] not in sauv:
                int=[]
                int.append(i)
                int.append(voisin[0])

                chemin.append(int)
                power.append(voisin[1])
        
        sauv.append(i)
        print("sauv=", sauv)
        print("chemin=",chemin)
        print("power=",power)

    G = Graph(range(1, len(sommets)+1))
    print("premiere étape passée -----------")
    # On prend le plus petit poids et on creer un graph avec cette arrête

    while new_sommets!=sommets:

        #On prend la liaison de plus petit poids
        ind_mn=indice_min(power)
        print("indicemin=", power[ind_mn])
        plus_ptt_poids=chemin[ind_mn]
        print("plus_petit_poids=", plus_ptt_poids)

        G.add_edge(plus_ptt_poids[0], plus_ptt_poids[1], power[ind_mn])

        chemin.pop(ind_mn)
        power.pop(ind_mn)
        print("test",plus_ptt_poids[0])
        new_sommets.append(plus_ptt_poids[0])
        new_sommets.append(plus_ptt_poids[1])
        
        new_sommets=list(set(new_sommets))
        new_sommets=sorted(new_sommets)

        print("new_sommets=", new_sommets)


    return G





