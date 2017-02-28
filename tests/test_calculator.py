# -*- coding: utf-8 -*-
import unittest

from src.calculator import Calculator


class CalculatorTest(unittest.TestCase):
    """unitetestモジュールの簡単な実行例その1。"""
    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        self._calculator = Calculator()

    def tearDown(self):
        pass

    def test_add(self):
        self.assertEqual(self._calculator.add(1.5, 1.5), 3)

    def test_subtract(self):
        self.assertEqual(self._calculator.subtract(1.5, 1), 0.5)

    def test_multiply(self):
        self.assertEqual(self._calculator.multiply(1.5, 1.5), 2.25)

    def test_divide(self):
        self.assertEqual(self._calculator.divide(1.5, 0.3), 5)
