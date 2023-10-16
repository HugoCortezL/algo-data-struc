import pytest
from Algorithms.Arrays import rotation_right

class TestRotationRightArray():

    def test_rotation_right_empty_list(self):
        data = []
        result = rotation_right(data, 3)
        assert result == []
    
    def test_rotation_right_zero(self):
        data = [1, 2, 3, 4, 5]
        result = rotation_right(data, 0)
        assert result == [1, 2, 3, 4, 5]
    
    def test_rotation_right_length(self):
        data = [1, 2, 3, 4, 5]
        result = rotation_right(data, 5)
        assert result == [1, 2, 3, 4, 5]
    
    def test_rotation_right_middle(self):
        data = [1, 2, 3, 4, 5]
        result = rotation_right(data, 3)
        assert result == [3, 4, 5, 1, 2]
    
    def test_rotation_right_more_length(self):
        data = [1, 2, 3, 4, 5]
        result = rotation_right(data, 24)
        assert result == [2, 3, 4, 5, 1]

    def test_rotation_right_duplicate_values(self):
        data = [4, 2, 4, 1, 2, 3]
        result = rotation_right(data, 2)
        assert result == [2, 3, 4, 2, 4, 1]
    
    def test_rotation_right_same_values(self):
        data = [1, 1, 1, 1, 1, 1]
        result = rotation_right(data, 6)
        assert result == [1, 1, 1, 1, 1, 1]

