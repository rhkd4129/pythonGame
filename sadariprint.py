from tkinter import*


#entry의 width = 6은 70px 정도 됨
def PrintSadari(window, ent_num, array):
    window = window
    wid = ((ent_num-1)*100)+70
    num = ent_num
    hline = []
    w = Canvas(window, width=wid, height=310)
    w.place(x = 50, y = 60)
    for i in range(ent_num):
        w.create_line(35+i*100, 0, 35+i*100, 310)
    for i in range(1,11):
        for j in range(1,num*2-1,2):
            a = int(j/2)
            if array[i][j] == 0:
                continue
            w.create_line(35+a*100, 10+i*29, 35+(a+1)*100, 10+i*29)
