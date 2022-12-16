import tkinter as tk
from tkinter.messagebox import showinfo, showerror
import time


class mybutton(tk.Button):
    def __init__(self, master, x, y, number=0, *args, **kwargs):
        super(mybutton, self).__init__(master, font = 'Calibri 15 bold', *args, **kwargs)
        self.x = x
        self.y = y
        self.number = number
        self.count_neib = 0
        self.is_alive = False
    def __repr__(self):
        return f'MyButton {self.x} {self.y} {self.number} {self.is_mine}'
class game:
    window = tk.Tk()
    row = 50
    col = 50
    mines = 25
    IS_GAME_OVER = False
    is_first_click = True
    cells_map = []
    surv = 0
    def __init__(self):
        self.buttons = []
        for i in range (game.row+2):
            temp=[]
            for j in range (game.col+2):
                btn = mybutton(game.window, x=i, y=j, width=3)
                btn.config(command=lambda button=btn: self.click(button))
                temp.append(btn)
            self.buttons.append(temp)


    def click(self, clicked_button:mybutton):

        if not clicked_button.is_alive:
            clicked_button.config(background = 'black', disabledforeground ='black')
            clicked_button.is_alive = True
            game.surv = game.surv + 1
                

        else:
            clicked_button.config(background = 'white', disabledforeground ='white')
            clicked_button.is_alive = False
            game.surv = game.surv - 1

#        print(clicked_button)
#        if clicked_button.is_mine:
#            clicked_button.config(text="*", background = 'red', disabledforeground ='black')
#            clicked_button.is_open = True
#            game.IS_GAME_OVER = True
#            showinfo('Game over', 'Вы проиграли')
#            for i in range(1, game.row + 1):
#                for j in range(1, game.col + 1):
#                    btn = self.buttons[i][j]
#                    if btn.is_mine:
#                        btn['text'] = '*'
#        else:
#                            
#            color = colors.get(clicked_button.count_bomb, 'black')
#            if clicked_button.count_bomb:
#                clicked_button.config(text=clicked_button.count_bomb, disabledforeground = color)
#                clicked_button.is_open = True
#            else:
#                self.breadth_first_search(clicked_button)
#        clicked_button.config(state = 'disabled')
#        clicked_button.config(relief=tk.SUNKEN)



    def create_wigets(self):


        menubar = tk.Menu(self.window)
        self.window.config(menu = menubar)

        settings_menu = tk.Menu(menubar, tearoff = 0)
        settings_menu.add_command(label = 'Начало игры', command = self.start_game)
        settings_menu.add_command(label = 'Перезагрузка', command = self.reload)
        settings_menu.add_command(label = 'Выход', command = self.window.destroy)
        menubar.add_cascade(label='Файл', menu = settings_menu)

        
        count = 1
        for i in range (1, game.row+1):
            for j in range (1, game.col+1):
                btn = self.buttons[i][j]
                btn.number = count
                btn.grid(row = i, column = j, stick = 'NWES')
                count += 1
        for i in range (1, game.row+1):
            tk.Grid.rowconfigure(self.window, i, weight = 1)
        for i in range (1, game.col+1):
            tk.Grid.columnconfigure(self.window, i, weight = 1)
                


        
    def start(self):
        self.create_mapp()
        self.create_wigets()
        #self.count_neib_in_buttons()
        #self.print_buttons()
        game.window.mainloop()


    def count_neib_in_buttons(self):
        for i in range (1, game.row+1):
            for j in range (1, game.col+1):
                btn = self.buttons[i][j]
                count_neib = 0
                for row_dx in [-1, 0, 1]:
                    for col_dx in [-1, 0, 1]:
                        neib = self.buttons[i+row_dx][j+col_dx]
                        if neib.is_alive:
                            count_neib += 1
                if btn.is_alive:
                    count_neib = count_neib - 1
                btn.count_neib = count_neib


                    
    def print_buttons(self):
         for i in range (1, game.row+1):
            for j in range (1, game.col+1):
                btn = self.buttons[i][j]
                game.cells_map[i-1][j-1] = btn.count_neib
    def reload(self):
            [child.destroy() for child in self.window.winfo_children()]
            self.__init__()
            self.create_wigets()

    def start_game(self): 
                changes = False
                self.count_neib_in_buttons()
                self.print_buttons()
                tmp = game.cells_map
                for i in range (1, game.row+1):
                    for j in range (1, game.col+1):
                        btn = self.buttons[i][j]
                        if tmp[i-1][j-1] > 0:
                            if tmp[i-1][j-1] == 3 and not btn.is_alive:
                                btn.is_alive = True
                                game.surv = game.surv + 1
                                changes = True
                                btn.config(background = 'black', disabledforeground ='black')
                            elif (tmp[i-1][j-1]<2 or tmp[i-1][j-1]>3) and btn.is_alive:
                                btn.is_alive = False
                                game.surv = game.surv - 1
                                changes = True
                                btn.config(background = 'white', disabledforeground ='white')
                        else:
                            if btn.is_alive == True:
                                btn.is_alive = False
                                game.surv = game.surv - 1
                                btn.config(background = 'white', disabledforeground ='white')
                #for i in range (1, game.row+1):
                    #for j in range (1, game.col+1):
                        #btn = self.buttons[i][j]
                        #if btn.is_alive:
                            #print('1', end = ' ')
                        #else:
                            #print('0', end = ' ')
                    #print()
                #print()

                if game.surv > 0 and changes == True:
                      game.window.after(100, self.start_game)
                
    def create_mapp(self):
        for i in range(game.row):
            game.cells_map.append([])
            for j in range (game.col):
                game.cells_map[i].append(0)
        
game = game()
#game.create_wigets()
game.start()
