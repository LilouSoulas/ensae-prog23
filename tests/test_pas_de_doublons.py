import sys 
sys.path.append("delivery_network/")

import unittest
from graph import pas_de_doublons


class Test_PasDeDoublons(unittest.TestCase):
    def test_0(self):
        l1, l2 = [1, 2, 3, 4, 5], [4, 5, 6, 7, 8]
        self.assertEqual(pas_de_doublons(l1,l2),[1, 2, 3, 4, 5, 6, 7, 8])

    def test_1(self):
        l1, l2 = [5, 8, 2, 9, 0] , [1, 3, 4, 6, 7]
        self.assertEqual(pas_de_doublons(l1,l2), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

if __name__ == '__main__':
    unittest.main()