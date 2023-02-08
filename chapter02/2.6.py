#!/usr/bin/env python3
# coding: utf-8


from node import *


def is_palindrome(L):
    p1 = L
    p2 = L
    while p2.next != None:
        p2 = p2.next

    while (p1 != p2) and (p2.next != p1):
        if p1.data != p2.data:
            return False
        p1 = p1.next
        p2 = p2.prev

    return True

def main():
    L = list(map(int, input().split()))
    L = make_linked_list(L)

    print(is_palindrome(L))


if __name__ == '__main__':
    main()
