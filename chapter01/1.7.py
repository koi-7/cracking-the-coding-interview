#!/usr/bin/env python3
# coding: utf-8


import numpy as np


def rotate(l):
    arr_l = np.array(l)
    arr_l_rot = np.rot90(arr_l)
    return arr_l_rot.tolist()

def main():
    N = int(input().strip())
    A = [list(map(int, input().split())) for _ in range(N)]
    A = rotate(A)
    for i in range(N):
        print()
        for j in range(N):
            print(A[i][j], end=' ')


if __name__ == '__main__':
    main()
