/**
 * Quick Sort Template
 */
#include <stdlib.h>

int numcmp(const void *a, const void *b)
{
    return *((int *)a) - *((int *)b);
}

int test(int A[], int N)
{
	qsort(A, N, sizeof(int), numcmp);
}