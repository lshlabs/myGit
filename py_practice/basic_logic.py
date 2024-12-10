
# 1.배열에 입력받기

# 한 줄 입력
s = input()  
# 입력: Hello
# s = "Hello"

# 공백으로 구분된 여러 문자열
s1, s2 = input().split()
# 입력: Hello World
# s1 = "Hello", s2 = "World"

# n줄의 문자열 입력
n = int(input())
strings = [input() for _ in range(n)]
# 입력:
# 3
# apple
# banana
# orange
# strings = ["apple", "banana", "orange"]

# 문자열을 한 글자씩 리스트로
chars = list(input())
# 입력: Hello
# chars = ['H', 'e', 'l', 'l', 'o']

# 한 줄을 단어별로 리스트에 저장
words = input().split()
# 입력: I am a boy
# words = ["I", "am", "a", "boy"]

# 한 줄에 하나씩 입력
n = int(input())  # 입력받을 개수
arr = [int(input()) for _ in range(n)]

# 한 줄에 여러 숫자 입력 (공백으로 구분)
arr = list(map(int, input().split()))

# 예시: 5개 숫자 입력
# 입력: 1 2 3 4 5
numbers = list(map(int, input().split()))


########################################################

# 2. nCr 조합 구하기

from itertools import combinations

arr = [1, 2, 3, 4, 5]
r = 3

# 5C3 구하기
combs = list(combinations(arr, r))
print(combs)  # [(1,2,3), (1,2,4), (1,2,5), ...]

########################################################

# 3. 배열 정렬하기

arr = [5, 2, 3, 1, 4]

# 오름차순
arr.sort()  # 원본 배열 정렬
sorted_arr = sorted(arr)  # 새로운 배열 반환

# 내림차순
arr.sort(reverse=True)  # 원본 배열 정렬
sorted_arr = sorted(arr, reverse=True)  # 새로운 배열 반환

########################################################

# 4. 배열 관련 유용한 함수들:

arr = [1, 2, 3, 4, 5]

# 길이
length = len(arr)

# 합계
total = sum(arr)

# 최대/최소
max_val = max(arr)
min_val = min(arr)

# 특정 값의 인덱스
idx = arr.index(3)  # 값 3의 위치

# 배열 추가/삭제
arr.append(6)      # 끝에 추가
arr.insert(0, 0)   # 특정 위치에 추가
arr.pop()          # 마지막 요소 제거
arr.remove(3)      # 특정 값 제거

########################################################

# 5. 랜덤 숫자 생성

import random

# 0부터 9까지 랜덤 숫자
num = random.randint(0, 9)

# 1부터 10까지 랜덤 숫자
num = random.randint(1, 10)

# 리스트에서 랜덤 선택
arr = [1, 2, 3, 4, 5]
random_choice = random.choice(arr)

########################################################

# 6. 조건문과 프로그램 종료:

def check_number(n):
    if n <= 0:
        return False    # 함수 종료
    return True

# 사용 예시
def solution(numbers):
    if not numbers:    # 빈 리스트 체크
        return 0       # 함수 종료
    
    result = sum(numbers)
    return result      # 결과 반환

import sys

n = int(input())
if n <= 0:
    print("양수를 입력하세요")
    sys.exit(0)    # 프로그램 종료

# 로직 처리
print("프로그램 종료")