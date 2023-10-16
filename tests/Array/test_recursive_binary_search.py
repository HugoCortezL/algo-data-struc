import pytest
from Algorithms.Arrays import recursive_binary_search

class TestBinarySearch():

    @pytest.fixture
    def setup_data(self):
        data = [1, 4, 6, 8, 10, 15, 20, 24, 36, 47, 60]
        return data
    
    def test_search_target_not_in_array_recursive(self, setup_data):
        data = setup_data
        result = recursive_binary_search(data, 3)
        assert result == -1
    
    def test_search_found_at_end_recursive(self, setup_data):
        data = setup_data
        result = recursive_binary_search(data, 60)
        assert result == 10

    def test_search_found_at_beginning_recursive(self, setup_data):
        data = setup_data
        result = recursive_binary_search(data, 1)
        assert result == 0

    def test_search_found_in_middle_recursive(self, setup_data):
        data = setup_data
        result = recursive_binary_search(data, 15)
        assert result == 5
    
    def test_search_empty_array_recursive(self):
        result = recursive_binary_search([], 1)
        assert result == -1
    
    def test_search_unsorted_array_recursive(self):
        unsorted_array = [5, 1, 4, 2, 3]
        with pytest.raises(ValueError, match="The array must be sorted."):
            recursive_binary_search(unsorted_array, 3)