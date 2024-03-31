import pytest
from typing import Any

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


    def insert(self, data: Any) -> None:
        """
        Inserts a new node with the given value at the beginning of the list.
        Parameters:
        - value: The value to insert.
        Time complexity - O(1)
        Space complexity - O(1)
        """
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def __str__(self) -> str:
        """
        Returns a string representation of the list from head to tail.
        Time complexity - O(N)
        Space complexity - O(1)
        """
        result = []
        current_node = self.head
        while current_node:
            result.append(str(current_node.data))
            result.append(" --> ")
            current_node = current_node.next
        result.append("None")
        
        return ''.join(result) 


    def print_llist(self) -> None:
        print(str(self)) # calling str triggers __str__ function, here we have leveraged an existing function to implement another function.


    def delete(self, value: Any) -> None:
        """
        Inspired by: https://leetcode.com/problems/remove-linked-list-elements/description/
        
        Deletes the first occurrence of a node with the given value from the list.
        Parameters:
        - value: The value of the node to delete.
        Time - O(N)
        Space - O(1)
        """
        current_node = self.head
        previous_node = None
        while current_node:
            if current_node.data == value:
                if previous_node:
                    previous_node.next = current_node.next
                else:
                    self.head = current_node.next
                del current_node
                return
            else:
                previous_node = current_node
                current_node = current_node.next

    def search(self, value: Any) -> Node | None:
        """
        Searches for a node with the given value.
        Parameters:
        - value: The value to search for.
        Returns:
        - The node if found, else None.
        Time - O(N)
        Space - O(1)
        """
        current_node = self.head
        while current_node:
            if current_node.data == value:
                return current_node
            current_node = current_node.next               
        return None

    def is_empty(self) -> bool:
        """
        Checks if the list is empty.
        Returns:
        - True if the list is empty, False otherwise.
        Time - O(1)
        Space - O(1)
        """
        if self.head is None:
            return True
        else:
            return False

    def size(self) -> int:
        """
        Returns the number of nodes in the list.
        Returns:
        - The size of the list.
        Time - O(N)
        Space - O(1)
        """
        current_node = self.head
        count = 0
        while current_node:
            count += 1
            current_node = current_node.next
        return count
    
    def index(self, value) -> int:
        """
        Returns the position (0-based index) of the first occurrence of a node with the given value.
        Parameters:
        - value: The value to find the index of.
        Returns:
        - The index of the node if found, else -1.
        Time - O(N)
        Space - 
        """
        index = 0
        current = self.head

        while current is not None:
            if current.data == value:
                return index
            current = current.next
            index += 1
        return -1
    

    def pop(self) -> int:
        """
        Removes and returns the last element from the list.
        Returns:
        - The data of the popped element.
        Time - O(N)
        Space - 
        """
        if self.head is None:
            return None
        current = self.head
        previous = None
        while current.next is not None:
            previous = current
            current = current.next

        if previous is None:  
            self.head = None
        else:
            previous.next = None
        
        return current.data

    def append(self, data):
        """
        Appends a new node with the given value to the end of the list.
        Parameters:
        - value: The value to append.
        Time - O(N)
        Space - 
        """
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    
    def middle_element(self) -> int:
        """
        Inspired from: https://leetcode.com/problems/middle-of-the-linked-list/description/
        
        Finds and returns the middle element of the list. If the list has an even number of elements, the second middle element is returned.
        Returns:
        - The data of the middle element.
        Time - O(N)
        Space - O(N)
        """
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.next
        middle  = count // 2
        current = self.head
        for i in range(middle):
            current = current.next
            middle += 1
        return current.data


    def copy(self) -> None:
        """
        Creates a shallow copy of the list.
        Returns:
        - A new LinkedList instance that is a shallow copy of the original list.
        Time - O(N)
        Space - O(1)
        """
        copy_llist = LinkedList()
        current = self.head
        while current:
            copy_llist.insert(current.data)
            current = current.next
        return copy_llist

    def reverse(self):
        """
        Inspired by: https://leetcode.com/problems/remove-linked-list-elements/description/
        
        Reverses the list in place.
        """

    def remove_duplicates(self) -> None:
        """
        Inspired by: https://leetcode.com/problems/remove-duplicates-from-sorted-list/description/
        
        Removes duplicate values from the list.
        """
        current = self.head
        while current:
            next_node = current.next
            while next_node is not None and next_node.data == current.data:
                next_node = next_node.next
            current.next = next_node
            current = next_node 

    def is_palindrome(self):
        """
        Inspired by: https://leetcode.com/problems/palindrome-linked-list/description/
        
        Checks if the list is a palindrome.
        Returns:
        - True if the list is a palindrome, False otherwise.
        """
        pass

    def swap_nodes(self, x: int, y: int):
        """
        Swaps the nodes with the given values x and y in the list. If x and y are the same, does nothing.
        Parameters:
        - x: The value of the first node to swap.
        - y: The value of the second node to swap.
        Time - O(N)
        Space - O(N)
        """
        current = self.head
        while current:
            if current.data == x:
                current.data = y
            elif current.data == y:
                current.data = x
            current = current.next


    def move_tail_to_head(self) -> None:
        """
        Moves the last node of the list to be the head of the list.
        Time - O(N)
        Space - 
        """
        current = self.head
        previous = None
        while current.next:
            previous = current
            current = current.next
        previous.next = None
        current.next = self.head
        self.head = current
        return current

