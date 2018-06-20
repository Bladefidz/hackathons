import unittest
import random

from tape_equilibrium import *

N_RANGE = (2, 100000)
ELEMENT_RANGE = (-1000, 1000)

class TestExercise(unittest.TestCase):
    def test_example1(self):
        self.assertEqual(solution([3, 1, 2, 4, 3]), 1)

    def test_simple(self):
        self.assertEqual(solution([1,2]), 1)

    def test_double(self):
        self.assertEqual(solution([-1000, 1000]), 2000)

    def test_random(self):
        N = random.randint(*N_RANGE)
        arr = [random.randint(*ELEMENT_RANGE) for _ in xrange(N)]
        print N, solution(arr), arr

    def test_maximum(self):
        arr = [random.randint(*ELEMENT_RANGE) for _ in range(100000)]
        print 100000, solution(arr), arr


if __name__ == '__main__':
    unittest.main()