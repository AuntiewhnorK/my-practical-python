"""

Practical Python - Testing and Debugging

Faith Kpolie
6/27/2022

This module uses unittest to perform
unit tests on the Stock class.
"""

import unittest
import stock


class TestStock(unittest.TestCase):
    def test_create(self):
        # test creating a Stock instance
        s = stock.Stock("GOOG", 120, 50.0)
        self.assertEqual(s.name, "GOOG")
        self.assertEqual(s.shares, 120)
        self.assertEqual(s.price, 50.0)

    def test_correct_cost(self):
        # test returning the correct total cost (6000.0)
        s = stock.Stock("GOOG", 120, 50.0)
        self.assertEqual(s.cost, 6000.0)

    def test_sell(self):
        # tests s.sell() decreases s.shares correctly
        s = stock.Stock("GOOG", 120, 50.0)
        s.sell(20)
        self.assertEqual(s.shares, 100)

    def test_share_vartype(self):
        # tests that s.shares is an integer type
        s = stock.Stock("GOOG", 120, 50.0)
        with self.assertRaises(TypeError):
            s.shares = "100"
            s.shares = 100.0


if __name__ == "__main__":
    unittest.main()
