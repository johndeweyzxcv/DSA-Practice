# Reversing a Linked Lists
# Leetcode problem link https://leetcode.com/problems/reverse-linked-list/

# Example:
# [1] -> [2] -> [3] -> [4] -> [5] = [5] -> [4] -> [3] -> [2] -> [1]

class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class LinkedLists:
    def __init__(self, head=None):
        self.head = None
        self.tail = None
        self.size = 0
    
    def read_list(self):
        node_data = []
        node = self.head

        while node is not None:
            node_data.append(node.data)
            node = node.next
        
        return node_data

    def append(self, data):
        node = Node(data)
        
        if self.tail is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.size += 1
    
    def reverse_list(self):
        current = self.head
        previous = None

        while current:
            # Save the pointer of the NEXT node then point the NEXT of
            # CURRENT node to the PREVIOUS node.

            next_node = current.next
            current.next = previous

            # Change PREVIOUS pointer to CURRENT pointer then change
            # CURRENT to NEXT pointer.
            previous = current
            current = next_node
        
        self.head = previous

linked_lists = LinkedLists()

linked_lists.append('Monday')
linked_lists.append('Tuesday')
linked_lists.append('Wednesday')
linked_lists.append('Thursday')
linked_lists.append('Friday')
linked_lists.append('Saturday')
linked_lists.append('Sunday')

print(linked_lists.read_list())
linked_lists.reverse_list()
print(linked_lists.read_list())