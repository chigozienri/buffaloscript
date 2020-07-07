import unittest

from buffaloparse import parses

class TestParses(unittest.TestCase):
    def test_good(self):
        # Given
        good_sentences = [
            "buffalo",
            "buffalo buffalo",
            "buffalo buffalo buffalo",
            "buffalo buffalo buffalo buffalo",
            "Buffalo buffalo buffalo",
            "Buffalo buffalo buffalo Buffalo buffalo",
            "Buffalo buffalo Buffalo buffalo buffalo buffalo Buffalo buffalo",
            "Buffalo buffalo Buffalo buffalo Buffalo buffalo buffalo buffalo buffalo",
            "Buffalo buffalo Buffalo buffalo buffalo buffalo Buffalo buffalo"]
        # When / Then
        for sentence in good_sentences:
            self.assertEqual(parses(sentence), True)
    
    def test_bad(self):
        # Given
        bad_sentences = [
            "Buffalo",
            "Buffalo buffalo",
            "buffalo Buffalo",
            "Buffalo Buffalo buffalo",
            "Buffalo buffalo Buffalo buffalo buffalo"]

        # When / Then
        for sentence in bad_sentences:
            self.assertEqual(parses(sentence), False)
