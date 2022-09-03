from tkinter import *
from tkinter.messagebox import *

mp = [[0 for i in range(19)] for j in range(19)]
rd = 1

def main():
    win = Tk()
    win.resizable(0, 0)
    win.geometry("+200+20")
    win.title("五子棋 V1.0.2 -- By lanlan2_")
    win.iconbitmap("icon.ico")
    win.config(bg="aliceblue")

    can = Canvas(win, height=780, width=780, borderwidth=0, relief=FLAT, bg="lightgrey")
    can.config(highlightthickness=0)

    for i in range(18):
        for j in range(18):
            can.create_rectangle(j*40+30, i*40+30, j*40+70, i*40+70, fill="GoldenRod", outline="black")
    for m in range(3):
        for n in range(3):
            can.create_oval(240*n+147, 240*m+147, 240*n+153, 240*m+153, fill="Black", outline="black")
    can.pack()

    def judge(a, b):
        global rd
        tr = 2 - rd % 2
        c1 = c2 = c3 = c4 = 0
        
        #横向
        for i in range(b-4, b+6):
            if c1 == 5:
                return 1
            else:
                if i <= 18 and i >= 0:
                    if mp[a][i] == tr:
                        c1 += 1
                    else:
                        c1 = 0
        #纵向                
        for i in range(a-4, a+6):
            if c2 == 5:
                return 1
            else:
                if i <= 18 and i >= 0:
                    if mp[i][b] == tr:
                        c2 += 1
                    else:
                        c2 = 0
        #左上——右下
        for i, j in zip(range(a-4, a+6), range(b-4, b+6)):
            if c3 == 5:
                return 1
            else:
                if i <= 18 and i >= 0 and j <= 18 and j >= 0:
                    if mp[i][j] == tr:
                        c3 += 1
                    else:
                        c3 = 0
        #右上——左下
        for i, j in zip(range(a-4, a+6), range(b+4, b-6, -1)):
            if c4 == 5:
                return 1
            else:
                if i <= 18 and i >= 0 and j <= 18 and j >= 0:
                    if mp[i][j] == tr:
                        c4 += 1
                    else:
                        c4 = 0
                        
    def luozi(event):
        global rd
        if event.x > 770 or event.x < 10 or event.y < 10 or event.y > 770:
            return
        else:
            x = int((event.x - 10) // 40)
            y = int((event.y - 10) // 40)
            if mp[y][x] == 0:
                if rd % 2 == 1:
                    mp[y][x] = 1
                    can.create_oval(int(x*40+10), int(y*40+10), int(x*40+50), int(y*40+50), fill="black")
                else:
                    mp[y][x] = 2
                    can.create_oval(int(x*40+10), int(y*40+10), int(x*40+50), int(y*40+50), fill="white", outline="white")
                over = judge(y, x)
                if over == 1:
                    if rd % 2 == 1:
                        showinfo("提示", "黑方获胜！")
                    else:
                        showinfo("提示", "白方获胜！")
                    can.unbind("<Button-1>")
                else:
                    rd += 1
                    
    can.bind("<Button-1>", luozi)
    win.mainloop()

if __name__ == "__main__":
    main()
