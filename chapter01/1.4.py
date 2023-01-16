#!/usr/bin/env python3
# coding: utf-8


def is_palindrome_permutation(s):
    s = s.lower()
    s = s.replace(' ', '')

    d = {}
    while(s != ''):
        d[s[0]] = s.count(s[0])
        s = s.replace(s[0], '')

    odd_count = 0
    for val in d.values():
        if val % 2 != 0:
            odd_count += 1

    if odd_count > 1:
        return False
    else:
        return True

def main():
    s = input()
    print(is_palindrome_permutation(s))


if __name__ == '__main__':
    main()
