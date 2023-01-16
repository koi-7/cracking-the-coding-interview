#!/usr/bin/env python3
# coding: utf-8


def compress(s):
    s_org = s
    s = s + ' '

    i = 0
    while s[i+1] != ' ':
        if s[i] == s[i+1]:
            i += 1
        else:
            s = s[:i+1] + ',' + s[i+1:]
            i += 2

    s = s.strip()
    l = s.split(',')

    compressed = ''
    for i in range(len(l)):
        compressed += l[i][0] + str(len(l[i]))

    if len(s_org) < len(compressed):
        return s_org
    else:
        return compressed

def main():
    s = input().strip()
    print(compress(s))


if __name__ == '__main__':
    main()
