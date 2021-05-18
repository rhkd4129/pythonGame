from tkinter import*


# 사다리 세로줄 출력 함수
###############################
# PrintVline(canvas, ent_num)
# canvas - 그려지는 캔버스
# ent_num - 인원수
###############################
def PrintVline(canvas, ent_num):
    c = canvas
    num = ent_num
    for i in range(ent_num):
        c.create_line(35+i*100, 0, 35+i*100, 310)

#entry의 width = 6은 70px 정도 됨
# 사다리 출력 함수
################################
# PrintSadari(window, ent_num, array):
# window - 최상위 위젯
# ent_num - 인원수
# array - 사다리타기 배열
################################
def PrintSadari(canvas, ent_num, array):
    c = canvas
    num = ent_num
    # 세로줄 그리기
    PrintVline(c,num)

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
            c.create_line(35+a*100, 10+i*29, 35+(a+1)*100, 10+i*29)
