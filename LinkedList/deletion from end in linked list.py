class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

#creating nodes
node1 = Node(10)
node2 = Node(20)
node3 = Node(30)
node4 = Node(40)

#connecting nodes to form a linked list
node1.next = node2
node2.next = node3
node3.next = node4

#deletion from the end in linked list
head = node1
current = head
while current.next.next is not None:
    current = current.next
current.next = None

#printing the linked list
current = head
while current is not None:
    print(current.data, end=" -> ")
    current = current.next
print("None")
