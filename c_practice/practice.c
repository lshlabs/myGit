#include <stdio.h>

int main(void) {
    int play[8];
    int isAscending = 1;
    int isDescending = 1;
    
    for(int i = 0; i < 8; i++) {
        scanf("%d", &play[i]);
    }

    if(play[0] == 1) {
        for(int i = 0; i < 7; i++) {
            if(play[i] + 1 != play[i+1]) {
                isAscending = 0;
                break;
            }
        }
        isDescending = 0;
    } else if(play[0] == 8) {
        for(int i = 0; i < 7; i++) {
            if(play[i] - 1 != play[i+1]) {
                isDescending = 0;
                break;
            }
        }
        isAscending = 0;
    } else {
        isAscending = 0;
        isDescending = 0;
    }

    if(isAscending) {
        printf("ascending\n");
    } else if(isDescending) {
        printf("descending\n");
    } else {
        printf("mixed\n");
    }
    
    return 0;
}