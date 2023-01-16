#!/usr/bin/env python3
# coding: utf-8


def is_permutation(s1, s2):
    return sorted(s1) == sorted(s2)

def main():
    s1, s2 = input().split()
    print(is_permutation(s1, s2))


if __name__ == '__main__':
    main()
