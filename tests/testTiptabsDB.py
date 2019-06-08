# import unittest
# from Tiptabs.TiptabsDB import *

# class testTiptabsDB(unittest.TestCase):

#     #TODO: Add setup for DB for further testing of storage / input.
    
#     def testCheckInputs(self):
#         input = ['users', 'Gary', 'Gary', 'JPYtoUSD']
#         expected = [True, "Valid input entered."]
#         result = TiptabsDB.check_inputs(self, input)
#         return self.assertEqual(expected, result)

#     def testCheckInputs_InvalidInputSize(self):
#         invalid_size_input = ['users', 'Alex', 'Alex']
#         expected = [False, "Invalid number of entry items entered."]
#         result = TiptabsDB.check_inputs(self, invalid_size_input)
#         return self.assertEqual(expected, result)

#     def testCheckInputs_NoneInput(self):
#         none_input = None
#         expected = [False, "ERROR: None entries are not allowed to be stored into the Tiptabs database."]
#         result = TiptabsDB.check_inputs(self, none_input)
#         return self.assertEqual(expected, result)

#     def testCheckInputs_NoneArrayEntries(self):
#         null_array_entries = [None, None, None, None]
#         expected = [False, 'Invalid item was attempted to be added.']
#         result = TiptabsDB.check_inputs(self, null_array_entries)
#         return self.assertEqual(expected, result)
        
#     def testCheckInputs_NoneEntry(self):
#         none_entry = ['users', 'Barry', 'Barry', None]
#         expected = [False, "Invalid item was attempted to be added."]
#         result = TiptabsDB.check_inputs(self, none_entry)
#         return self.assertEqual(expected, result)

#     def testCheckInputs_EmptyStrings(self):
#         empty_string_input = ["", "", "", ""]
#         expected = [False, "Invalid item was attempted to be added."]
#         result = TiptabsDB.check_inputs(self, empty_string_input)
#         return self.assertEqual(expected, result)

# if __name__ == '__main__':
#     unittest.main()
