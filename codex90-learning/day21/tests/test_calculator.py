import unittest

from tools.calculator import predict_money


class TestPredictMoney(unittest.TestCase):

    def test_normal_calculation(self):
        result = predict_money(10000, 5000)
        self.assertEqual(result, 610000)

    def test_zero_income(self):
        result = predict_money(10000, 0)
        self.assertEqual(result, 10000)

    def test_zero_money(self):
        result = predict_money(0, 1000)
        self.assertEqual(result, 120000)

    def test_all_values_are_zero(self):
        result = predict_money(0, 0)
        self.assertEqual(result, 0)

if __name__ == "__main__":
    unittest.main()