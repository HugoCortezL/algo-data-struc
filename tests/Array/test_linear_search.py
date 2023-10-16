import pytest
from Algorithms.Arrays import linear_search

class TestLinearSearch():

    @pytest.fixture
    def setup_data(self):
        data = [1, 4, 2, 7, 5, 9]
        return data
    
    def test_search_target_not_in_array(self, setup_data):
        data = setup_data
        result = linear_search(data, 3)
        assert result == -1
    
    def test_search_found_at_end(self, setup_data):
        data = setup_data
        result = linear_search(data, 9)
        assert result == 5

    def test_search_found_at_beginning(self, setup_data):
        data = setup_data
        result = linear_search(data, 1)
        assert result == 0

    def test_search_found_in_middle(self, setup_data):
        data = setup_data
        result = linear_search(data, 7)
        assert result == 3
    
    def test_search_empty_array(self):
        result = linear_search([], 1)
        assert result == -1
    
    def test_search_target_at_multiple_positions(self):
        data = [1, 2, 3, 2, 4, 5, 2]
        result = linear_search(data, 2)
        assert result == 1