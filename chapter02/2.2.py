#!/usr/bin/env python3
# coding: utf-8


from node import *


def print_Kth_to_last(linked_list, k):
    p = linked_list
    length = 0
    while p != None:
        length += 1
        p = p.next

    p = linked_list
    index = length - k
    for _ in range(index):
        p = p.next

    return p.data


def main():
    k = int(input().strip())
    l = list(map(int, input().split()))
    linked_list = make_linked_list(l)

    print(k)
    print_linked_list(linked_list)

    print(print_Kth_to_last(linked_list, k))

if __name__ == '__main__':
    main()
