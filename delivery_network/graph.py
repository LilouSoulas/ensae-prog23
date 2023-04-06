import copy, time, random, sys 
from graphviz import Graph as gr
 
sys.setrecursionlimit(10000)

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
        print("get_path_with_power")

        #BSF qui marche
        #Retourne le chemin optimale selon la puissance du camion

        ancetre={}   # le dictionnaire des ancètres
        ou_est_on=[dep] # notre liste des positions
        position=dep # notre posotion de départ
        k=0
        recul=[] # notre liste des endroits ou l'on est déja allé pour éviter de faire demi tour

        while position!=dest: # tant que notre position actuelle n'est pas égale à la destination on fait:
            les_voisins=self.graph[position] # on récupere tous les voisins de notre position considérée
            
            for voisin in les_voisins: # pour chaque voisin
                if voisin[0] not in recul and power >= voisin[1] : # si la puissance est o et qu'on ne recule pas:
                    ou_est_on.append(voisin[0]) # on ajoute les positions suivantes a notre liste de positions
                    ancetre[voisin[0]]=position # on ajoute au dictionnaire des ancètres l'ancetre du voisin considéré

            ou_est_on.pop(0) # on retire la position traitée de la liste de positions
            recul.append(position) # on ajoute la position traitée à la liste des positions déja traitée

            if ou_est_on!=[]: # juste pour le dernier tour sinon out of range
                
                position=ou_est_on[0]
            else:
                return None
            k=k+1

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
        # Renvoi les éléments qui sont reliés entre eux dans un graph
        # !!! SERT POUR LES GRAPHS QUI SONT PLUS PETITS OU EGALS A 100000 SOMMETS !!!
        déja_vu = set() # on initialise un set qui va contenir tous les noeuds déja traités
        tous_les_elements_connectés = [] # on initialise une liste qui va contenir tous les paquets d'éléments connectés
        for noeud in self.graph: # pour chaque noeuds du graph:
            if noeud not in déja_vu: # si le noeud n'a pas déja été traité:
                elements_connecté = set() # on creer un set qui va contenir les elements connectés avec ce noeud
                print("-------------on entre en DFS-----------")
                self.DFS(noeud, déja_vu, elements_connecté) # on utiilise le DFS voir ci dessous
                tous_les_elements_connectés.append(elements_connecté) # on ajoute a notre grosse liste de tous les éléments connectés le paquets d'éléments cpnnectés que l'on vient de faire
        return tous_les_elements_connectés

    def DFS(self, noeud, déja_vu, elements_connectés):
        # !!! SERT POUR LES GRAPHS QUI SONT PLUS PETITS OU EGALS A 100000 SOMMETS !!!
        
        # ne renvoi rien car elle stock des informations en mémoire
        déja_vu.add(noeud) # on ajoute à déja vu le noeud traité
        elements_connectés.add(noeud) # on ajoute a nos éléments connectés le noeud traité
        for voisin in self.graph[noeud]: # pour chaque voisin:
            if voisin[0] not in déja_vu: # si le voisin n'a pas déja été traité:
                counter += 1
                self.DFS(voisin[0], déja_vu, elements_connectés) # on utilise le DFS pour ecommencer jusqu'a ce qu'il n'y ai plus de voiins à traiter

    def connected_components2(self):  
        """
        Pour un graph donné, renvoi des listes contenant tous les élements relié ensembles
        Autre facon de le coder qu'on a laissé ici mais on preferera utiliser la fonction avec le DFS car plus optimisée


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
        return set(map(frozenset, self.connected_components2()))
    
    def min_power_non(self, dep, dest):
        # Trouve le chemin optimal et calcul la puissance minimale necessaire pour passer sur ce chemin

        # COMPLEXITE DE MIN_POWER : complexité en max(complexité de get_path_with_power, longueur de trajet * longuer de liste)
        
        trajet=self.get_path_with_power(dep, dest, power=999999999999999999)
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
    
    def bornes_power(self):

        min=100000000000
        max=0
        for noeud in self.nodes:
            for voisin in self.graph[noeud]:
                if voisin[1]<min:
                    min=voisin[1]
                if voisin[1]>max:
                    max=voisin[1]

        return min, max

    def min_power(self, dep, dest):
        print("min_power")
        # Trouve le chemin parmis tous les chemins qui necessite le moins de puissance

        pmin, pmax= self.bornes_power()
        dicoto=(pmax-pmin)/2
        dicotomin=pmin
        dicotomax=pmax
        
        i=0
        
        while dicotomin+1<dicotomax:
        
            print("dans min power, juste avant de faire geth_path: dep=", dep, "dest=", dest, "dicoto=", dicoto)
            trajet=self.get_path_with_power(dep, dest, power=dicoto)
            print("dans min power: trajet=", trajet)
            if trajet==None:
                dicotomin=dicoto
                dicoto=dicotomin+(dicotomax-dicotomin)/2
            else:
                dicotomax=dicoto
                dicoto=dicotomin+(dicotomax-dicotomin)/2  
            i+=1

        dicoto=int(dicotomax)

        return dicoto             


        
            

        return trajet, puissance 

    def representation(self, nom):

        # Permet d'affciher le graph

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
    
    def montre_le_chemin(self, nom,  dep, dest, power):

        # Permet d'afficher le graph, et de mettre en évidence l'arrivée, le départ et le chemin optimal.

        graphe = gr(format='png', engine="circo") # on creer un graph
        trajet=self.get_path_with_power(dep, dest, power)
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
    
    def temps_necessaire(self):
        #fonction de jul, temps necessaire pour calculer la puissnace minimale et le chemin associé, ie get_path_with_power
        temps = []
        # !! NE MARCHE QUE POUR DES GRAPHS DONT SOMMETS < 100 000 !!
        #nb_chemin_possible=self.Nombre_de_chemin()  # on devrait prendre la fonction Nombre de chemin mais comme elle ne calcule que pour le sgra^hs < 100000 sommets, on prend n**2 comme le nombre de chemins possibles
        nb_chemin_possibles = self.nb_nodes**2
        for i in range(6):
            print("tour numero", i)
            a = random.randint(0,self.nb_nodes)
            b = random.randint(0,self.nb_nodes)
            t1 = time.perf_counter()
            c = self.get_path_with_power(a,b,9999999999999999999999999999)
            t2 = time.perf_counter()
            temps.append(t2-t1)
        moyenne_temps=sum(temps)/len(temps)
        temps_necessaire=moyenne_temps*nb_chemin_possibles
        return temps_necessaire

    def Nombre_de_chemin(self):
        # on calcul combien de composentes connexes on a et on fait le nombre de sommets de ces composantes au carré. On fait la somme
        compo_connex=self.connected_components()
        compte_trajets=0
        
        for paquet in compo_connex:
            nb_noeuds=len(paquet)
            compte_trajets += (nb_noeuds)**2

        return compte_trajets

    def min_power_kruskal(self,dep,dest):
        g = self.kruskal() #kruskal fonction qui nous renvoie un arbre couvrant de poids minimal 
        return g.min_power(dep,dest)
    
    def dfs(self, node, previous= {}, father = 0, c = 0, p = 0):
        """
        Return the dictionnary of the previous nodes, starting with the node initial node in argument
        As we consider the graph to be related it works
        """
        previous[node] = (father, c, p)
        for son, power, distance in self.graph[node]:
            if son != father:
                self.dfs( son, previous, father = node, c = c+1, p = power)
        return previous

    def get_path(self, previous, dep, dest):
    # prend une source et une destintion et renvoi le chemin otpimal
    # Les graphes sont connexes, donc osef de vérifier qu'ils appartienent à la même composante
        power = {0}
        condition = previous[dest][1] < previous[dep][1]
        if condition:     # on veut toujours partir du point le plus loin du noeud mère.
            dep, dest = dest, dep

        path1, node1 = [dest], dest
        path2, node2 = [dep], dep

        while previous[node1][1] > previous[node2][1]:
            node1, new_power = previous[node1][0], previous[node1][2]
            path1.insert(0,node1)
            power.add(new_power)
        while node1 != node2:
            node1, new_power = previous[node1][0], previous[node1][2]
            path1.insert(0,node1)
            power.add(new_power)

            node2, new_power = previous[node2][0], previous[node2][2]
            power.add(new_power)
            if node2 != node1:
                path2 += [node2]

        path = path2 + path1
        min_power = max(power)
        if condition :
            path.reverse()

        return path, min_power

    def new_min_power(self, previous, source, dest):
        return self.get_path(previous, source, dest)[1]
    


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
    nb_edge=int(first_line[first_line.find(" "):-1])
    
    G = Graph(range(1, nb_node+1))

    line=[]
    for i in range( nb_edge):
        line=fichier.readline()
        ligne_split=line.split(" ")
        noeud1=ligne_split[0]
        noeud2=ligne_split[1]
        power=ligne_split[2]
        if len(ligne_split)==4:
            distance=ligne_split[3]
            G.add_edge(int(noeud1), int(noeud2) ,  int(power), float(distance))
        else:
            G.add_edge(int(noeud1), int(noeud2) ,  int(power))

    return G

def routes_out(filename):
    # Creer un nouveau fichier qui contient les puissances minimales des chemins optimaux associés à un fichier routes
    # On récupere le numero du fichier routes in associé
    nom= filename.split(".")
    print("nom=", nom)
    fichier_out = open("input/" + "routes." + f"{nom[1]}" + ".out", "w")
    fichier_in = open("input/" + filename, "r")
    first_line=fichier_in.readline()

    print('input/'+  'network.' + f"{nom[1]}" + ".in")
    g, previous=new_kruskal(graph_from_file( 'input/'+  'network.' + f"{nom[1]}" + ".in" ))
    fichier_out.write(first_line)

    for _ in range(int(first_line)):
        line=fichier_in.readline()
        ligne_split=line.split(" ")
        dep=int(ligne_split[0])
        dest=int(ligne_split[1])
        print("dest", dest, "dep", dep)
        print(type(g))
        power=g.new_min_power(previous, dep, dest)
        print("power=", power)
        fichier_out.write(str(dep) + " " + str(dest) + " " + str(power) + "\n")

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

class UnionFind:

    def __init__(self, n):  #n nombre de sommets du graphe a etudier
        self.parent = list(range(1,n+1))
        self.rang = [0] * n


    def find(self, x):  #nous renvoie le représentant de l'élément x
        if self.parent[x-1] == x:  #x-1 car notre premier sommet est 1 et non 0
            return x 
        else:
            return self.find(self.parent[x-1])


    def union(self, x, y): #fusionne les branches du représentant de x et du représentant de y 
        representant_x = self.find(x)
        representant_y = self.find(y)
        if representant_x != representant_y:  #il va fusionner les "familles" des représentants à celui qui a le moins de "descendants"
            if self.rang[representant_x-1] < self.rang[representant_y-1]:
                self.parent[representant_x-1] = representant_y
            elif self.rang[representant_x-1] > self.rang[representant_y-1]:
                self.parent[representant_y-1] = representant_x
            else:
                self.parent[representant_y-1] = representant_x
                self.rang[representant_x-1] += 1

def unionfinds(chemin,classe):
    return [classe.finds(i) for i in chemin]  #nous renvoie la liste des parents 

def kruskal(g):

    "renvoie un graph dont il ne reste que les arretes qui ne font pas de cycle et dont es arretes sont de poids minimal"

    sommets=list(g.graph.keys()) # on récupere tous les sommets

    new_sommets = []

    uf = UnionFind(len(sommets)) 

    # On récupere les chemins et les puissances dans deux listes


    chemin=[]#tous les chemins possibles (57), (12),...
    power=[]
    sauv=[]



    for i in sommets: # on creer tous les sommets
    

        for voisin in g.graph[i]:
            if voisin[0] not in sauv:
                int=[]
                int.append(i)
                int.append(voisin[0])
                chemin.append(int)
                power.append(voisin[1])

        sauv.append(i)

    G = Graph(range(1, len(sommets)+1))


    # On prend le plus petit poids et on creer un graph avec cette arrête

    while chemin!= []: #tant qu'on a pas regardé tout les chemins

        #On prend la liaison de plus petit poids

        ind_mn=indice_min(power)

        plus_ptt_poids=chemin[ind_mn]


        '''union finds :

         1- on trouve la prochaine arrête de plus petite puissance
         2- on regarde si le parent des deux sommets de cette arrête est le même :
         si oui, on ne la prends pas
         si non, on la prends et on lui change le parent afin que ce soit le même
         PROBLEME : changer tous les parents précédents, résolu par union by rank  '''

        i = sommets.index(plus_ptt_poids[0])
        j = sommets.index(plus_ptt_poids[1])


        if uf.find(plus_ptt_poids[0]) != uf.find(plus_ptt_poids[1]): #si le parent du i eme sommet different du parent du j ieme sommet

         
            uf.union(plus_ptt_poids[0], plus_ptt_poids[1]) #les parents des i et j sommets deviennent tout deux egaux au parent du j ieme sommet
            G.add_edge(plus_ptt_poids[0], plus_ptt_poids[1], power[ind_mn])


        chemin.pop(ind_mn) #on enlève dans tous les cas de la liste de chemin puisqu'on ne pourra pas la prendre
        power.pop(ind_mn)

        new_sommets.append(plus_ptt_poids[0])
        new_sommets.append(plus_ptt_poids[1])        

        new_sommets=list(set(new_sommets))
        new_sommets=sorted(new_sommets)

    return G

#------------------------------------------NEW KRUSKAL--------------------------------------

def initial_node(initial,node):
    """
    Fonction de initial un dictionnaire, et de node un noeud donc un entier.
    Trouve le noeud initial d'un noeud (c'est à dire le noeud à partir duquel a été créé la composante connexe)
    Il permettra d'indicer cette composante.
    """
    if initial[node] != node:
        initial[node] = initial_node(initial,initial[node])
    return initial[node]
    
def union(initial,rank,node1,node2):
    """
    Unit node 1 à node 2 en faisant devenir leur noeud initial clef/valeur l'un de l'autre dans initial.
    En d'autres termes, dans kruskal lorsqu'on tombe sur une arrête qui relie deux arbres,
    union les relie et actualise leurs rangs et noeud initiaux.
    On actualise le rang pour avoir le même noeud initial quelque soit le noeud de l'arbre 
    (on lie les arbres en prenant tjrs le même noeud initial ; celui de rang le plus élevé)
    Actualise également le rang.
    """
    i1 = initial_node(initial,node1)
    i2 = initial_node(initial,node2)
    if i1 == i2: 
        return None
    if rank[i2] < rank[i1]:
        initial[i2] = i1
    else:
        initial[i1]=i2
        if rank[i1] == rank[i2]:
            rank[i2] += 1
    return None

def new_kruskal(g):
    """ 
    On remarque qu'avec ce fonctionnement, on s'autorise à avoir des graphes non connexes.
    Néanmoins, on ne prendra pas en compte les points isolés. Nous n'essaierons pas de les 
    inclure dans notre nouveau graphe car on s'intéresse aux trajets ; nous n'en avons que
    faire des points isolés !
    """
    g_mst = Graph(nodes = g.nodes)
    edges = []
    initial = {}  # Noeud précédent. Permettra de remonter au noeud initial de chaque composante connexe avec initial_node
                        # Le noeud initial permet d'indicer la composante connexe.
    rank = {}           # Le rang nous permettra de lier des gros arbres avec des petits
        
    # Chaque noeud a comme noeud initial lui même, et comme rang 0
    t0 = time.perf_counter()
    for node in g.nodes:
        if g.graph[node] != []:
            initial[node] = node
            rank[node] = 0
    for node in g.graph:
        for edge in g.graph[node]:
            edges.append((node,edge[0],edge[1])) # edges devient la liste des arrêtes notées (node1, node2, power)
    t1 = time.perf_counter()
    print("parcourt du graphe : ", t1-t0)
    edges.sort(key = lambda x : x[2]) # Permet de trier la liste par rapport à la troisième valeur des sous liste de la liste edge
    t2 = time.perf_counter()
    for edge in edges:
        if initial_node(initial,edge[0]) != initial_node(initial,edge[1]):
        # Si les bouts d'une arrête nne sont pas déjà dans la même composante connexe, alors on les unit.
            g_mst.add_edge(edge[0],edge[1],edge[2])
            union(initial,rank,edge[0],edge[1])
    t3 = time.perf_counter()
    print("parcourt des arrêtes : ", t3-t2)
    t4 = time.perf_counter()
    previous = g_mst.dfs(1) 
    # on se dit que le noeud générateur du graph a plus de chances d'être au milieu du graphe car il appartient à l'arbre 
    # auquel on a fixé d'autres arbres.
    t5 = time.perf_counter()
    print("get_previous prend : ", t5 - t4)
  
    return g_mst, previous

## COMPLEXITE : notons n le nombre de sommets
## - la boucle for nous permettant de calculer tous les somments a une complexité en O(n²)
## - la boucle while faisant appel a la classe union_finds a alors une complexité a son tour en O(n)
## - On construit p arrêtes pour notre nouveau graphe
## - La complexité finale est en O(p*n²)

def truck_to_dico(truck): 
    '''
    Prend en entrée un fichier de camions 
    Retourne un dico de camions comme ca truck=[[puissance, prix, rapport prix puissance ]]
    '''
    dico_trucks={}
    fichier = open("input/" + f"{truck}", "r")
    nb_camion=int(fichier.readline())
    for i in range(1,nb_camion+1):
        line=fichier.readline()
        ligne_split=line.split(" ")
        power=int(ligne_split[0])
        prix=int(ligne_split[1])
        dico_trucks[i]=(power, prix)
    return dico_trucks

def routes_to_dico(filename_in, filename_out): 
    '''
    Entrée: un fichier routes.in
    Return: un dico de liste comme ca: routes = [[dep, dest, powermin, profit], [powermin, profit]]
    '''

    dico_chemins={}
    nom= filename_in.split(".")
    fichier_in = open("input/" + f"{filename_in}", "r")
    fichier_out = open("input/" + f"{filename_out}", "r") 
    nb_trajet=int(fichier_in.readline())
    print(nb_trajet)
    nb_trajet_out=int(fichier_out.readline())
    routes=[]
    for i in range(1,nb_trajet+1):
        line_in=fichier_in.readline()
        line_out=fichier_out.readline()

        ligne_in_split=line_in.split(" ")
        ligne_out_split=line_out.split(" ")

        profit=int(ligne_in_split[2])
        power_min=int(ligne_out_split[2])
        dep=int(ligne_in_split[0])
        dest=int(ligne_in_split[1])
        dico_chemins[f"{dep}"+"-"+f"{dest}"]=(power_min, profit)
    return dico_chemins


def selection_camion(filename_trucks, budget, filename_in, filename_out):
    # CODE GLOUTON
    '''
    prend en entrée le fichier trucks de tous les camions disponibles, 
    le budget budget de la compagnie de transport 
    et le fichier routes de tous les trajets disponibles avec leur puissance requise (routeout) et leur profit (routin). 
    
    renvoie la liste des camions sélectionnés avec leur affectation à un trajet ainsi que le profit total obtenu.
    '''
    #

    # On change nos fichiers en listes et on rajoute (par le biais de la fonction) le rapport pri puissance dans la liste
    trucks=truck_to_dico(filename_trucks)
    print("trucks=", trucks)
    routes=routes_to_dico(filename_in, filename_out)
    print("routes=", routes)

    # Pour chaque trajet, on creer une liste de tous 
    camion_selected=[]
    for trajet in routes.keys():
        for camion in trucks.keys():
            power=trucks[camion][0]
            print("power=", power)
            prix=trucks[camion][1]
            print("prix=", prix)
            puissance_requise=routes[trajet][0]
            print("puissance_requise=", puissance_requise)
            profit=routes[trajet][1]
            print("profit=", profit)
            if power >= puissance_requise:
                camion_selected.append([trajet, camion, prix/profit, prix])
            print(camion_selected)

        
    # On trie les camions par ordre décroissant de leur ratio prix-puissance
    camion_trie = sorted(camion_selected, key=lambda camion_selected: camion_selected[2], reverse=True)
    print("camion_trie=", camion_trie)
    
    derniere_selection = []
    trajets_deja_faits=[]
    total_profit = 0
    
    for traj_cam in camion_trie:
        print("traj_cam=", traj_cam)
        # On séléctionne les camions en commençant par le camion avec le ratio coût-puissance le plus élevé jusqu'à ce que le budget soit atteint
        if traj_cam[3] <= budget and traj_cam[0] not in trajets_deja_faits:
            derniere_selection.append(traj_cam)
            trajets_deja_faits.append(traj_cam[0])
            budget -= traj_cam[3]
    
    return derniere_selection













