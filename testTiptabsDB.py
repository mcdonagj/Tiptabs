import unittest
from TiptabsDB import *

class testTiptabsDB(unittest.TestCase):

    #TODO: Add setup for DB for further testing of storage / input.
    
    def testCheckInputs(self):
        input = ['users', 'Gary', 'Gary', 'JPYtoUSD']
        expected = [True, "Valid input entered."]
        result = TiptabsDB.check_inputs(self, input)
        return self.assertEqual(expected, result)

    def testCheckInputs_InvalidInputSize(self):
        invalid_size_input = ['users', 'Alex', 'Alex']
        expected = [False, "Invalid number of entry items entered."]
        result = TiptabsDB.check_inputs(self, invalid_size_input)
        return self.assertEqual(expected, result)

    def testCheckInputs_NoneInput(self):
        none_input = None
        expected = [False, "ERROR: None entries are not allowed to be stored into the Tiptabs database."]
        result = TiptabsDB.check_inputs(self, none_input)
        return self.assertEqual(expected, result)
        
