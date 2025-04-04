# 시간 관리 매서드 구현
# 1. _active_mode.py에서 배민인지 요기요인지 받아옴.
# 2. 배민의 배달 기본 설정시간은 50분, 포장 기본 설정시간은 15분
# 3. 요기요의 배달 기본 설정시간은 50분, 포장 기본 설정시간은 20분
# 4. image_finder를 사용하여 data에 저장된 배민/요기요의 roi영역 내에서 img폴더의 plus/minus 이미지를 찾음.
# 5. 예시로 data.json에 저장된 배민 배달시간이 40분이라면 기본 설정시간이 50분 이므로 10분을 조정해야함.
# 6. 시간은 5분단위로 조정되므로 찾은 탬플릿을 2번 클릭하여 조정해야함. (50분 -> 40분)
# 7. 탬플릿의 좌표와 클릭횟수를 _active_mode.py에 전달함.
# 8. 포장시간 조정은 추후에 추가예정