
// 재귀함수를 사용하여 조합을 찾는 함수
int findCombination(int arr[], int picked[], int start, int n, int r, int idx) {
    if (r == 0) {
        int sum = 0;
        for(int i = 0; i < idx; i++) {
            sum += picked[i];
        }
        return (sum == 100);  // 합이 100이면 1 반환
    }
    
    for (int i = start; i < n; i++) {
        picked[idx] = arr[i];
        if (findCombination(arr, picked, i + 1, n, r - 1, idx + 1)) {
            return 1;  // 유효한 조합을 찾으면 즉시 반환
        }
    }
    return 0;  // 유효한 조합을 찾지 못함
}