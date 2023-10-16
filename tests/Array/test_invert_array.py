import pytest
from Algorithms.Arrays import invert_array

class TestInvertArray():

    def test_invert_empty_list(self):
        data = []
        result = invert_array(data)
        assert result == []
    
    def test_invert_sorted_list(self):
        data = [1, 2, 3, 4, 5]
        result = invert_array(data)
        assert result == [5, 4, 3, 2, 1]

    def test_invert_random_list(self):
        data = [3, 1, 4, 5, 2]
        result = invert_array(data)
        assert result == [2, 5, 4, 1, 3]

    def test_invert_duplicate_values(self):
        data = [4, 2, 4, 1, 2, 3]
        result = invert_array(data)
        assert result == [3, 2, 1, 4, 2, 4]
    
    def test_invert_same_values(self):
        data = [1, 1, 1, 1, 1, 1]
        result = invert_array(data)
        assert result == [1, 1, 1, 1, 1, 1]

