import pytest
from Exceptions import EmptyStackException
from DataStructure import Stack

class TestStack:
    
    def test_is_empty(self):
        stack = Stack()
        assert stack.is_empty() is True
        assert stack.size() == 0
    
    def test_push(self):
        stack = Stack()
        for item in [1, 2, 3, 4, 5]:
            stack.push(item)
        assert stack.is_empty() is False
        assert stack.size() == 5
    
    def test_top(self):
        stack = Stack()
        with pytest.raises(EmptyStackException):
            stack.top()
        for item in [1, 2, 3, 4, 5]:
            stack.push(item)
        assert stack.top() == 5
        assert stack.size() == 5
    
    def test_poll(self):
        stack = Stack()
        with pytest.raises(EmptyStackException):
            stack.pop()
        for item in [1, 2, 3, 4, 5]:
            stack.push(item)
        assert stack.pop() == 5
        assert stack.pop() == 4
        assert stack.is_empty() is False
        assert stack.size() == 3

        assert stack.pop() == 3
        assert stack.pop() == 2
        assert stack.pop() == 1
        assert stack.is_empty() is True
        assert stack.size() == 0
        with pytest.raises(EmptyStackException):
            stack.pop()