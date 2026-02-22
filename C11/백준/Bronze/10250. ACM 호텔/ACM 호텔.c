#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main(void) {
	int t;
	scanf("%d", &t);
	for (int i = 1; i <= t; i++) {
		int h, w, n;
		scanf("%d %d %d", &h, &w, &n);
		int floor, ho;
		floor = n % h;
		ho = n / h + 1;
		if (n % h == 0) {
			floor = h;
			ho = n / h;
		}
		int room_num = 100 * floor + ho;
		printf("%d\n", room_num);
	}

	return 0;
}