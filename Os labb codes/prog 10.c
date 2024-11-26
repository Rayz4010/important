#include <stdio.h>
void scanDiskSchedule(int request[], int n, int head) {
int seekCount = 0;
int direction = 1; // 1 for right, 0 for left
// Sort the request array in ascending order
for (int i = 0; i < n; i++) {
for (int j = 0; j < n - i - 1; j++) {
if (request[j] > request[j + 1]) {
int temp = request[j];
request[j] = request[j + 1];
request[j + 1] = temp;
}
}
}
// Move the head in the specified direction
for (int i = 0; i < n; i++) {
if (direction == 1) {
// Moving to the right
seekCount += abs(head - request[i]);
head = request[i];
} else {
// Moving to the left
seekCount += abs(head - request[i]);
head = request[i];
}
}
printf("Total seek count: %d\n", seekCount);
}
int main() {
int request[] = {53, 183, 37, 122, 14, 124, 65, 67};
int n = sizeof(request) / sizeof(request[0]);
int head = 53;
printf("Initial head position: %d\n", head);
printf("Request queue: ");
for (int i = 0; i < n; i++) {
printf("%d ", request[i]);
}
printf("\n");
scanDiskSchedule(request, n, head);
return 0;
}