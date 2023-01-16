#!/usr/bin/env python3
# coding: utf-8


def urlify(s):
    s = s.rstrip()
    s = s.replace(' ', '%20')
    return s

def main():
    s = input()
    print(urlify(s))


if __name__ == '__main__':
    main()
