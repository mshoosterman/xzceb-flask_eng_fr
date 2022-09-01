from translator import englishToFrench, frenchToEnglish
import unittest


class Test_frenchToEnglish(unittest.TestCase):
    def test_singleword(self):
        self.assertEqual(frenchToEnglish('Bonjour'),'Hello')

    def test_null(self):
        self.assertNotEqual(frenchToEnglish('None'),'')


class Test_englishToFrench(unittest.TestCase):
    def test_singleword(self):
        self.assertEqual(englishToFrench('Hello'), 'Bonjour')

    def test_null(self):
        self.assertNotEqual(englishToFrench('None'),'')

unittest.main()