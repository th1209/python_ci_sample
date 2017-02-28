# -*- coding: utf-8 -*-
class Stack:
    def __init__(self):
        self._stack = []

    def is_empty(self):
        return len(self._stack) <= 0

    def size(self):
        return len(self._stack)

    def push(self, value):
        self._stack.append(value)

    def pop(self):
        if self.is_empty():
            raise IndexError('')
        return self._stack.pop()

    def top(self):
        if self.is_empty():
            raise IndexError('')
        return self._stack[len(self._stack) - 1]
