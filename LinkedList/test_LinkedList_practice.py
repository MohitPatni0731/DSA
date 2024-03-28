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

def test_printing():
    linked_list = LinkedList()
    linked_list.insert(1)
    linked_list.insert(2)
    linked_list.insert(3)
    assert str(linked_list) == "3 --> 2 --> 1 --> None"

    empty_llist = LinkedList()
    assert str(empty_llist) == "None"

    one_node_llist = LinkedList()
    one_node_llist.insert(1)
    assert str(one_node_llist) == "1 --> None"

def test_delete_first_element():
    llist = LinkedList()
    llist.insert(1)
    llist.insert(2)
    llist.insert(3)
    llist.insert(4)

    llist.delete(1)
    assert str(llist) == "4 --> 3 --> 2 --> None"

def test_last_element():
    llist = LinkedList()
    llist.insert(10)
    llist.insert(20)
    llist.insert(30)
    llist.insert(40)
    llist.delete(40)
    assert str(llist) == "30 --> 20 --> 10 --> None"

def test_non_existing_element():
    llist = LinkedList()
    assert llist.delete(2) == None

def test_delete_more_than_one_occurance_element():
    llist = LinkedList()
    llist.insert(1)
    llist.insert(2)
    llist.insert(3)
    llist.insert(2)
    llist.delete(2)
    assert str(llist) == "3 --> 2 --> 1 --> None"
    
def test_searching():
    llist = LinkedList()
    llist.insert(10)
    llist.insert(20)
    llist.insert(30)
    llist.insert(40)

    result = llist.search(20)
    assert result

def test_search_nonexisting_element():
    llist = LinkedList()
    llist.insert(10)
    llist.insert(20)
    llist.insert(30)
    llist.insert(40)
    assert llist.search(50) == None

def test_search_duplicate_element():
    llist = LinkedList()
    llist.insert(10)
    llist.insert(20)
    llist.insert(30)
    llist.insert(30)
    assert llist.search(30) is not None

def test_empty():
    linked_list = LinkedList()
    assert linked_list.is_empty() == True

def test_nonempty():
    llist = LinkedList()
    llist.insert(10)
    assert llist.is_empty() == False
def test_size():
    linked_list = LinkedList()
    linked_list.insert(1)
    linked_list.insert(2)
    linked_list.insert(3)
    assert linked_list.size() == 3

def test_zero_sized():
    llist = LinkedList()
    assert llist.size() == 0