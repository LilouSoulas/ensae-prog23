import sys 
sys.path.append("delivery_network/")

import unittest
from graph import indice_min


class Test_IndiceMin(unittest.TestCase):
    def test_0(self):
        l1 = [1, 2, 3, 4, 5]
        self.assertEqual(indice_min(l1),0)

    def test_1(self):
        l1 = [5, 8, 2, 9, 0] 
        self.assertEqual(indice_min(l1),4)

if __name__ == '__main__':
    unittest.main()
