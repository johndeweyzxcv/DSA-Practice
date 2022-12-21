# https://leetcode.com/problems/linked-list-cycle-ii/

class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class LinkedLists:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def insert(self, val):
        node = Node(val=val)
        if self.tail is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node

    def read_list(self):
        list_data = []
        current = self.head
        while current:
            list_data.append(current.val)
            current = current.next
        return list_data

class Solution(object):
    def detectCycle(self, head):
        list_data = []

        while head:
            if head in list_data:
                return head
                
            list_data.append(head)
            head = head.next