# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    N = len(A)
    # Sanity check
    if N == 0:
        raise ValueError("Input length must be greater than 0")
    if N == 1:
        return A[0]

    # Count all deltas
    minDist = None
    left = 0
    right = sum(A)

    for i in range(len(A) - 1):
        left += A[i]
        right -= A[i]
        diff = abs(left - right)

        if minDist is None or diff < minDist:
            minDist = diff

    return minDist


# 50% 100% 0%