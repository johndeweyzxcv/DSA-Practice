# Swap Nodes in pairs
# Leetcode problem link https://leetcode.com/problems/swap-nodes-in-pairs/

# Example
# [1] -> [2] -> [3] -> [4] -> [5] -> [6] -> [7] = [2] -> [1] -> [3] -> [4] -> [6] -> [5] -> [7]

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
    def swapPairs(self, head):
        # head = [1] -> [2] -> [3] -> [4] -> [5] -> [6] -> [7]
        if head is None or head.next is None:
            return head

        previous = None
        new_head = None

        while head:
            if head.next is None:
                return new_head

            # current = [1]
            # current_pair = [2]
            # next_pair = [3]
            current = head
            current_pair = current.next
            next_pair = current_pair.next


            if previous is not None:
                previous.next = current_pair
            
            # Point the next of [1] to [3]
            # Point the next of [2] to [1]
            # Thus [1] -> [2] -> [3] = [2] -> [1] -> [3]

            current.next = next_pair
            current_pair.next = current

            # Previous = [1]
            # head = [3]

            previous = current
            head = next_pair
            
            if new_head is None:
                new_head = current_pair
        
        return new_head

    def read_list(self, head):
        current = head
        list_data = []
        while current:
            list_data.append(current.val)
            current = current.next
        return list_data

linked_lists = LinkedLists()
linked_lists.insert(1)
linked_lists.insert(2)
linked_lists.insert(3)
linked_lists.insert(4)
linked_lists.insert(5)
linked_lists.insert(6)
linked_lists.insert(7)

sol = Solution()
new_head = sol.swapPairs(linked_lists.head)
print(sol.read_list(new_head))