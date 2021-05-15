from random import randint

sadari = []
roadPosList = [] #가로줄 좌표
a=1
number = 0
num = 0


#사다리 출력
def printSadari(sadari, number):
    num = number * 2 -1
    for row in range(12):
        for col in range(num):
             print(sadari[row][col],end=" ")
        print()
    print()



# 사다리줄에맞게 배열 초기화
def SadariInit(PeopleNum):
    tempsadari = []
    num = PeopleNum*2-1
    for row in range(12):
        tempsadari += [[0]*num]
    tempsadari = SadariVerticalLine(tempsadari, num)
    tempsadari = SadarihorizontalLine(tempsadari, num)

    return tempsadari

#사다리 세로줄 1로 초기화
def SadariVerticalLine(sadari, PeopleNum):
    for row in range(len(sadari)):
        for col in range(0,PeopleNum,2):
            sadari[row][col] = 1

    return sadari



#가로줄 초기화
def SadarihorizontalLine(sadari, PeopleNum):
    num = int((PeopleNum+1)/2)
    a=1
    for t in range(num-1):
        roadPosList.clear()
        roadNumber=0
        roadPos = 0
        roadNumber = randint(1,4)
        while True:
            roadPos = randint(1,10)
            if(not roadPos in roadPosList):
                roadPosList.append(roadPos)
                if len(roadPosList) == roadNumber:
                    break
        for x in roadPosList:
            sadari[x][a] = 1
        a = a+2

    return sadari
