#include <stdio.h>
#include <string.h>
#include <math.h>

/**
# Let
T = set()
tuples = [(0, 1), (2, 3), (4, 5)]
D = 3  # Threshold
for tuple in tuples:
	if sum(tuple) > D:
		T.add(tuple)

# Find
S = set([(10, 1), (11, 0), (2, 8)])
M = len(S)

# Where
N = 2

# Then
subsetS = minimumUglinessof(S, N)

# Define
minimalLexicograph(S, N):
	return A

minimumUglinessof(S, N):
	T = minimalLexicograph(S, N)
**/
int main(int argc, char const *argv[])
{
	// Get constrains N, M, D as string
	char constrains[20];
	gets(constrains);
	
	// Find index of space
	int space1 = 0;
	int space2 = 0;
	int index = 0;
	int len1 = 0;
	while (constrains[index] != '\0') {
		char c = constrains[index];
		if (c == ' ') {
			if (space1 == 0) {
				space1 = index;
				++index;
				++len1;
				continue;
			}
			if (space1 != 0 && space2 == 0) {
				space2 = index;
			}
		}
		++index;
		++len1;
	}

	// // Inspect space indexes
	// printf("First space = %d\n", space1);
	// printf("Second space = %d\n", space2);
	// printf("Length = %d\n", len1);

	// Transform constrains into N, M, D
	int N, M, D;
	N = 0;
	M = 0;
	D = 0;
	for (int i = 0; i < space1; i++) {
		int digit = constrains[i] - '0';
		int p = space1 - i - 1;
		N += digit * (int) pow(10, p);
	}
	for (int i = space1+1; i <= space2; i++) {
		int digit = constrains[i] - '0';
		int p = space2 - i - 1;
		M += digit * (int) pow(10, p);
	}
	for (int i = space2+1; i < len1; i++) {
		int digit = constrains[i] - '0';
		int p = len1 - i - 1;
		D += digit * (int) pow(10, p);
	}

	// // Inspect N, M, D
	// printf("N = %d\n", N);
	// printf("M = %d\n", M);
	// printf("D = %d\n", D);

	// Get set of T as string
	char set[M];
	gets(set);


}