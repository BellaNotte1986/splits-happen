import unittest
from unittest.mock import patch
from bowling import ScoreCalc

class TestBowling(unittest.TestCase):

    strikes = 'XXXXXXXXXXXX'
    @patch('builtins.input', return_value=strikes)
    def test_strikes(self, strikes):
        result = ScoreCalc(self.strikes)
        self.assertTrue(result == 300)

    misses = '9-9-9-9-9-9-9-9-9-9-'
    @patch('builtins.input', return_value=misses)
    def test_misses(self, misses):
        result = ScoreCalc(self.misses)
        self.assertTrue(result == 90)

    spares = '5/5/5/5/5/5/5/5/5/5/5'
    @patch('builtins.input', return_value=spares)
    def test_spares(self, spares):
        result = ScoreCalc(self.spares)
        self.assertTrue(result == 150)

    varied = 'X7/9-X-88/-6XXX81'
    @patch('builtins.input', return_value=varied)
    def test_varied(self, varied):
        result = ScoreCalc(self.varied)
        self.assertTrue(result == 167)
