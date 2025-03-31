#include <stdio.h>
#include <string.h>
#include <stdlib.h>

void queue(int n);
void push(int value);
int pop();
int size();
int isEmpty();
int get_front();
int get_back();

int queue_arr[10000];
int rear = -1;
int front = -1;

int main(void) {
	int n;
	scanf("%d", &n);
	queue(n);

	return 0;
}

void queue(int n) {
	char* cmd = (char*)malloc(100 * sizeof(char));
	if (cmd == NULL) {
		printf("메모리 할당 실패\n");
		return;
	}

	int result = 0;

	for (int i = 0; i < n; i++) {
		scanf(" %s", cmd); // 앞 공백으로 개행 문자 제거
		if (strcmp(cmd, "push") == 0) {
			int value = 0; 
			scanf("%d", &value); 
			push(value);
		}
		else if (strcmp(cmd, "pop") == 0) {
			result = pop();
			printf("%d\n", result);

		}
		else if (strcmp(cmd, "size") == 0) {
			result = size();
			printf("%d\n", result);
		}
		else if (strcmp(cmd, "empty") == 0) {
			result = isEmpty();
			printf("%d\n", result);
		}
		else if (strcmp(cmd, "front") == 0) {
			result = get_front();
			printf("%d\n", result);
		}
		else if (strcmp(cmd, "back") == 0) {
			result = get_back();
			printf("%d\n", result);
		}
	}
	free(cmd); 
}


void push(int value) {
	queue_arr[++rear] = value; 
}

int pop() {
	if (isEmpty())
		return -1;
	return queue_arr[++front];
}


int size() {
	return (rear - front);
}


int isEmpty() {
	if (rear == front)
		return 1; // queue is empty 
	else
		return 0;
}

int get_front() {
	if (isEmpty())
		return -1;
	return queue_arr[front + 1];
}

int get_back() {
	if (isEmpty())
		return -1;
	return queue_arr[rear];
}