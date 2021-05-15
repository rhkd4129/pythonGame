from random import randint
import tkinter
from tkinter import ttk

#전역변수 자리
sadari = []
roadPosList = [] #가로줄 좌표
a=1
number = 0
num = 0


#사다리 출력
def printSadari(sadari, number):
    for row in range(12):
        for col in range(number):
             print(sadari[row][col],end=" ")
        print()



# 사다리줄에맞게 배열 초기화
def SadariInit(number):
    tempsadari = []
    for row in range(12):
        tempsadari += [[0]*number]
    tempsadari = SadariVerticalLine(tempsadari, number)
    tempsadari = SadarihorizontalLine(tempsadari, number)

    return tempsadari

#사다리 세로줄 1로 초기화
def SadariVerticalLine(sadari, number):
    for row in range(len(sadari)):
        for col in range(0,number,2):
            sadari[row][col] = 1

    return sadari



#가로줄 초기화
def SadarihorizontalLine(sadari, number):
    num = int((number+1)/2)
    a=1
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

    return sadari

#다시 만들어야 함
class MainWindow:
    def __init__(self):
        self.window = tkinter.Tk()
        self.window.title("sagari Game")
        self.window.geometry("1200x600")
        self.window.resizable(False, False)
        self.firstwindow = FirstWindow(self.window, self)
        self.firstwindowlist = self.firstwindow.ListReturn()
        self.secondwindow = SecondWindow(self.window)
        self.secondwindowlist = []
        self.thirdwindow = ThirdWindow()
        self.thirdwindowlist = []
        self.window.mainloop()
    def SecondWindowListMake(self):
        self.secondwindowlist = self.secondwindow.ListReturn()

class FirstWindow(MainWindow):
    num = 0
    number = 0
    def __init__(self, window, controll):
        self.window = window
        self.controll = controll
        self.label = ttk.Label(self.window, text="인원수")
        self.label.grid(column=0, row=0)

        self.button = ttk.Button(self.window, text="확인", command=self.ButtonClick)
        self.button.grid(column=1,row=1)

        self.PeopleNum = tkinter.StringVar()
        self.textbox = ttk.Entry(self.window, width=12, textvariable=self.PeopleNum)
        self.textbox.grid(column=0, row=1)

        self.labelNew = ttk.Label(self.window, text="")
        self.labelNew.grid(column=1,row=2)
        self.firstwindowlist = [self.label, self.button, self.textbox, self.labelNew]

    def ListReturn(self):
        return self.firstwindowlist

    def ButtonClick(self):
        global sadari
        global num
        num = int(self.PeopleNum.get())
        number = (num*2)-1
        sadari = SadariInit(number)
        printSadari(sadari, number)
        self.button.grid_forget()
        self.textbox.grid_forget()
        self.labelNew.grid_forget()
        self.label.grid_forget()
        self.controll.SecondWindowListMake()


class SecondWindow(MainWindow):
    global num
    def __init__(self, window):
        self.test = 0
        self.num = num
        self.window = window
        self.list = []
    def test(self):
        self.test = 2
        print(self.test)
    def ListReturn(self):
        self.num = num
        self.list = [0]*self.num*2
        for i in range(0,self.num*2):
            self.list[i] = ttk.Entry(self.window, width=12, text="인원수")
            if i<12:
                self.list[i].grid(column = i, row=0)
            else:
                self.list[i].grid(column = i-12, row=2)

            print(i)

        print(self.list)
        return self.list


class ThirdWindow(MainWindow):
    def __init__(self):
        self.test = 0
    def test(self):
        self.test = 3
        print(self.test)

mainwindow = MainWindow()
