#include <stdio.h>
#include <string.h>

// 1-9 프레임 계산 함수
int calculateNormalFrame(const char* input, int* index) {
    int frameScore = 0;
    
    // 스트라이크인 경우
    if (input[*index] == 'S') {
        frameScore += 10;
        
        // 다음 두 투구의 보너스
        if (input[*index + 1]) {  // 첫 번째 보너스
            if (input[*index + 1] == 'S') frameScore += 10;
            else if (input[*index + 1] == '-') frameScore += 0;
            else frameScore += (input[*index + 1] - '0');
        }
        
        if (input[*index + 2]) {  // 두 번째 보너스
            if (input[*index + 2] == 'S') frameScore += 10;
            else if (input[*index + 2] == 'P') 
                frameScore += (10 - (input[*index + 1] == '-' ? 0 : input[*index + 1] - '0'));
            else if (input[*index + 2] == '-') frameScore += 0;
            else frameScore += (input[*index + 2] - '0');
        }
        (*index)++;
    }
    // 스페어인 경우
    else if (input[*index + 1] == 'P') {
        frameScore += 10;
        
        // 다음 한 투구의 보너스
        if (input[*index + 2]) {
            if (input[*index + 2] == 'S') frameScore += 10;
            else if (input[*index + 2] == '-') frameScore += 0;
            else frameScore += (input[*index + 2] - '0');
        }
        *index += 2;
    }
    // 일반 점수인 경우
    else {
        frameScore += (input[*index] == '-' ? 0 : input[*index] - '0');
        frameScore += (input[*index + 1] == '-' ? 0 : input[*index + 1] - '0');
        *index += 2;
    }
    
    return frameScore;
}

// 10번째 프레임 계산 함수
int calculateLastFrame(const char* input, int index) {
    int lastScore = 0;
    
    // 스트라이크인 경우
    if (input[index] == 'S') {
        lastScore += 10;
        
        // 두 번의 추가 투구
        if (input[index + 1] == 'S') lastScore += 10;
        else if (input[index + 1] == '-') lastScore += 0;
        else lastScore += (input[index + 1] - '0');
        
        if (input[index + 2] == 'S') lastScore += 10;
        else if (input[index + 2] == 'P') 
            lastScore += (10 - (input[index + 1] == '-' ? 0 : input[index + 1] - '0'));
        else if (input[index + 2] == '-') lastScore += 0;
        else lastScore += (input[index + 2] - '0');
    }
    // 스페어인 경우
    else if (input[index + 1] == 'P') {
        lastScore += 10;
        
        // 한 번의 추가 투구
        if (input[index + 2] == 'S') lastScore += 10;
        else if (input[index + 2] == '-') lastScore += 0;
        else lastScore += (input[index + 2] - '0');
    }
    // 일반 점수인 경우
    else {
        lastScore += (input[index] == '-' ? 0 : input[index] - '0');
        lastScore += (input[index + 1] == '-' ? 0 : input[index + 1] - '0');
    }
    
    return lastScore;
}

// 전체 점수 계산 함수
int calculateScore(const char* input) {
    int score = 0;
    int frame = 0;
    int index = 0;

    // 1-9 프레임 계산
    while (frame < 9 && input[index]) {
        score += calculateNormalFrame(input, &index);
        frame++;
    }

    // 10번째 프레임 계산
    if (input[index]) {
        score += calculateLastFrame(input, index);
    }

    return score;
}

int main() {
    char input[30];
    
    printf("볼링 점수를 입력하세요: ");
    scanf("%29s", input);

    int totalScore = calculateScore(input);
    printf("총 점수: %d\n", totalScore);

    return 0;
}