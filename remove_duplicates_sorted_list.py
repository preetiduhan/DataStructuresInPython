'''
Created on 27-May-2019

@author: preeti
'''
'''
Created on 26-May-2019

@author: preeti
'''
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

    def insert_list_back(self, data):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
            return self.head
        else:
            ptr = Node()
            new_node = Node(data)
            ptr= self.head
            while ptr.next_node is not None:
                ptr=ptr.next_node
            ptr.next_node = new_node
            return self.head

    def remove_dups_sorted_list(self, head):
        import pdb
        #pdb.set_trace()
        temp = [None] * 100
        ptr = Node()
        ptr1 = Node()
        ptr = head
        ptr1 = head
        while ptr1.next_node is not None:
            if temp[ptr.data] is None:
                temp[ptr.data] = ptr.data
            else:
                while temp[ptr.data] is not None and ptr1.next_node is not None:
                    ptr1.next_node = ptr.next_node
                    if ptr1.next_node is not None:
                        ptr = ptr1.next_node
                    else:
                        ptr = ptr1
            if ptr and ptr.next_node:
                ptr1 = ptr
                ptr= ptr.next_node
        return head

    def print_list(self, head):
        ptr = Node()
        ptr = head
        while ptr.next_node is not None:
            print(ptr.data)
            ptr = ptr.next_node
        print(ptr.data)

obj = Llist()
head = obj.insert_list_back(1)
head = obj.insert_list_back(3)
head = obj.insert_list_back(3)
head = obj.insert_list_back(3)
head = obj.insert_list_back(4)
head = obj.insert_list_back(4)
'''head = obj.insert_list_back(1)
head = obj.insert_list_back(1)
head = obj.insert_list_back(1)'''
#obj.print_list(head)
head = obj.remove_dups_sorted_list(head)
obj.print_list(head)
