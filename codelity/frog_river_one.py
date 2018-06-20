# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(X, A):
    N = len(A)
    # Sanity check
    if N == 0:
        raise ValueError("Input must be greater that 0")
    if N == 1 and N[0] == 1:
        return 0

    upperBound = 2 ** (X+1) - 2
    current = 0
    for i in range(len(A)):
        current |= 2**A[i]
        # print(bin(current), A[i])
        if current == upperBound:
            return i

    # Not able to cross river
    return -1

# 63% 83% 40%