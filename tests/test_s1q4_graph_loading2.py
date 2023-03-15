# À compléter

import sys 
sys.path.append("delivery_network/")

import unittest 
from graph import Graph, graph_from_file

class Test_GraphLoading(unittest.TestCase):
    def test_network0(self):
        g = graph_from_file("input/network.00.in")
        self.assertEqual(g.nb_nodes, 10)
        self.assertEqual(g.nb_edges, 9)
        self.assertEqual(g.graph[3][1][2],1)  #on teste que cela nous renvoie bien 1 comme distance

    def test_network1(self):
        g = graph_from_file("input/network.01.in")  #aucune distance n'est donnée dans ce fichier, d'où le test
        self.assertEqual(g.nb_nodes, 7)
        self.assertEqual(g.nb_edges, 5)
        self.assertEqual(g.graph[5][0][2],1)  #la fonction graph_from_file a été modifiée afin de faire apparaître la distance par défaut
    
    def test_network4(self):
        g = graph_from_file("input/network.04.in")
        self.assertEqual(g.nb_nodes, 10)
        self.assertEqual(g.nb_edges, 4)
        self.assertEqual(g.graph[1][0][2], 6)

if __name__ == '__main__':
    unittest.main()


