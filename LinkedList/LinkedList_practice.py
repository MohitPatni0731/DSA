import pytest
# Add typing to all methods
# Add unit tests for all methods
# Write time and space complexity for all methods as comment in their docstring

class Node:
    def __init__(self, data) -> None: 
        """
        Initializes a new node with the specified data.
        Parameters:
        - data: The data to store in the node.

        Time complexity - O(1)
        Space complexity - O(1)
        """
        self.data = data
        self.next = None
    

class LinkedList:
    def __init__(self) -> None:
        """
        Initializes a new empty linked list.
        """
        self.head = None

from typing import Any (on top of file)

    def insert(self, data: Any) -> None:
        """
        Inserts a new node with the given value at the beginning of the list.
        Parameters:
        - value: The value to insert.
        Time complexity - O(1)
        Space complexity - O(1)
        """
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def print(self):
        """
        Prints the contents of the list from head to tail.
        Time complexity - O(N)
        Space complexity - O(1)
        """
        current_node = self.head
        while current_node:
            print(current_node.data, end=" --> ")
            current_node = current_node.next
        print("None")


    def delete(self, value):
        """
        Inspired by: https://leetcode.com/problems/remove-linked-list-elements/description/
        
        Deletes the first occurrence of a node with the given value from the list.
        Parameters:
        - value: The value of the node to delete.
        """
        pass

    def search(self, value):
        """
        Searches for a node with the given value.
        Parameters:
        - value: The value to search for.
        Returns:
        - The node if found, else None.
        """
        pass

    def is_empty(self):
        """
        Checks if the list is empty.
        Returns:
        - True if the list is empty, False otherwise.
        """
        pass

    def size(self):
        """
        Returns the number of nodes in the list.
        Returns:
        - The size of the list.
        """
        pass
    
    def index(self, value):
        """
        Returns the position (0-based index) of the first occurrence of a node with the given value.
        Parameters:
        - value: The value to find the index of.
        Returns:
        - The index of the node if found, else -1.
        """
        pass

    def pop(self):
        """
        Removes and returns the last element from the list.
        Returns:
        - The data of the popped element.
        """
        pass

    def append(self, value):
        """
        Appends a new node with the given value to the end of the list.
        Parameters:
        - value: The value to append.
        """
        pass
    
    def middle_element(self):
        """
        Inspired from: https://leetcode.com/problems/middle-of-the-linked-list/description/
        
        Finds and returns the middle element of the list. If the list has an even number of elements, the second middle element is returned.
        Returns:
        - The data of the middle element.
        """
        pass

    def copy(self):
        """
        Creates a shallow copy of the list.
        Returns:
        - A new LinkedList instance that is a shallow copy of the original list.
        """
        pass

    def reverse(self):
        """
        Inspired by: https://leetcode.com/problems/remove-linked-list-elements/description/
        
        Reverses the list in place.
        """
        pass

    def remove_duplicates(self):
        """
        Inspired by: https://leetcode.com/problems/remove-duplicates-from-sorted-list/description/
        
        Removes duplicate values from the list.
        """
        pass

    def is_palindrome(self):
        """
        Inspired by: https://leetcode.com/problems/palindrome-linked-list/description/
        
        Checks if the list is a palindrome.
        Returns:
        - True if the list is a palindrome, False otherwise.
        """
        pass

    def swap_nodes(self, x, y):
        """
        Swaps the nodes with the given values x and y in the list. If x and y are the same, does nothing.
        Parameters:
        - x: The value of the first node to swap.
        - y: The value of the second node to swap.
        """
        pass

    def move_tail_to_head(self):
        """
        Moves the last node of the list to be the head of the list.
        """
        pass

