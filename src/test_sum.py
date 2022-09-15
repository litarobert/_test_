import pytest
from sum import sum

class TestClass:
    def test_one(self):
        assert sum(10, 20) == 30
        assert sum(90, 10) == 100

    def test_two(self):
        assert sum(10, 2) == 12
        assert sum(-5, -9) == -14
        assert sum(10000, 45) == 10045
        assert sum(33, 70) == 103