from random import randint

num = int(input("개수 입력"))
number = (num*2)-1


sadari = []
roadPosList = [] #가로줄 좌표
a=1


#사다리 출력
def printSadari():
    for row in range(12):
        for col in range(number):
                         print(sadari[row][col],end=" ")
        print()

        

# 사다리줄에맞게 배열 초기화
for row in range(12):
        sadari += [[0]*number]

#사다리 세로줄 1로 초기화
for row in range(len(sadari)):
    for col in range(0,number,2):
            sadari[row][col] = 1



#가로줄 초기화
for t in range(num-1):
        roadPosList.clear()
        roadNumber=0
        roadPos = 0
        roadNumber = randint(1,4)
        while True:
            roadPos = randint(2,10)
            if(not roadPos in roadPosList):
                roadPosList.append(roadPos)
                if len(roadPosList) == roadNumber:
                    break
        for x in roadPosList:
            sadari[x][a] = 1
        a = a+2
      

printSadari()
