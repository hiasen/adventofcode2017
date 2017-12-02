#include <stdio.h>
#include <ctype.h>

int
main(int argc, char *argv[])
{
	int first = getchar();
	int previous = first;
	int current;
	int the_sum = 0;
	while ((current = getchar()) != EOF) {
		if (!isdigit(current)) {
			continue;
		}
		if (previous == current) {
			the_sum += (current - 48);
		}
		previous = current;
	}
	if (previous == first) {
		the_sum += (previous - 48);
	}
	printf("%d\n", the_sum);
}
