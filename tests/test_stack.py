# -*- coding: utf-8 -*-
import unittest

from src.stack import Stack


class CalculatorTest(unittest.TestCase):
    """unitetestモジュールの簡単な実行例その2。"""
    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        self._stack = Stack()

    def tearDown(self):
        pass

    def test_is_empty(self):
        self.assertTrue(self._stack.is_empty())

        self._stack.push(1)
        self.assertFalse(self._stack.is_empty())

    def test_size(self):
        self.assertEqual(0, self._stack.size())

        self._stack.push(1)
        self.assertEqual(1, self._stack.size())

    def test_push(self):
        self._stack.push(1)
        self.assertEqual(1, self._stack.top())

    def test_pop(self):
        self._stack.push(1)
        self.assertEqual(1, self._stack.pop())
        self.assertEqual(0, self._stack.size())

        with self.assertRaises(IndexError):
            self._stack.pop()

    def test_top(self):
        self._stack.push(1)
        self.assertEqual(1, self._stack.top())
        self.assertEqual(1, self._stack.size())

        self._stack.pop()
        with self.assertRaises(IndexError):
            self._stack.top()
