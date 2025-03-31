#include <stdio.h>
int bool_vps(int n);
void push(char value);
void pop();

int top = -1;
char ps[51];
int result = -1; // 0: NO

int main(void) {   
    int n; // 입력데이터 수 
    scanf("%d", &n);
    bool_vps(n);   
}


int bool_vps(int n) {
    char value[51];
    for (int i = 0; i < n; i++) {
        scanf("%s", value);
        for (int j = 0; j < sizeof(value); j++) {

            if (value[j] == '\0')
                break;

            if (value[j] == '(')
                push(value);

            else if (value[j] == ')')
                pop();

            if (result == 0) {
                break;
            }
        }

        if ((top == -1) && (result == -1))
            printf("YES\n");
        else if (result == 0) {
            printf("NO\n");
            top = -1;
            result = -1; // 초기화 
        }
        else {
            printf("NO\n");
            top = -1;
            result = -1;
        }
    }
    return 0;
}

void push(char value) {
    ps[++top] = value;
}

void pop() {
    if (top < 0) { // 원소가 하나도 없는 경우
        result = 0; //NO
    }
    else
        top--;
}
