# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    N = len(A)
    if N == 0:
        raise ValueError("Input must be greater than 0")
    if N == 1:
        if A[0] == 1:
            return 2
        else:
            return 1
    mini = None
    mini1 = None
    maxi = -1000000
    for i in A:
        if i > maxi:
            maxi = i
        if mini is None:
            mini = i
            continue
        if i > mini:
            if i - mini > 0:
                if mini1 == None:
                    mini1 = i
                if i < mini1:
                    mini1 = i
            mini = i
    #print(i, mini, mini1, maxi)
    if mini < 0:
        return 1
    if mini1 == None:
        return maxi + 1
    else:
        return mini1 + 1