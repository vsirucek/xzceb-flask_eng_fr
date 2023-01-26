import unittest

from translator import frenchToEnglish, englishToFrench

class TestTranslator(unittest TestCase):
        def test_fr2en(self):
            self assertEqual(frenchToEnglish(''),'')
            self assertEqual(frenchToEnglish('Bonjour'),'Hello')

        def test_en2fr(self):
            self assertEqual(englishToFrench(''), '')
            self assertEqual(englishToFrench('Hello'), 'Bonjour')
