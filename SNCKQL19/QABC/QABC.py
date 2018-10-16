import sys
sys.stdin = open('input.txt', 'r')

def check(A, B, N):
    for i in range (0, N):
        diff = B[i] - A[i]
        if diff < 0:
            return False
        elif diff > 0:
            try:
                A[i] += 1 * diff
                A[i+1] += 2 * diff
                A[i+2] += 3 * diff
            except IndexError:
                return False
    return True

T = int(input())

for i in range(0, T):

    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    if check(A, B, N):
        print('TAK')
    else:
        print('NIE')
