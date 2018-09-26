import unittest
from TiptabsDB import *

class testTiptabsDB(unittest.TestCase):

    def testCheckInputs(self):
        input = ['users', 'Gary', 'Gary', 'JPYtoUSD']
        expected = [True, "Valid input entered."]
        db = TiptabsDB()
        result = db.check_inputs(input)
        return self.assertEqual(expected, result)
        
