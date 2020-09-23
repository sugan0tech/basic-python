class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def print_linked_list(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next
class Solution:
    def add_linkedlist(self, l1, l2):
        self.l1 = l1
        self.l2 = l2
        result = LinkedList()
        x = l1.head.data + l2.head.data
        y = l1.head.next.data + l2.head.next.data 
        z = l1.head.next.next.data + l2.head.next.next.data
        if x >= 10:
            x -= 10
            y += 1
        if y>= 10:
            y -= 10
            z += 1
        result.head = Node(x)
        result.head.next = Node(y)
        result.head.next.next = Node(z)
        result.print_linked_list()

L1 = LinkedList()
L2 = LinkedList()
L1.head  = Node(9)
L1.head.next = Node(2)
L1.head.next.next = Node(3)
L2.head = Node(4)
L2.head.next = Node(5)
L2.head.next.next = Node(6)
Solution().add_linkedlist(L1, L2)