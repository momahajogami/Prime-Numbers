from legendre import legendre

class testLegendre(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass
    
    def testBasic(self):
        self.assertEqual(legendre(2,15),1)
        
        


if __name__ == '__main__':
    unittest.main()




