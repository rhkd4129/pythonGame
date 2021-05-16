from random import randint

sadari = []
roadPosList = [] #가로줄 좌표
a=1
number = 0
num = 0


#사다리 콘솔 출력
#############################
# printSadari(sadari, number):
# sadari - 사다리 배열
# number - 인원수
#############################
def printSadari(sadari, number):
    num = number * 2 -1
    for row in range(12):
        for col in range(num):
             print(sadari[row][col],end=" ")
        print()
    print()



# 사다리 배열 값 설정
##############################
# SadariInit(PeopleNum):
# PeopleNum - 인원수
# 반환값 - 완성된 사다리 배열
##############################
def SadariInit(PeopleNum):
    tempsadari = []
    num = PeopleNum*2-1
    # 사다리 배열 0으로 초기화
    for row in range(12):
        tempsadari += [[0]*num]
    tempsadari = SadariVerticalLine(tempsadari, num)
    tempsadari = SadarihorizontalLine(tempsadari, num)

    return tempsadari


#사다리 세로줄 1로 초기화
#############################
# SadariVerticalLine(sadari, PeopleNum):
# sadari - 설정중인 사다리 배열
# PeopleNum - 인원수
# 반환값 - 세로줄 설정된 사다리 배열
#############################
def SadariVerticalLine(sadari, PeopleNum):
    for row in range(len(sadari)):
        for col in range(0,PeopleNum,2):
            sadari[row][col] = 1

    return sadari



#가로줄 초기화
###############################
# SadarihorizontalLine(sadari, PeopleNum):
# sadari - 설정중인 사다리 배열
# PeopleNum - 인원수
# 반환값 - 가로줄 설정된 사다리 배열
###############################
def SadarihorizontalLine(sadari, PeopleNum):
    num = int((PeopleNum+1)/2) # 인원수
    a=1
    for t in range(num-1):
        roadPosList.clear()
        roadNumber=0
        roadPos = 0
        roadNumber = randint(1,4)
        while True:
            roadPos = randint(1,10)
            if(not roadPos in roadPosList):
                # 설정할 좌표에 중복표시가 있으면 건너 뜀
                if(sadari[roadPos][a] == 2):
                    print("pass")
                    continue
                # 중복표시가 없을때만 좌표리스트에 추가
                roadPosList.append(roadPos)
                if len(roadPosList) == roadNumber:
                    break
        for x in roadPosList:
            sadari[x][a] = 1
        # 중복 확인을 위해 다음줄 같은 라인에 2로 표시
        for x in roadPosList:
            if(a<PeopleNum - 2):
                sadari[x][a+2] = 2

        # 사다리 확인하기
        # for i in sadari:
        #     print(i)
        # print()
        a = a+2

    return sadari
