#test unitaire kruskal

import sys 
sys.path.append("delivery_network/")

import unittest 
from graph import Graph, kruskal, UnionFind, graph_from_file

class Test_kruskal(unittest.TestCase):
    def test_network2(self):
        g = graph_from_file("input/network.02.in")
        d = kruskal(g)
        self.assertEqual(d.graph[1][0][0], 4)
        self.assertEqual(d.graph[3][1][0], 2)
        self.assertEqual(d.graph[4][0][0], 3)

    def test_network3(self):
        g = graph_from_file("input/network.03.in")
        d = kruskal(g)
        self.assertEqual(d.graph[1][0][0], 2)
        self.assertEqual(d.graph[3][1][0], 2)
        self.assertEqual(d.graph[2][0][0], 3)

    
if __name__ == '__main__':
    unittest.main()



