# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
import math

def solution(N):
    # Expect all 1-bits
    logN = math.log(N+1, 2)
    if logN - int(logN) == 0:
        return 0
    
    logN = math.log(N, 2)
    logNFloor = int(logN)

    # Expect 1-bit followed by 0s
    if logN - logNFloor == 0:
        return 0

    # Find longest gap
    logN1 = math.log(N - 2**logNFloor, 2)
    logNFloor1 = int(logN1)
    if logNFloor1 % 2 == 0:
        # Longest gap should be at the left
        return logNFloor - logNFloor1 - 1
    else:
        # Longest gap may either at left or right
        left = logNFloor - logNFloor1 - 1
        right = logNFloor1 - 1
        if left > right:
            return left
        else:
            return right

# 50%, 50%