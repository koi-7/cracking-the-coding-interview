#!/usr/bin/env python3
# coding: utf-8


def set_zeros(A, M, N):
    zeros_row = set()
    zeros_column = set()

    for m in range(M):
        for n in range(N):
            if A[m][n] == 0:
                zeros_row.add(m)
                zeros_column.add(n)

    for m in range(M):
        for n in range(N):
            if (m in zeros_row) or (n in zeros_column):
                A[m][n] = 0

    return A

def main():
    M, N = map(int,input().split())
    A = [list(map(int, input().split())) for _ in range(M)]
    A = set_zeros(A, M, N)

    for i in range(M):
        print()
        for j in range(N):
            print(A[i][j], end=' ')


if __name__ == '__main__':
    main()
