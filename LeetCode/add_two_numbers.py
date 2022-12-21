# https://leetcode.com/problems/add-two-numbers/

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
    def __init__(self):
        self.head = None

    def addTwoNumbers(self, l1, l2):
        l1_data = []
        l2_data = []
        head_1 = l1
        head_2 = l2

        while head_1:
            l1_data.append(str(head_1.val))
            head_1 = head_1.next
        while head_2:
            l2_data.append(str(head_2.val))
            head_2 = head_2.next

        l1_data.reverse()
        l2_data.reverse()
        l1_data = int(''.join(l1_data))
        l2_data = int(''.join(l2_data))
        sum = l1_data + l2_data
        sum = list(str(sum))
        sum.reverse()

        for i in sum:
            node = Node(i)
            if self.head is None:
                self.head = node
            else:
                current = self.head
                while current:
                    if current.next is not None:
                        current = current.next
                    else:
                        current.next = node
                        break

        return self.head

linked_lists = LinkedLists()
linked_lists.insert(2)
linked_lists.insert(4)
linked_lists.insert(3)

linked_lists_2 = LinkedLists()
linked_lists_2.insert(5)
linked_lists_2.insert(6)
linked_lists_2.insert(4)

sol = Solution()
print(sol.addTwoNumbers(linked_lists.head, linked_lists_2.head))
