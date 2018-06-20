# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A, K):
    N = len(A)

    # Extreme value
    if N == 0:
        return A
    
    # Main
    if K == N:
        return A
    if K > N:
        K = K % N
    if K < N:
        r = A[:N-K]
        l = A[N-K:]
        return l + r

# 100%, 100%