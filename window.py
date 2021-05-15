from tkinter import*

# pack(side =  "top",left,right,bottom,   padx = 20, pady 20)
# grid(column =0,row = 2)       gird(column = 2,row -0,rowspan =2 // columnspan = 2)
# place(x = 20, y =29// relx = 0.3 rely = 0.4 상대적 위치)

main = Tk()
main.title("window")

# 창안에 위젯들 삭제 
def Clear():
  for w in main.place_slaves():
      w.destroy()

    
def GOClick():
  global ent_num
  ent_num = int(ent.get())
  Clear()
  main.geometry("800x500")   
  main.option_add("*Font","맑은고딕 15")
  a=1
  
  for i in range(ent_num):
        i = Entry(main)
        i.place(x = 50*a,y =35)
        i.config(width = 6)
        a +=2
  a=1
  for i in range(ent_num):
        i = Entry(main)
        i.place(x = 50*a,y =370)
        i.config(width = 6)
        a +=2
  PlayBtn()
  BackBtn()


  

def PlayBtn():
  Playbtn = Button(main)
  Playbtn.config(text = "Play")
  Playbtn.place(x=50 , y = 450)
  Playbtn.config(command = PlayClick)

def BackBtn():
  Backbtn = Button(main)
  Backbtn.config(text = "Back")
  Backbtn.place(x = 120 , y = 450)
  Backbtn.config(command = BackClick)


  
def PlayClick():
  entList=[]
  for x  in main.place_slaves():
    entList.append(x)
  Clear()  
  main.geometry("800x400")
  for x in entList:
    x = Label(main)
    x.config(text = x)
    x.pack()


def BackClick():
  
  Clear()
  mainWindow()


def mainWindow():
  main.geometry("400x400")
  main.option_add("*Font","맑은고딕 20")

  lab = Label(main)
  lab.config(text = "개수입력")
  lab.place(x = 145, y= 50)

  global ent
  ent = Entry(main)
  ent.place(x = 40, y= 80)


  GObtn = Button(main)
  GObtn.config(text="GO")
  GObtn.place(x = 160, y= 120)
  GObtn.config(command = GOClick)










mainWindow()


main.mainloop()
