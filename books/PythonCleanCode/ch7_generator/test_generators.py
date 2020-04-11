"""Clean Code in Python - Chapter 07: Using generators

> Test for: generators_1.py
"""
from unittest import TestCase, main

from generators_1 import PurchasesStats
from generators_2 import process_purchases


class TestPurchaseStats(TestCase):
    def test_calculations(self):
        stats = PurchasesStats(range(1, 11 + 1)).process()

        self.assertEqual(stats.min_price, 1)
        self.assertEqual(stats.max_price, 11)
        self.assertEqual(stats.avg_price, 6)

    def test_emtpy(self):
        self.assertRaises(ValueError, PurchasesStats, [])


class TestProcessPurchases(TestCase):
    def test_calculations(self):
        min_, max_, avg = process_purchases(range(1, 11 + 1))

        self.assertEqual(min_, 1)
        self.assertEqual(max_, 11)
        self.assertEqual(avg, 6)

    def test_empty(self):
        self.assertRaises(ValueError, process_purchases, [])


if __name__ == "__main__":
    main()
