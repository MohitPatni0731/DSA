import pytest
from LinkedList_practice import Node
from LinkedList_practice import LinkedList

def ll(elements):
    linked_list = LinkedList()
    for element in elements:
        linked_list.insert(element)
    return linked_list

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
    llist1 = LinkedList()
    data1 = 10
    llist1.insert(data1)
    assert llist1.head.data == data1
    
    llist = LinkedList()
    data2 = "Mohit"
    llist.insert(data2)
    assert llist.head.data == data2

def test_printing():
    linked_list = ll([1, 2, 3, 4])
    assert str(linked_list) == "1 --> 2 --> 3 --> 4 --> None"

    empty_llist = LinkedList()
    assert str(empty_llist) == "None"

    one_node_llist = LinkedList()
    one_node_llist.insert(1)
    assert str(one_node_llist) == "1 --> None"

def test_delete_first_element():
    linked_list = ll([1, 2, 3, 4])
    linked_list.delete(1)
    assert str(linked_list) == "2 --> 3 --> 4 --> None"

def test_last_element():
    linked_list = ll([1, 2, 3, 4])
    linked_list.delete(4)
    assert str(linked_list) == "1 --> 2 --> 3 --> None"

def test_non_existing_element():
    linked_list = ll([1, 2, 3, 4])
    assert linked_list.delete(5) == None

def test_delete_more_than_one_occurance_element():
    linked_list = ll([1, 2, 3, 2, 4])
    linked_list.delete(2)
    assert str(linked_list) == "1 --> 3 --> 2 --> 4 --> None"
    
def test_searching():
    linked_list = ll([1, 2, 3, 4])
    result = linked_list.search(2)
    assert result

def test_search_nonexisting_element():
    linked_list = ll([1, 2, 3, 4])
    assert linked_list.search(5) == None

def test_search_duplicate_element():
    linked_list = ll([1, 3, 2, 3, 4])
    assert linked_list.search(3) is not None

def test_empty():
    linked_list = ll([])
    assert linked_list.is_empty() == True

def test_nonempty():
    linked_list = ll([1, 2, 3, 4])
    assert linked_list.is_empty() == False
def test_size():
    linked_list = ll([1, 2, 3, 4])
    assert linked_list.size() == 4

def test_zero_sized():
    linked_list = ll([])
    assert linked_list.size() == 0

def test_append():
    """
    not writing the other edge test cases like empty list, etc 
    because already included in the insert function tests.
    """
    linked_list = ll([])
    linked_list.append(1)
    linked_list.append(2)
    linked_list.append(3)
    assert str(linked_list) == "3 --> 2 --> 1 --> None"

def test_pop():
    linked_list = ll([1, 2, 3, 4])
    popped = linked_list.pop()
    assert popped == 4

def test_pop_from_empty():
    linked_list = ll([])
    assert linked_list.pop() == None

def test_pop_from_one_node():
    linked_list = ll([2, 3])
    linked_list.pop()
    assert str(linked_list) == "2 --> None"

def test_middle_element():
    linked_list = ll([1,2,3])
    assert linked_list.middle_element() == 2

def test_middle_element_of_even_sized_llist():
    linked_list = ll([1,2,3,4])
    assert linked_list.middle_element() == 3

def test_copy():
    linked_list = ll([1,2,3,4])
    copy_list = linked_list.copy()
    assert str(copy_list) == str(linked_list)
    
def test_copy_empty():
    linked_list = ll([])
    copy_list = linked_list.copy()
    assert str(copy_list) == str(linked_list)

def test_move_head_to_tail():
    linked_list = ll([1,2,3,4])
    linked_list.move_tail_to_head()
    assert str(linked_list) == "4 --> 1 --> 2 --> 3 --> None"

def test_move_head_to_tail_size_1():
    linked_list = ll([1])
    linked_list.move_tail_to_head()
    assert str(linked_list) == "1 --> None"

def test_remove_duplicates():
    linked_list = ll([1,2,2,3,4])
    linked_list.remove_duplicates()
    assert str(linked_list) == "1 --> 2 --> 3 --> 4 --> None"

def test_remove_duplicates_with_no_duplicates():
    linked_list = ll([1,2,3,4])
    linked_list.remove_duplicates()
    assert str(linked_list) == "1 --> 2 --> 3 --> 4 --> None"

def test_remove_duplicates_from_empty_llist():
    linked_list = ll([])
    linked_list.remove_duplicates()
    assert str(linked_list) == "None"

def test_nodes():
    linked_list = ll([1,2,3,4])
    linked_list.swap_nodes(1,4)
    assert str(linked_list) == "4 --> 2 --> 3 --> 1 --> None"

def test_nodes_from_empty_llist():
    linked_list = ll([])
    linked_list.swap_nodes(1,4)
    assert str(linked_list) == "None"

def test_nodes_x_and_y_equal():
    linked_list = ll([1,2,3])
    linked_list.swap_nodes(1,1)
    assert str(linked_list) == "1 --> 2 --> 3 --> None"