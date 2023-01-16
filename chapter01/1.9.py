#!/usr/bin/env python3
# coding: utf-8


def isSubstring(s1, s2):
    return s2 in s1

def is_rotation(s1, s2):
    if len(s1) != len(s2):
        return False

    s1s1 = s1 + s1
    return isSubstring(s1s1, s2)

def main():
    s1, s2 = input().split()
    print(is_rotation(s1, s2))


if __name__ == '__main__':
    main()
