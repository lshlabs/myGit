#include <stdio.h>

#define MAX_DWARFS 9
#define TARGET_DWARFS 7
#define TARGET_SUM 100

void sortArray(int arr[], int size) {
    for(int i = 0; i < size - 1; i++) {
        for(int j = 0; j < size - 1 - i; j++) {
            if(arr[j] > arr[j + 1]) {
                int temp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = temp;
            }
        }
    }
}

int findCombination(int arr[], int picked[], int start, int n, int r, int idx) {
    if (r == 0) {
        int sum = 0;
        for(int i = 0; i < idx; i++) {
            sum += picked[i];
        }
        return (sum == TARGET_SUM);  // 합이 100이면 1 반환

    }
    
    for (int i = start; i < n; i++) {
        picked[idx] = arr[i];
        if (findCombination(arr, picked, i + 1, n, r - 1, idx + 1)) {
            return 1;  // 유효한 조합을 찾으면 즉시 반환
        }
    }
    return 0;  // 유효한 조합을 찾지 못함
}

int main(void) {
    int heights[MAX_DWARFS];
    int picked[TARGET_DWARFS];
    
    for(int i = 0; i < MAX_DWARFS; i++) {
        scanf("%d", &heights[i]);
    }
    
    findCombination(heights, picked, 0, MAX_DWARFS, TARGET_DWARFS, 0);
    
    sortArray(picked, TARGET_DWARFS);
    for(int i = 0; i < TARGET_DWARFS; i++) {
        printf("%d\n", picked[i]);
    }
    
    return 0;
}