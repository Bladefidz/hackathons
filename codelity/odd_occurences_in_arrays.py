# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    N = len(A)

    # Extreme values
    if N == 0:
        return 0
        
    # Value counter
    A.sort()
    prev = A[0]
    cnt = 1
    for a in A[1:]:
        if a == prev:
            cnt += 1
            continue
        if cnt == 1:
            return prev
        prev = a
        cnt = 1
    return 0

# 22%, 0%, 50%