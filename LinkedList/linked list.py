class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:   
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def insert_at_position(self, data, position):
        if position == 0:
            self.insert_at_beginning(data)
            return
        new_node = Node(data)
        current_node = self.head
        for _ in range(position - 1):
            if current_node is None:
                print("Position out of range")
                return
            current_node = current_node.next
        new_node.next = current_node.next
        current_node.next = new_node

    def print_list(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=" -> ")
            current_node = current_node.next
        print("None")

    def find_length(head):
        length = 0
        current_node = head
        while current_node:
            length += 1
            current_node = current_node.next
        return length
    
    def search(head, key):
        current_node = head
        while current_node:
            if current_node.data == key:
                return True
            current_node = current_node.next
        return False
    
    def delete_node(head, key):
        if head is None:
            return None
        if head.data == key:
            return head.next
        current_node = head
        while current_node.next:
            if current_node.next.data == key:
                current_node.next = current_node.next.next
                return head
            current_node = current_node.next
        return head

    def reverse_list(head):
        prev_node = None
        current_node = head
        while current_node:
            next_node = current_node.next
            current_node.next = prev_node
            prev_node = current_node
            current_node = next_node
        return prev_node

# Create a linked list
linked_list = LinkedList()

# Insert elements
linked_list.insert_at_end(1)
linked_list.insert_at_end(2)
linked_list.insert_at_beginning(8)
linked_list.insert_at_end(3)
linked_list.insert_at_beginning(0)
linked_list.insert_at_position(5, 2)

# Print the list
linked_list.print_list()
