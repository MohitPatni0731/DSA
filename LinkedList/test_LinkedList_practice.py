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
    linked_list = LinkedList()
    data1 = 10
    linked_list.insert(data1)
    assert linked_list.head.data == data1

    data2 = "Mohit"
    linked_list.insert(data2)
    assert linked_list.head.data == data2

