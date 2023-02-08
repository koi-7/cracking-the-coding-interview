#!/usr/bin/env python3
# coding: utf-8


from node import *


def delete_dups(linked_list):
    s = set()
    p = linked_list
    while p != None:
        if p.data in s:
            p.prev.next = p.next
            if p.next != None:
                p.next.prev = p.prev
        else:
            s.add(p.data)
        p = p.next

    return linked_list

def main():
    l = list(map(int, input().split()))
    linked_list = make_linked_list(l)
    linked_list = delete_dups(linked_list)
    print_linked_list(linked_list)


if __name__ == '__main__':
    main()
