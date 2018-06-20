// you can write to stdout for debugging purposes, e.g.
// printf("this is a debug message\n");
#include <stdlib.h>

int cmp(const void *a, const void *b)
{
    return *((int *) a) - *((int *)b);
}

int solution(int A[], int N)
{
    if (N == 0) {
        return 0;
    }
    if (N == 1) {
    	return A[0];
    }

    qsort(A, N, sizeof(int), cmp);

    int i = A[0];
    for (int j = 1; j < N; j++) {
        if (A[j] == i) {
            continue;
        }
        if (A[j] != i + 1) {
            return i + 1;
        }
        i++;
    }
    
    return i;
}


/* 50% 20% 80% */