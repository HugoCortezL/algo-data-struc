import pytest
from Algorithms.Arrays import selection_sort

class TestBinarySearch():

    def test_sort_empty_list(self):
        data = []
        result = selection_sort(data)
        assert result == []
    
    def test_sort_sorted_list(self):
        data = [1, 2, 3, 4, 5]
        result = selection_sort(data)
        assert result == [1, 2, 3, 4, 5]

    def test_sort_reverse_sorted_list(self):
        data = [5, 4, 3, 2, 1]
        result = selection_sort(data)
        assert result == [1, 2, 3, 4, 5]

    def test_sort_random_list(self):
        data = [3, 1, 4, 5, 2]
        result = selection_sort(data)
        assert result == [1, 2, 3, 4, 5]

    def test_sort_duplicate_values(self):
        data = [4, 2, 4, 1, 2, 3]
        result = selection_sort(data)
        assert result == [1, 2, 2, 3, 4, 4]

