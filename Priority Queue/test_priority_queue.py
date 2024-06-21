from priority_queue import PriorityQueue
import pytest


def test_insert():
    PQ = PriorityQueue()
    PQ.insert(2)
    PQ.insert(4)
    assert PQ.queue == [2, 4]


def test_empty_queue():
    PQ = PriorityQueue()
    assert PQ.queue == []


def test_pop():  ###
    PQ = PriorityQueue()
    PQ.insert(2)
    PQ.insert(4)
    PQ.insert(3)
    assert PQ.pop() == 2
    assert PQ.queue == [3, 4]


def test_peek():
    PQ = PriorityQueue()
    PQ.insert(1)
    PQ.insert(2)
    assert PQ.peek() == 1
