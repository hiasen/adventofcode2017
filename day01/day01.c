#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>

void
part1()
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

void
part2()
{
	char buffer[4096];
	int bytes_read = fread(buffer, 1, 4096, stdin);
	while (!isdigit(buffer[bytes_read - 1])) {
		bytes_read--;
	}
	if (bytes_read % 2 != 0) {
		fprintf(stderr, "The number of digits should be even!");
		exit(1);
	}
	int half = bytes_read/2;
	int the_sum = 0;
	for (int i = 0; i < half; ++i) {
		if (buffer[i] == buffer[i+half]) {
			the_sum += (buffer[i] - 48);
		}
	}
	printf("%d\n", the_sum*2);

}

int
main(int argc, char *argv[])
{
	if (argc > 1) {
		part2();
	} else {
		part1();
	}
	return 0;
}
