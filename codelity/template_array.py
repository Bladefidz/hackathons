# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    N = len(A)
    # Sanity check
    if N == 0:
        raise ValueError("Input length must be greater than 0")