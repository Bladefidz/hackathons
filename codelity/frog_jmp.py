# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(X, Y, D):
    jump = 0
    
    while X < Y:
        X += D
        jump += 1
    
    return jump

# 44% 100% 0%