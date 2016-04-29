import unittest
from numpy import poly1d

class testNumpy(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass
    
    def testBasic(self):
        self.assertFalse(poly1d([1,1]) == poly1d([1]))
        
        


if __name__ == '__main__':
    unittest.main()




