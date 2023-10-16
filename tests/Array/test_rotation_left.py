import pytest
from Algorithms.Arrays import rotation_left

class TestRotationLeftArray():

    def test_rotation_left_empty_list(self):
        data = []
        result = rotation_left(data, 3)
        assert result == []
    
    def test_rotation_left_zero(self):
        data = [1, 2, 3, 4, 5]
        result = rotation_left(data, 0)
        assert result == [1, 2, 3, 4, 5]
    
    def test_rotation_left_length(self):
        data = [1, 2, 3, 4, 5]
        result = rotation_left(data, 5)
        assert result == [1, 2, 3, 4, 5]
    
    def test_rotation_left_middle(self):
        data = [1, 2, 3, 4, 5]
        result = rotation_left(data, 3)
        assert result == [4, 5, 1, 2, 3]
    
    def test_rotation_left_more_length(self):
        data = [1, 2, 3, 4, 5]
        result = rotation_left(data, 24)
        assert result == [5, 1, 2, 3, 4]

    def test_rotation_left_duplicate_values(self):
        data = [4, 2, 4, 1, 2, 3]
        result = rotation_left(data, 2)
        assert result == [4, 1, 2, 3, 4, 2]
    
    def test_rotation_left_same_values(self):
        data = [1, 1, 1, 1, 1, 1]
        result = rotation_left(data, 6)
        assert result == [1, 1, 1, 1, 1, 1]

