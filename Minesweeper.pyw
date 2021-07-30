import tkinter as tk
import time
import random
import tkinter.messagebox
# Minesweeper V1.1 by Calin Novogreblevschi
def startgame2():
    global sizetitle
    global sizelabel
    global sizescale
    global minelabel
    global minescale
    global configurebutton
    global start1
    start1 = False
    board_y = []
    board = []
    rulex = [-1,0,1,-1,1,-1,0,1]
    ruley = [-1,-1,-1,0,0,1,1,1]
    for x in range(size):     #Maps out the board
        for y in range(size):
            board_y.append(" ")
        board.append(board_y)
        board_y = []
    """
    for i in range(mines):      #Generates the coordinates for the mines
        found = False
        while found == False:
            random_x = random.randint(0,size-1)
            random_y = random.randint(0,size-1)
            if (board[random_x])[random_y] == " ":
                (board[random_x])[random_y] = "X"
                found = True
    
    for x in range(size):
        for y in range(size): #Maps out the numbers around the mines
            if (board[x])[y] == " ":
                mine_counter = 0
                for i in range(0,8):
                    if (x+(rulex[i]) >= 0) and (y+(ruley[i]) >= 0) and (x+(rulex[i]) <= (size-1)) and (y+(ruley[i]) <= (size-1)):
                        if (board[x+(rulex[i])])[y+(ruley[i])]  == "X":
                            mine_counter += 1

                if mine_counter == 0:
                    mine_counter = " "
                (board[x])[y] = str(mine_counter)
    """
    title = tk.Label(root, text= "Minesweeper", font=("Arial", 20))
    title.pack()
    def left(x,y):
        global start1
        if start1 == True:
            if (buttons[x])[y]['text'] != "F":
                found = []
                (buttons[x])[y].config(state=tk.DISABLED,relief= tk.SUNKEN,activeforeground="red",fg="black",text=(board[x])[y])
                if (board[x])[y] == " ":
                    for i in range(0,8):
                        if (x+(rulex[i]) >= 0) and (y+(ruley[i]) >= 0) and (x+(rulex[i]) <= (size-1)) and (y+(ruley[i]) <= (size-1)):
                            if (board[x+(rulex[i])])[y+(ruley[i])]  != "X":
                                if (buttons[x+(rulex[i])])[y+(ruley[i])]['text'] == "F":
                                    mine_counter = int(mineleft_label['text'][10:-12])
                                    mine_counter += 1
                                    mineleft_label.config(text="There are "+str(mine_counter)+" mines left.")
                                (buttons[x+(rulex[i])])[y+(ruley[i])].config(fg="black",state=tk.DISABLED,relief= tk.SUNKEN,text=str((board[x+(rulex[i])])[y+(ruley[i])]))
                                if (board[x+(rulex[i])])[y+(ruley[i])]  == " ":
                                    if (buttons[x+rulex[i]])[y+(ruley[i])]['activeforeground'] != "red":
                                        found.append([x+(rulex[i]),y+(ruley[i])])

                    for i in range(len(found)):
                        l = left(found[i][0],found[i][1])
                elif (board[x])[y] == "X":
                    #Game lost
                    for x1 in range(size):
                        for y1 in range(size):
                            if (board[x1])[y1] == "X":
                                if (buttons[x1])[y1]['text'] == "F":
                                    (buttons[x1])[y1].config(fg="green",text="X")
                                else:
                                    (buttons[x1])[y1].config(fg="red",text=str((board[x1])[y1]))
                    tk.messagebox.showinfo(title="Game lost",message="You lost the game!")
                    root.destroy()
                    title = ""
                    start_button = ""
                    beginning()
                else:
                    win = True
                    for x1 in range(size): #Checks for win
                        for y1 in range(size):
                            if (board[x1])[y1] == "X":
                                if (buttons[x1])[y1]['text'] != "F":
                                    win = False
                            else:
                                if (buttons[x1])[y1]['state'] == tk.NORMAL:
                                    win = False
                    if win == True:
                        tk.messagebox.showinfo(title="Game won!",message="You won the game!")
                        root.destroy()
                        title = ""
                        start_button = ""
                        beginning()
                #if (buttons[x])[y]['text'] != tk.:
        else:
            start1 = True
            for i in range(mines):      #Generates the coordinates for the mines
                found = False
                while found == False:
                    random_x = random.randint(0,size-1)
                    random_y = random.randint(0,size-1)
                    if (board[random_x])[random_y] == " ":
                        if (random_x != x) and (random_y != y):
                            (board[random_x])[random_y] = "X"
                            found = True
    
            for x1 in range(size):
                for y1 in range(size): #Maps out the numbers around the mines
                    if (board[x1])[y1] == " ":
                        mine_counter = 0
                        for i in range(0,8):
                            if (x1+(rulex[i]) >= 0) and (y1+(ruley[i]) >= 0) and (x1+(rulex[i]) <= (size-1)) and (y1+(ruley[i]) <= (size-1)):
                                if (board[x1+(rulex[i])])[y1+(ruley[i])]  == "X":
                                    mine_counter += 1

                        if mine_counter == 0:
                            mine_counter = " "
                        (board[x1])[y1] = str(mine_counter)
            found = []
            (buttons[x])[y].config(state=tk.DISABLED,relief= tk.SUNKEN,activeforeground="red",fg="black",text=(board[x])[y])
            if (board[x])[y] == " ":
                for i in range(0,8):
                    if (x+(rulex[i]) >= 0) and (y+(ruley[i]) >= 0) and (x+(rulex[i]) <= (size-1)) and (y+(ruley[i]) <= (size-1)):
                        if (board[x+(rulex[i])])[y+(ruley[i])]  != "X":
                            if (buttons[x+(rulex[i])])[y+(ruley[i])]['text'] == "F":
                                mine_counter = int(mineleft_label['text'][10:-12])
                                mine_counter += 1
                                mineleft_label.config(text="There are "+str(mine_counter)+" mines left.")
                            (buttons[x+(rulex[i])])[y+(ruley[i])].config(fg="black",state=tk.DISABLED,relief= tk.SUNKEN,text=str((board[x+(rulex[i])])[y+(ruley[i])]))
                            if (board[x+(rulex[i])])[y+(ruley[i])]  == " ":
                                if (buttons[x+rulex[i]])[y+(ruley[i])]['activeforeground'] != "red":
                                    found.append([x+(rulex[i]),y+(ruley[i])])

                for i in range(len(found)):
                    l = left(found[i][0],found[i][1])
    def right(x,y):
        mine_counter2 = int(mineleft_label['text'][10:-12])
        if (buttons[x])[y]['state'] != tk.DISABLED:
            if (buttons[x])[y]['text'] != "F":
                (buttons[x])[y].config(fg="red",text="F")
                mine_counter2 = mine_counter2-1
            else:
                (buttons[x])[y].config(state=tk.NORMAL,relief= tk.RAISED,fg="black",text="  ")
                mine_counter2 += 1
        mineleft_label.config(text="There are "+str(mine_counter2)+" mines left.")
        win = True
        for x1 in range(size): #Checks for win
            for y1 in range(size):
                if (board[x1])[y1] == "X":
                    if (buttons[x1])[y1]['text'] != "F":
                        win = False
                else:
                    if (buttons[x1])[y1]['state'] == tk.NORMAL:
                        win = False
        if win == True:
            tk.messagebox.showinfo(title="Game won!",message="You won the game!")
            root.destroy()
            title = ""
            start_button = ""
            beginning()
    def back():
        result = tk.messagebox.askquestion(title="Exit game?",message="Are you sure you want to end your current session?", icon='warning')
        if result == 'yes':
            root.destroy()
            beginning()
    length = str(200+((size-5)*20))
    width = str(300+((size-5)*28))
    sum = length+'x'+width
    root.geometry(sum)
    buttons=[]
    buttons_y = []
    for x in range(size):     #Maps out the board
        for y in range(size):
            buttons_y.append(" ")
        buttons.append(buttons_y)
        buttons_y = []
    
    mineleft_label = tk.Label(root,text="There are "+str(mines)+" mines left.")
    mineleft_label.pack()
    back_button = tk.Button(master=root, text="Back", command=back)
    xsize = 10+(size-5)
    back_button.place(x=xsize,y=25)
    for x in range(size):
        for y in range(size):
            (buttons[x])[y]=(tk.Button(master=root, text="  "))
            (buttons[x])[y].place(x=((20*x)+50),y=(30*y)+80)
            (buttons[x])[y].bind('<Button-1>', lambda event, x=x, y=y: left(x,y))
            (buttons[x])[y].bind('<Button-2>', lambda event, x=x, y=y: right(x,y))
            (buttons[x])[y].bind('<Button-3>', lambda event, x=x, y=y: right(x,y))
            #button.bind('<Button-3>', right)
    
def start():
    global sizetitle
    global sizelabel
    global sizescale
    global minelabel
    global minescale
    global configurebutton
    title.destroy()

    def update(l):
        scale = int(sizescale.get())
        area = (scale*scale)*0.65
        minimum= 0.05*(scale*scale)
        length = round((1/30)*area)
        middle = round(0.2*(scale*scale))
        minescale.config(from_=minimum,to=area, tickinterval=length)
        minescale.set(middle)
    def update2(l):
        scale = int(sizescale.get())
        area = scale*scale
        mines = int(minescale.get())
        percent = str((round(mines/area,3))*100)
        try:
            percent = percent[0]+percent[1]+percent[2]+percent[3]
        except:
            percent = percent[0]+percent[1]+percent[2]
        textlabel = "Select the number of mines on the board: ("+percent+"% of board)"
        minelabel.config(text=textlabel)
    def startgame():
        global size
        global mines
        size = int(sizescale.get())
        mines = int(minescale.get())
        sizetitle.destroy()
        sizelabel.destroy()
        sizescale.destroy()
        minelabel.destroy()
        minescale.destroy()
        configurebutton.destroy()
        startgame2()
    start_button.destroy()
    sizetitle = tk.Label(root, text="Select configuration:", font=("Arial", 20))
    sizetitle.pack()
    sizelabel = tk.Label(root, text="Select size of the board (length):", font=("Arial", 10))
    sizelabel.pack()
    sizescale = tk.Scale(root, from_=10, to=25, orient=tk.HORIZONTAL, tickinterval=1, length=600, command=update)
    sizescale.pack()
    minelabel = tk.Label(root, text="Select the number of mines on the board: (30% of board)", font=("Arial", 10))
    minelabel.pack()
    scale = int(sizescale.get())
    area = (scale*scale)*0.65
    length = round((1/30)*area)
    minescale = tk.Scale(root, from_=5, to=area, orient=tk.HORIZONTAL, tickinterval=length, length=600, command=update2 )
    minescale.set(round(0.2*(scale*scale)))
    minescale.pack()
    configurebutton = tk.Button(root, text="Configure", command=startgame)
    configurebutton.pack()
    
def beginning():
    global title
    global start_button
    global root
    root = tk.Tk()
    root.geometry('800x600')
    root.title("Minesweeper V1.1 by Calin Novogreblevschi")
    #root.state('zoomed')
    root.resizable(0, 0)
    title = tk.Label(root, text= "Minesweeper", font=("Arial", 20))
    title.place(relx=0.395, rely=0)
    start_button = tk.Button(root, text="Start",command=start, padx=10, pady = 10)
    start_button.place(relx=0.475,rely=0.3)
beginning()




root.mainloop()


