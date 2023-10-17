import pytest
from Exceptions import EmptyQueueException
from DataStructure import Queue

class TestQueue:
    
    def test_is_empty(self):
        queue = Queue()
        assert queue.is_empty() is True
        assert queue.size() == 0
    
    def test_add(self):
        queue = Queue()
        for item in [1, 2, 3, 4, 5]:
            queue.add(item)
        assert queue.is_empty() is False
        assert queue.size() == 5
    
    def test_peek(self):
        queue = Queue()
        with pytest.raises(EmptyQueueException):
            queue.peek()
        for item in [1, 2, 3, 4, 5]:
            queue.add(item)
        assert queue.peek() == 1
    
    def test_poll(self):
        queue = Queue()
        for item in [1, 2, 3, 4, 5]:
            queue.add(item)
        assert queue.poll() == 1
        assert queue.poll() == 2
        assert queue.is_empty() is False
        assert queue.size() == 3

        assert queue.poll() == 3
        assert queue.poll() == 4
        assert queue.poll() == 5
        assert queue.is_empty() is True
        assert queue.size() == 0



