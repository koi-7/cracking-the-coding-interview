#!/usr/bin/env python3
# coding: utf-8


from node import *


def add_lists(A, B):
    s = 0

    for L in [A, B]:
        counter = 0
        p = L
        while p != None:
            s += p.data * (10 ** counter)
            p = p.next
            counter += 1

    s = str(s)
    p = Node(None)

    for i in range(len(s)):
        p.append_to_tail(int(s[-i-1]))

    return p.next

def main():
    A, B = [list(map(int, input().split())) for _ in range(2)]
    A = make_linked_list(A)
    B = make_linked_list(B)

    print_linked_list(add_lists(A, B))


if __name__ == '__main__':
    main()
