//첫째 줄에 단어가 주어진다. 단어의 길이는 1보다 크거나 같고, 100보다 작거나 같으며, 알파벳 소문자로만 이루어져 있다.
//출력
//첫째 줄에 팰린드롬이면 1, 아니면 0을 출력한다.
#include <stdio.h>
#include <string.h>
#define MAX_LENGTH 100
#define MIN_LENGTH 1

int isPalindrome(char word[]) {
    int len = strlen(word);
    for(int i = 0; i < len/2; i++) {
        if(word[i] != word[len - i - 1]) return 0;
    }
    return 1;
}

int main() {
    char word[MAX_LENGTH + 1];  // null 문자를 위한 공간
    
    if(scanf("%99s", word) != 1) {
        printf("입력 오류\n");
        return 1;
    }

    int len = strlen(word);
    if(len < MIN_LENGTH || len > MAX_LENGTH) {
        printf("입력 오류\n");
        return 1;
    }

    printf("%d\n", isPalindrome(word));
    return 0;
}