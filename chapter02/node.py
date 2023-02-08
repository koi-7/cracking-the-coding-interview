# coding: utf-8


class Node:
    def __init__(self, data):
        self.prev = None
        self.next = None
        self.data = data

    def append_to_tail(self, d):
        end = Node(d)
        n = self
        while n.next != None:
            n = n.next
        n.next = end


def make_linked_list(l):
    head = Node(l[0])
    tail = head
    for i in range(1, len(l)):
        new_node = Node(l[i])
        tail.next = new_node
        new_node.prev = tail
        tail = new_node

    return head

def print_linked_list(node):
    p = node
    while p.next != None:
        print(p.data, end=' ')
        p = p.next
    print(p.data)


