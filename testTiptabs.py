import unittest

from DictionaryBuilder import *
from Tiptabs import *


class testTiptabs(unittest.TestCase):

    app_dict = DictionaryBuilder()
    app = Tiptabs("EUR", app_dict)

    # TODO: Test class constructor with empty string, null values, etc

    def test_get_base(self):
        expected = "EUR"
        result = self.app.get_base()
        return self.assertEqual(expected, result)