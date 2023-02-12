import unittest
from utils import arrs


class TestArrs(unittest.TestCase):

    def test_get(self):
        self.assertEqual(arrs.get([1, 2, 3], 1, "test"), 3)
        self.assertEqual(arrs.get([], 0, "test"), "test")

    def test_slice(self):
        assert arrs.my_slice([1, 2, 3, 4], 1, 3) == [2, 3]
        assert arrs.my_slice([1, 2, 3], 1) == [2, 3]
        assert arrs.my_slice([1, 2, 3, 4], -1) == [4]
        assert arrs.my_slice([1, 2, 3, 4], 5) == []
        assert arrs.my_slice([]) == []
        assert arrs.my_slice([1, 2, 3]) == [1, 2, 3]
        assert arrs.my_slice([1, 2, 3, 4], end=0) == []
