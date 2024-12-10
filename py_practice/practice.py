import random

N = int(input())
print(f"N: {N}")

if not (2 <= N <= 100):
    print("2에서 100사이의 숫자를 입력하세요")
    exit()
    
channels = [input() for _ in range(N)]
print(f"초기 channels: {channels}")
buttons = []
pointer = 0

print("while문 진입 직전")
print(f"조건: {not (channels[0] == 'KBS1' and channels[1] == 'KBS2')}")

while not (channels[0] == 'KBS1' and channels[1] == 'KBS2'):
    print(f"\n현재 상태:")
    print(f"channels: {channels}")
    print(f"pointer: {pointer}")
    print(f"buttons: {buttons}")
    
    # 1. 포인터가 0일 때
    if pointer == 0:
        print("포인터 0 조건 실행")
        if channels[pointer] == 'KBS1':
            if channels[pointer+1] != 'KBS2':
                choice = random.choice([1,3])
                print(f"KBS1 발견, KBS2 아님, 버튼 {choice} 선택")
                if choice == 1:
                    pointer += 1
                    buttons.append(1)
                elif choice == 3:
                    channels[pointer], channels[pointer+1] = channels[pointer+1], channels[pointer]
                    pointer += 1
                    buttons.append(3)
        elif channels[pointer] == 'KBS2':
            print("KBS2 발견, 버튼 3 선택")
            channels[pointer], channels[pointer+1] = channels[pointer+1], channels[pointer]
            pointer += 1
            buttons.append(3)
        elif channels[pointer] != 'KBS1' and channels[pointer] != 'KBS2':
            choice = random.choice([1,3])
            print(f"KBS1/KBS2 아님, 버튼 {choice} 선택")
            if choice == 1:
                pointer += 1
                buttons.append(1)
            elif choice == 3:
                channels[pointer], channels[pointer+1] = channels[pointer+1], channels[pointer]
                pointer += 1
                buttons.append(3)
    
    # 2. 포인터가 1일 때
    elif pointer == 1:
        print("포인터 1 조건 실행")
        if channels[pointer] == 'KBS1':
            print("KBS1 발견, 버튼 4 선택")
            channels[pointer], channels[pointer-1] = channels[pointer-1], channels[pointer]
            pointer -= 1
            buttons.append(4)
        elif channels[pointer] == 'KBS2':
            if channels[pointer-1] != 'KBS1':
                print("KBS2 발견, KBS1 앞에 없음, 버튼 1 선택")
                pointer += 1
                buttons.append(1)
        elif channels[pointer] != 'KBS1' and channels[pointer] != 'KBS2':
            choice = random.choice([1,3])
            print(f"KBS1/KBS2 아님, 버튼 {choice} 선택")
            if choice == 1:
                pointer += 1
                buttons.append(1)
            elif choice == 3:
                channels[pointer], channels[pointer+1] = channels[pointer+1], channels[pointer]
                pointer += 1
                buttons.append(3)
    
    # 3. 포인터가 2 ~ N-2일 때
    elif 2 <= pointer <= N-2:
        print(f"포인터 {pointer} 조건 실행 (2~N-2)")
        if channels[pointer] == 'KBS1' or channels[pointer] == 'KBS2':
            print("KBS1/KBS2 발견, 버튼 4 선택")
            channels[pointer], channels[pointer-1] = channels[pointer-1], channels[pointer]
            pointer -= 1
            buttons.append(4)
        elif channels[pointer] != 'KBS1' and channels[pointer] != 'KBS2':
            choice = random.choice([1,3])
            print(f"KBS1/KBS2 아님, 버튼 {choice} 선택")
            if choice == 1:
                pointer += 1
                buttons.append(1)
            elif choice == 3:
                channels[pointer], channels[pointer+1] = channels[pointer+1], channels[pointer]
                pointer += 1
                buttons.append(3)
    
    # 4. 포인터가 N-1(마지막)일 때
    elif pointer == N-1:
        print(f"포인터 {pointer} 조건 실행 (마지막)")
        if channels[pointer] == 'KBS1' or channels[pointer] == 'KBS2':
            print("KBS1/KBS2 발견, 버튼 4 선택")
            channels[pointer], channels[pointer-1] = channels[pointer-1], channels[pointer]
            pointer -= 1
            buttons.append(4)
        elif channels[pointer] != 'KBS1' and channels[pointer] != 'KBS2':
            print("KBS1/KBS2 아님, 버튼 2 선택")
            pointer -= 1
            buttons.append(2)

print(f"\n최종 결과:")
print(f"channels: {channels}")
print(f"buttons: {''.join(map(str, buttons))}")