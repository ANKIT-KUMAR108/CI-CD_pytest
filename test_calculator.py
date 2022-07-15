import unittest
from calculator import *

class TestCalculatorMethods(unittest.TestCase):
    def test_add(self): # naming convention of function "test_something"is mandatory
        # DOUBT: IS WRITING ADD AFTER "test_" is also mandatory? 

        # test addition of two numbers
        self.assertEqual(sum(101,18),119)
        self.assertEqual(sum(500,20),520)
        self.assertEqual(sum(-90,-18),-108)
        self.assertEqual(sum(0,0),0)
        self.assertEqual(sum(98,-18),80)
        self.assertEqual(sum(-1,-1),-2)
        self.assertAlmostEqual(sum(3.2,2.1),5.3)
    
    def test_values(self):
        self.assertRaises(ValueError,sum,"ankit",1)
        self.assertRaises(ValueError,sum,"ankit","kumar")
        self.assertRaises(ValueError,sum,1,"ankit") #arguments are (ValueError,function_name,argunments of function )

        # can also do the above exception handling like:
        with self.assertRaises(ValueError):
            divide(10,0)

if __name__ == '__main__':
    unittest.main()

    



