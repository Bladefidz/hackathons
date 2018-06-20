# Maximum value of int
MAXINT = 2147483647

def solution(N):
	if not isinstance(N, int):
		raise TypeError("Input must be integer")
	if N < 1:
		raise ValueError("Input must be greater than 0")
	if N > MAXINT:
		raise ValueError("Input must be positive number not more than 2147483647")