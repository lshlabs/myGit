#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <math.h>

#define MAX_TEAMS 4
#define MAX_MATCHES 6
#define MAX_CASES 729  // 3^6

struct case_score {
    double points[MAX_TEAMS];
    double probability;
};

int findTeamIndex(char teamNames[MAX_TEAMS][10], const char* name) {
    for(int i = 0; i < MAX_TEAMS; i++) {
        if(strcmp(teamNames[i], name) == 0) return i;
    }
    return -1;
}

int main() {
    char teamNames[MAX_TEAMS][10];
    struct case_score* cases = malloc(sizeof(struct case_score) * MAX_CASES);
    if(cases == NULL) return 1;
    
    int caseCount = 1;
    double finalProb[MAX_TEAMS] = {0};
    
    // 팀 이름 입력
    for(int i = 0; i < MAX_TEAMS; i++) {
        scanf("%s", teamNames[i]);
    }
    
    // 첫 번째 경우 초기화
    for(int i = 0; i < MAX_TEAMS; i++) {
        cases[0].points[i] = 0;
    }
    cases[0].probability = 1.0;
    
    // 6개 경기 처리
    for(int match = 0; match < MAX_MATCHES; match++) {
        char teamA[10], teamB[10];
        double winA, draw, winB;
        scanf("%s %s %lf %lf %lf", teamA, teamB, &winA, &draw, &winB);
        
        struct case_score* newCases = malloc(sizeof(struct case_score) * MAX_CASES);
        if(newCases == NULL) {
            free(cases);
            return 1;
        }
        
        int newCaseCount = 0;
        int idxA = findTeamIndex(teamNames, teamA);
        int idxB = findTeamIndex(teamNames, teamB);
        
        for(int c = 0; c < caseCount; c++) {
            // A팀 승리
            if(winA > 0) {
                memcpy(&newCases[newCaseCount], &cases[c], sizeof(struct case_score));
                newCases[newCaseCount].points[idxA] += 3;
                newCases[newCaseCount].probability = cases[c].probability * winA;
                newCaseCount++;
            }
            
            // 무승부
            if(draw > 0) {
                memcpy(&newCases[newCaseCount], &cases[c], sizeof(struct case_score));
                newCases[newCaseCount].points[idxA] += 1;
                newCases[newCaseCount].points[idxB] += 1;
                newCases[newCaseCount].probability = cases[c].probability * draw;
                newCaseCount++;
            }
            
            // B팀 승리
            if(winB > 0) {
                memcpy(&newCases[newCaseCount], &cases[c], sizeof(struct case_score));
                newCases[newCaseCount].points[idxB] += 3;
                newCases[newCaseCount].probability = cases[c].probability * winB;
                newCaseCount++;
            }
        }
        
        free(cases);
        cases = newCases;
        caseCount = newCaseCount;
    }
    
    // 각 경우의 확률 계산
    for(int i = 0; i < caseCount; i++) {
        double sortedPoints[MAX_TEAMS];
        int indices[MAX_TEAMS];
        
        for(int j = 0; j < MAX_TEAMS; j++) {
            sortedPoints[j] = cases[i].points[j];
            indices[j] = j;
        }
        
        // 내림차순 정렬
        for(int j = 0; j < MAX_TEAMS-1; j++) {
            for(int k = j+1; k < MAX_TEAMS; k++) {
                if(sortedPoints[j] < sortedPoints[k]) {
                    double tempPoint = sortedPoints[j];
                    sortedPoints[j] = sortedPoints[k];
                    sortedPoints[k] = tempPoint;
                    
                    int tempIdx = indices[j];
                    indices[j] = indices[k];
                    indices[k] = tempIdx;
                }
            }
        }
        
        // 1등 동점자 수 확인
        int topCount = 1;
        for(int j = 1; j < MAX_TEAMS; j++) {
            if(fabs(sortedPoints[j] - sortedPoints[0]) < 1e-9) {
                topCount++;
            }
        }
        
        if(topCount >= 2) {
            // 동점자 중 2팀 선택
            double selectProb = 2.0 / topCount;
            for(int j = 0; j < topCount; j++) {
                finalProb[indices[j]] += cases[i].probability * selectProb;
            }
        } else {
            // 1등은 확정
            finalProb[indices[0]] += cases[i].probability;
            
            // 2등 동점자 확인
            int secondCount = 1;
            for(int j = 2; j < MAX_TEAMS; j++) {
                if(fabs(sortedPoints[j] - sortedPoints[1]) < 1e-9) {
                    secondCount++;
                }
            }
            
            // 2등 동점자 중 1팀 선택
            double selectProb = 1.0 / secondCount;
            for(int j = 1; j < 1 + secondCount; j++) {
                finalProb[indices[j]] += cases[i].probability * selectProb;
            }
        }
    }
    
    // 결과 출력
    for(int i = 0; i < MAX_TEAMS; i++) {
        printf("%.10lf\n", finalProb[i]);
    }
    
    free(cases);
    return 0;
}