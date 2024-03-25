import pytest
from LinkedList_practice import Node
from LinkedList_practice import LinkedList

def test_node_creation():
    data = 10
    node = Node(data)
    assert node.data == data

def test_node_next_element():
    node1 = Node(10)
    node2 = Node(20)
    node1.next = node2
    assert node1.next == node2

def test_inserted_element():
    data1 = 10
    node = Node(data1)
    assert node.data == data1
    data2 = "Mohit"
    node2 = Node(data2)
    assert node2.data == data2

def test_printing():
    linked_list = LinkedList()
    linked_list.append(1)
    linked_list.append(2)
    linked_list.append(3)
    assert linked_list == "1 --> 2 --> 3 --> None"
