#!/usr/bin/env python3
# coding: utf-8


def is_unique(s):
    return len(s) == len(set(s))

def main():
    s = input()
    print(is_unique(s))


if __name__ == '__main__':
    main()
