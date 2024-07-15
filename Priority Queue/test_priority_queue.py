from priority_queue import PriorityQueue
import pytest


def test_priority_queue_insert():
    pq = PriorityQueue()
    pq.insert(10)
    assert pq.peek() == 10
    assert pq.isEmpty() == False


def test_priority_queue_heapify_up():
    pq = PriorityQueue()
    pq.insert(5)
    pq.insert(10)
    pq.insert(20)
    pq.insert(15)
    assert pq.print_queue() == [20, 15, 10, 5]


def test_priority_queue_is_empty():
    pq = PriorityQueue()
    assert pq.isEmpty() == True
    pq.insert(1)
    assert pq.isEmpty() == False


def test_priority_queue_print_queue():
    pq = PriorityQueue()
    pq.insert(10)
    pq.insert(20)
    pq.insert(5)
    assert pq.print_queue() == [20, 10, 5]
    pq.insert(15)
    assert pq.print_queue() == [20, 15, 5, 10]


def test_heapifydown():
    pq = PriorityQueue(is_min_heap=False)
    pq.queue = [3, 1, 2]
    pq.heapifyDown(0)
    assert pq.queue == [3, 1, 2]
