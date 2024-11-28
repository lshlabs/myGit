#include <stdio.h>

int main() {
    int fibo[46] = {0, 1};
    int n;
    scanf("%d", &n);
    
    // n = 4, i = 2 ~ 3, fibo[] = {0, 1, 1, 2}
    // n = 5, i = 2 ~ 4, fibo[] = {0, 1, 1, 2, 3}
    for(int i = 2; i < n; i++) {
        fibo[i] = fibo[i-1] + fibo[i-2];
    }
    
    printf("%d", fibo[n]);
    
    return 0;
}