'''
Created on 26-May-2019

@author: preeti
'''
import pdb
class Node:
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

class Llist(object):
    def __init__(self):
        self.head = None

    def insert_list_front(self, data):
        if self.head is None:
            self.head = Node(data)
            return self.head
        else:
            new_node = Node(data)
            new_node.next_node = self.head
            self.head = new_node
            return self.head

    def length_list(self, head):
        ptr = Node()
        size = 0
        ptr = self.head
        while ptr is not None:
            size = size + 1
            ptr = ptr.next_node
        return size

    def nth_node_last(self, n):
        #pdb.set_trace()
        size = obj.length_list(self.head)
        print("size=%s",size)
        node_index = size - n
        print("node_index=%s",node_index)
        ptr = Node()
        ptr = head
        while node_index > 0:
            ptr = ptr.next_node
            node_index = node_index -1
        return ptr

    def delete_node(self, data):
        ptr = Node()
        ptr1= Node()
        ptr = self.head
        ptr1 = self.head.next_node
        if ptr.data is data:
            self.head = ptr1
        elif ptr1.data is data:
            self.head.next_node = ptr1.next_node
        else:
            while ptr1.data is not data and ptr1 is not None:
                ptr = ptr.next_node
                ptr1 = ptr1.next_node
            if ptr1.data is data:
                ptr.next_node = ptr1.next_node
            else:
                print("Element is not found")
        return self.head

    def print_list(self, head):
        ptr = Node()
        ptr = head
        while ptr.next_node is not None:
            print(ptr.data)
            ptr = ptr.next_node
        print(ptr.data)

obj = Llist()
head = obj.insert_list_front('5')
head = obj.insert_list_front('6')
head = obj.insert_list_front('7')
head = obj.insert_list_front('8')
head = obj.insert_list_front('9')
head = obj.insert_list_front('10')
obj.print_list(head)
x = obj.length_list(head)
print("length of llist %s",x)
ptr = Node()
index = 4
ptr = obj.nth_node_last(index)
print("nth node is %s",ptr.data)