import unittest

from src.calculator import sum, sub, mul, div

class CalculatorTest(unittest.TestCase):
    def test_sum(self):
        assert sum(1, 1) == 2

    def test_sub(self):
        assert sub(1, 1) == 0

    def test_mul(self):
        assert mul(1, 1) == 1

    def test_div(self):
        assert div(1, 1) == 1