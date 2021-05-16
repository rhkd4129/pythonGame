from tkinter import*


#entry의 width = 6은 70px 정도 됨
# 사다리 출력 함수
################################
# PrintSadari(window, ent_num, array):
# window - 최상위 위젯
# ent_num - 인원수
# array - 사다리타기 배열
################################
def PrintSadari(window, ent_num, array):
    window = window
    wid = ((ent_num-1)*100)+70 # 인원수에 따른 캔버스폭 변화
    num = ent_num
    w = Canvas(window, width=wid, height=310) # 캔버스 생성
    w.place(x = 50, y = 60) # 캔버스 위치 조정
    # 세로줄 그리기
    for i in range(ent_num):
        w.create_line(35+i*100, 0, 35+i*100, 310)

    # 가로줄 그리기
    for i in range(1,11):
        for j in range(1,num*2-1,2):
            a = int(j/2)
            if array[i][j] != 1:
                continue
            # x의 35는 entry위젯의 중간좌표
            # *100은 entry위젯 간의 거리
            # 10은 위 아래 약간의 간격
            # 29는 가로줄 사이 간격
            w.create_line(35+a*100, 10+i*29, 35+(a+1)*100, 10+i*29)
