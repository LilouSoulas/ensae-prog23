import sys 
sys.path.append("delivery_network/")

# le test ne marche pas 

import unittest 
from graph import UnionFind

class Test_UnionFinds(unittest.TestCase):
    def test_0(self):
        uf = UnionFind(6)
        uf.union(1,2)
        uf.union(2,3)
        self.assertEqual(uf.find(1),1)
        self.assertEqual(uf.find(2),1)

    def test_1(self):
        uf = UnionFind(10)
        uf.union(5,8)
        uf.union(2,7)
        uf.union(1,10)
        uf.union(5,3)
        uf.union(9,10)
        uf.union(5,9)
        self.assertEqual(uf.find(1),5)
        self.assertEqual(uf.find(5),5)



if __name__ == '__main__':
    unittest.main()
