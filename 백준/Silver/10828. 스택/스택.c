#include <stdio.h>
#include <string.h>

void push(int value);
int is_empty();
void pop();
void get_size();
void get_top();

typedef struct {
	int top;
	int data[10000];
} Stack;

Stack s = { .top = -1 }; // top이 -1로 초기화되고, 나머지 멤버인 data배열은 0으로 초기화됨 

int main(void) {
	int n; // 입력할 수 있는 명령의 수 
	scanf("%d", &n);

	for (int i = 0; i < n; i++) {
		char cmd[6]; // 입력 명령어 
		scanf(" %s", cmd);

		if (strcmp(cmd, "push") == 0) { // cmd == "push" (x) cmd는 주솟값을 저장하고 있기 때문!! -> 문자열 비교 함수 strcmp() 사용해야됨 
			int num;
			scanf("%d", &num);
			push(num);
		}
		else if (strcmp(cmd, "pop") == 0)
			pop();
		else if (strcmp(cmd, "size") == 0)
			get_size();
		else if (strcmp(cmd, "empty") == 0)
			is_empty();
		else if (strcmp(cmd, "top") == 0)
			get_top(); 
	}
}

void push(int value) { // 정수 value를 스택에 넣음
	s.data[++(s.top)] = value;
}

int is_empty() { // 스택이 비어있으면 1, 아니면 0을 출력한다
	if (s.top == -1)
		printf("%d\n", 1);
	else
		printf("%d\n", 0);
}

void pop() { //스택에서 가장 위에 있는 정수를 빼고, 그 수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
	if (s.top==-1) {
		printf("%d\n", -1);
	}
	else {
		printf("%d\n", s.data[(s.top)--]);
	}
}

void get_size() { // 스택에 들어있는 정수의 개수를 출력한다.
	printf("%d\n", s.top + 1);
}




void get_top() { // 스택의 가장 위에 있는 정수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
	if (s.top==-1)
		printf("%d\n", -1);
	else
		printf("%d\n", s.data[s.top]);
}
