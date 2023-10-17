import pytest
from Exceptions import EmptyQueueException
from DataStructure import Queue

class TestQueue:
    
    def test_is_empty(self):
        queue = Queue()
        assert queue.is_empty() is True
        assert queue.size() == 0
    
    def test_enqueue(self):
        queue = Queue()
        for item in [1, 2, 3, 4, 5]:
            queue.enqueue(item)
        assert queue.is_empty() is False
        assert queue.size() == 5
    
    def test_front(self):
        queue = Queue()
        with pytest.raises(EmptyQueueException):
            queue.front()
        for item in [1, 2, 3, 4, 5]:
            queue.enqueue(item)
        assert queue.front() == 1
    
    def test_dequeue(self):
        queue = Queue()
        for item in [1, 2, 3, 4, 5]:
            queue.enqueue(item)
        assert queue.dequeue() == 1
        assert queue.dequeue() == 2
        assert queue.is_empty() is False
        assert queue.size() == 3

        assert queue.dequeue() == 3
        assert queue.dequeue() == 4
        assert queue.dequeue() == 5
        assert queue.is_empty() is True
        assert queue.size() == 0

        with pytest.raises(EmptyQueueException):
            queue.dequeue()



