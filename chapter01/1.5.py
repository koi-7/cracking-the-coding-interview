#!/usr/bin/env python3
# coding: utf-8


def is_edited(s1, s2):
    if s1 == s2:
        return True

    if len(s1) + 1 == len(s2):    # 挿入
        for i in range(len(s1)):
            if s1[i] == s2[i]:
                continue
            else:
                return s1[i:] == s2[i+1:]
        return True
    elif len(s1) - 1 == len(s2):  # 削除
        for i in range(len(s2)):
            if s1[i] == s2[i]:
                continue
            else:
                return s1[i+1:] == s2[i:]
        return True
    elif len(s1) == len(s2):      # 置き換え
        flag = False
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                if flag:
                    return False
                flag = True
        return True

    return False

def main():
    s1, s2 = input().split()
    print(is_edited(s1, s2))


if __name__ == '__main__':
    main()
