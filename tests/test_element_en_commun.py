import sys 
sys.path.append("delivery_network/")

import unittest
from graph import Graph, element_en_commun


class Test_ElementCommun(unittest.TestCase):
    def test_0(self):
        l1, l2 = [1, 2, 3, 4, 5], [6, 7, 8, 9, 10]
        self.assertEqual(element_en_commun(l1,l2),0)

    def test_1(self):
        l1, l2 = [0,1,2],[2,3,4] 
        self.assertEqual(element_en_commun(l1,l2),1)

if __name__ == '__main__':
    unittest.main()
