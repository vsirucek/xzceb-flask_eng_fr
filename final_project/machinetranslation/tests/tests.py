"""
this is a module docstring
"""
import unittest
from translator import french_to_english, english_to_french

class TestTranslator(unittest.TestCase):
    def test_fr2en(self):
        self.assertEqual(french_to_english(''),'')
        self.assertEqual(french_to_english('Bonjour'),'Hello')
        self.assertNotEqual(french_to_english('Bonjour'),'Bonjour')

    def test_en2fr(self):
        self.assertEqual(english_to_french(''),'')
        self.assertEqual(english_to_french('Hello'), 'Bonjour')
        self.assertNotEqual(english_to_french('Hello'), 'Hello')

unittest.main()
       
