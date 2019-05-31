
import tkinter as tk
from tkinter import messagebox as tkMsg
import random
import TTT_ENV
import TTT_Brain
import TTT_Player
import json


# local Variable Declaration here 


## Main UI Class
class TTT_GUI() :

    
   
    def __init__(self, ttt_brain):
        
        # Declare all UI Compoments here 
        self.root = None

        self.ttt_env = None

        self.player1 = None

        self. player2 = None

        self.game_on = False

        self.ttt_brain = ttt_brain

        self.position_map = {}


    # Function to Initialize TTT ENV
    def initiate_TTT_ENV(self) :
        # Instantiate the TTT ENV Class
        self.ttt_env   = TTT_ENV.TTT_ENV()

        # Add the players
        self.player1 = self.ttt_env.add_player("X")
        self.player2 = self.ttt_env.add_player("O")

        self.active_player = None
        

    # Function to Initialize the UI
    def initiate_ui(self) :

        # Local variables here

        padx = 10
        pady = 10

        ipadx = 10
        ipady = 10

        # Construct Root Frame (main canvas)
        self.create_frame()
        
        # Set Application Title 
        self.root.title("Tic-Tac-Toe Simulator")


        # Assign a grid geometry to root
        self.root.grid_rowconfigure(0, weight = 1)
        self.root.grid_columnconfigure(0, weight = 1)
        self.root.grid_rowconfigure(1, weight = 8)
        
        # Create a Frame (Top)
        self.frame_top = tk.Frame(self.root, bd= 2, bg = "#D3D3D3")
        self.frame_top.grid(row=0, column =0, sticky = "snew", padx=padx, pady=pady)
        
        # set grid parameters for Top Frame : for each column, weight denotes its % space used
        self.frame_top.grid_rowconfigure(0, weight = 1)
        self.frame_top.grid_columnconfigure(0, weight = 1)
        self.frame_top.grid_rowconfigure(1, weight = 1)
        self.frame_top.grid_columnconfigure(1, weight = 1)

        # Add Top Frame Components
        self.label_player1 = tk.Label(self.frame_top, text="Player 1 (X)", bd = 4, padx=padx, pady=pady, anchor = tk.CENTER, font=("Helvetica", 16))
        self.label_player1.grid(row = 0, column = 0, sticky = "snew",  padx=padx, pady=pady)

        self.label_player2 = tk.Label(self.frame_top, text="Player 2 (O)", bd = 4, padx=padx, pady=pady, anchor = tk.CENTER, font=("Helvetica", 16))
        self.label_player2.grid(row = 0, column = 1, sticky = "snew",  padx=padx, pady=pady)

        self.button_start = tk.Button(self.frame_top, text="Start", bd = 4, padx=padx, pady=pady, command=self.start,  font=("Helvetica", 18)) 
        self.button_start.grid(row = 1, column = 0, sticky = "snew", padx=padx, pady=pady, columnspan = "2")

        
        # Create a Frame (Middle)
        self.frame_middle = tk.Frame(self.root, bd= 2, bg = "#D3D3D3")
        self.frame_middle.grid(row=1, column =0, sticky = "snew", padx=padx, pady=pady)
        
        # set grid parameters for Top Frame : for each column, weight denotes its % space used
        self.frame_middle.grid_rowconfigure(0, weight = 1)
        self.frame_middle.grid_rowconfigure(1, weight = 1)
        self.frame_middle.grid_rowconfigure(2, weight = 1)
        self.frame_middle.grid_columnconfigure(0, weight = 1)
        self.frame_middle.grid_columnconfigure(1, weight = 1)
        self.frame_middle.grid_columnconfigure(2, weight = 1)
        
        self.button_A1 = tk.Button(self.frame_middle, text="", bd = 4, padx=padx, pady=pady, command=self.move_A1,  font=("Helvetica", 18) )
        self.button_A1.grid(row = 0, column = 0, sticky = "snew", padx=padx, pady=pady)
        self.position_map.update({"A1" : self.button_A1})
        

        self.button_A2 = tk.Button(self.frame_middle, text="", bd = 4, padx=padx, pady=pady, command=self.move_A2,  font=("Helvetica", 18) )
        self.button_A2.grid(row = 0, column = 1, sticky = "snew", padx=padx, pady=pady)
        self.position_map.update({"A2" : self.button_A2})
        

        self.button_A3 = tk.Button(self.frame_middle, text="", bd = 4, padx=padx, pady=pady, command=self.move_A3,  font=("Helvetica", 18) )
        self.button_A3.grid(row = 0, column = 2, sticky = "snew", padx=padx, pady=pady)
        self.position_map.update({"A3" : self.button_A3})
        

        self.button_B1 = tk.Button(self.frame_middle, text="", bd = 4, padx=padx, pady=pady, command=self.move_B1,  font=("Helvetica", 18) )
        self.button_B1.grid(row = 1, column = 0, sticky = "snew", padx=padx, pady=pady)
        self.position_map.update({"B1" : self.button_B1})

        self.button_B2 = tk.Button(self.frame_middle, text="", bd = 4, padx=padx, pady=pady, command=self.move_B2,  font=("Helvetica", 18) )
        self.button_B2.grid(row = 1, column = 1, sticky = "snew", padx=padx, pady=pady)
        self.position_map.update({"B2" : self.button_B2})

        self.button_B3 = tk.Button(self.frame_middle, text="", bd = 4, padx=padx, pady=pady, command=self.move_B3,  font=("Helvetica", 18) )
        self.button_B3.grid(row = 1, column = 2, sticky = "snew", padx=padx, pady=pady)
        self.position_map.update({"B3" : self.button_B3})

        self.button_C1 = tk.Button(self.frame_middle, text="", bd = 4, padx=padx, pady=pady, command=self.move_C1,  font=("Helvetica", 18) )
        self.button_C1.grid(row = 2, column = 0, sticky = "snew", padx=padx, pady=pady)
        self.position_map.update({"C1" : self.button_C1})

        self.button_C2 = tk.Button(self.frame_middle, text="", bd = 4, padx=padx, pady=pady, command=self.move_C2,  font=("Helvetica", 18) )
        self.button_C2.grid(row = 2, column = 1, sticky = "snew", padx=padx, pady=pady)
        self.position_map.update({"C2" : self.button_C2})

        self.button_C3 = tk.Button(self.frame_middle, text="", bd = 4, padx=padx, pady=pady, command=self.move_C3,  font=("Helvetica", 18) )
        self.button_C3.grid(row = 2, column = 2, sticky = "snew", padx=padx, pady=pady)
        self.position_map.update({"C3" : self.button_C3})


        self.root.mainloop()



    # Supporting UI functions here
    def create_frame(self):
        self.root = tk.Tk()
        
        ## Set Frame Size
        w=1024
        h=768

        ## Get Screen Resolution
        ws=self.root.winfo_screenwidth()
        hs=self.root.winfo_screenheight()
        
        ## Calculate mid of the screen
        x=(ws/2)-(w/2)
        y=(hs/2)-(h/2)

        ## Set the Top Left to position the Frame
        self.root.geometry('%dx%d+%d+%d'%(w,h,x,y))


    # UI Callback functions here

    # These are callback functions for buttons to make move
    
    def move_A1(self) :
        if  self.game_on == False :
            tkMsg.showerror("Error", "Please Press Start Button")
            return

        if self.button_A1.cget("text") == "" and self.ttt_env.game_status == "" :
            # Change Button text             
            self.button_A1.config(text = self.active_player.name)

            # Make move
            self.make_move("A1")
            
    def move_A2(self) :
        if  self.game_on == False:
            tkMsg.showerror("Error", "Please Press Start Button")
            return
            
        if self.button_A2.cget("text") == "" and self.ttt_env.game_status == "":
            # Change Button text             
            self.button_A2.config(text = self.active_player.name)

            # Make move
            self.make_move("A2")

    def move_A3(self) :
        if  self.game_on == False:
            tkMsg.showerror("Error", "Please Press Start Button")
            return
            
        if self.button_A3.cget("text") == "" and self.ttt_env.game_status == "":
            # Change Button text             
            self.button_A3.config(text = self.active_player.name)

            # Make move
            self.make_move("A3")

    def move_B1(self) :
        if  self.game_on == False:
            tkMsg.showerror("Error", "Please Press Start Button")
            return
            
        if self.button_B1.cget("text") == "" and self.ttt_env.game_status == "":
            # Change Button text             
            self.button_B1.config(text = self.active_player.name)

            # Make move
            self.make_move("B1")
    
    def move_B2(self) :
        if  self.game_on == False:
            tkMsg.showerror("Error", "Please Press Start Button")
            return
            
        if self.button_B2.cget("text") == "" and self.ttt_env.game_status == "":
            # Change Button text             
            self.button_B2.config(text = self.active_player.name)

            # Make move
            self.make_move("B2")

    def move_B3(self) :
        if  self.game_on == False:
            tkMsg.showerror("Error", "Please Press Start Button")
            return
            
        if self.button_B3.cget("text") == "" and self.ttt_env.game_status == "":
            # Change Button text             
            self.button_B3.config(text = self.active_player.name)

            # Make move
            self.make_move("B3")

    def move_C1(self) :
        if  self.game_on == False:
            tkMsg.showerror("Error", "Please Press Start Button")
            return
            
        if self.button_C1.cget("text") == "" and self.ttt_env.game_status == "":
            # Change Button text             
            self.button_C1.config(text = self.active_player.name)

            # Make move
            self.make_move("C1")

    def move_C2(self) :
        if  self.game_on == False:
            tkMsg.showerror("Error", "Please Press Start Button")
            return
            
        if self.button_C2.cget("text") == "" and self.ttt_env.game_status == "":
            # Change Button text             
            self.button_C2.config(text = self.active_player.name)

            # Make move
            self.make_move("C2")
    
    def move_C3(self) :
        if  self.game_on == False:
            tkMsg.showerror("Error", "Please Press Start Button")
            return
            
        if self.button_C3.cget("text") == "" and self.ttt_env.game_status == "":
            # Change Button text             
            self.button_C3.config(text = self.active_player.name)

            # Make move
            self.make_move("C3")


    # This is the start callback function
    def start(self) :
        
        self.reset()

        # Toss and make one player active
        self.active_player = self.toss()
        self.highlight_active_player()
        self.game_on = True

        if self.active_player.computer_player == True :
            self.move_computer_player()

    # This is reset support function called by start
    def reset(self) :
        
        # Make all the buttons reset here
        self.label_player1.config(bg = "#D3D3D3")
        self.label_player2.config(bg = "#D3D3D3")
        self.button_A1.config(text = "")
        self.button_A2.config(text = "")
        self.button_A3.config(text = "")
        self.button_B1.config(text = "")
        self.button_B2.config(text = "")
        self.button_B3.config(text = "")
        self.button_C1.config(text = "")
        self.button_C2.config(text = "")
        self.button_C3.config(text = "")
        self.game_on = False

        # Kill the TTT ENV and create a new object of it
        self.initiate_TTT_ENV()

        # Assign Brain to the player (This will be set by a checkbox later)
        self.player2.computer_player = True
        self.player2.ttt_brain = self.ttt_brain


    # Supporting Other Functions here 
    def toss(self):
        num = random.randint(0, 1)
        if num == 0 :
            return self.player1
        if num == 1 :
            return self.player2

    
    def check_game_conclusion(self) :
        
        # Check for Winner
        if self.ttt_env.game_status == "WINNER":
            tkMsg.showinfo("Winner", "Game Over !! Winner is :" +  self.active_player.name)
            self.game_on = False
            return True
        
        if self.ttt_env.game_status == "DRAW":
            tkMsg.showinfo("Draw", "Game DRAW !!!")
            self.game_on = False
            return True
        
        return False


    def change_active_player(self) :
        #Change Active Player
        
        if self.active_player.name == "X":
            self.player1 = self.active_player
            self.active_player = self.player2
            return
        
        if self.active_player.name == "O":
            self.player2 = self.active_player
            self.active_player = self.player1
            return

    def highlight_active_player(self):
        
        if self.active_player.name == "X":
            self.label_player1.config(bg = "#FFFFFF")
            self.label_player2.config(bg = "#D3D3D3")
        if self.active_player.name == "O":
            self.label_player2.config(bg = "#FFFFFF")
            self.label_player1.config(bg = "#D3D3D3")

    def make_move(self, position) :
        
        # make env move the board
        self.ttt_env.move_UI(position, self.active_player)

        #check winner/draw
        if self.check_game_conclusion() : 
            return
        # Change active player
        self.change_active_player()

        # Highlight Active player
        self.highlight_active_player()

        # Move if the active Player is Computer
        if self.active_player.computer_player == True :
            self.move_computer_player()
            
     
    def move_computer_player(self) :
        
        selected_postion = self.ttt_env.move(self.active_player)

        # Modify UI
        w = self.position_map.get(selected_postion)
        w.config(text = self.active_player.name)

        #check winner/draw
        if self.check_game_conclusion() : 
            return

        # Change active player
        self.change_active_player()

        # Highlight Active player
        self.highlight_active_player()

    
## End of Main UI Class

# Main function
def main():
    
    #strength = 500000
    
    # ttt_brain = get_trained_brain(strength)

    brain_file = open("brain_dump_final.txt", "r")

    ttt_brain = TTT_Brain.TTT_Brain()

    ttt_brain.memory = json.loads(brain_file.read())

    ttt_brain.shows = True

    # Switch to TEST mode
    ttt_brain.train = False


    #print(ttt_brain.memory)

    
    # Initiate GUI Class
    ttt_gui = TTT_GUI(ttt_brain)

    # Create ENV
    ttt_gui.initiate_TTT_ENV()

    

    ttt_gui.initiate_ui()


    print("Program Complete")


def get_trained_brain(strength) :

    
    # Create brain 
    ttt_brain = TTT_Brain.TTT_Brain()

    # Switch to train mode
    ttt_brain.train = True

    # open a file to record qtable
    out_file_all = open("brain_dump_all.txt", "w")
    out_file_final = open("brain_dump_final.txt", "w")



    # Play games (Training)

    game_count  = strength
    p1_winning_count = 0
    p2_winning_count = 0
    draw_count = 0

    for i in range(0,game_count) :

        ttt_env   = TTT_ENV.TTT_ENV()
        p1 = ttt_env.add_player("X")
        p2 = ttt_env.add_player("O")

        p1.ttt_brain = ttt_brain
        p2.ttt_brain = ttt_brain

        toggle = True

        while not ttt_env.game_status   :
            if toggle :
                ttt_env.move(p1)
                toggle = False
            else :
                ttt_env.move(p2)
                toggle = True

        

        if ttt_env.game_status == "WINNER" :

            reward1 =  6-len(p1.positions)
            punishment1 = -6+len(p1.positions)

            reward2 =  6-len(p2.positions)
            punishment2 = -6+len(p2.positions)
            
            if p1.name == ttt_env.winner :
                p1.get_reward(reward1)
                p2.get_reward(punishment2)
                p1_winning_count +=1
                
            if p2.name == ttt_env.winner :
                p2.get_reward(reward2)
                p1.get_reward(punishment1)
                p2_winning_count +=1
                
            
        
        if ttt_env.game_status == "DRAW" :
            #print("Game Draw !!")
            draw_count += 1
        
        #  Print Q table
        #for key, value in ttt_brain.memory.items():
        #    out_file_all.write(str(i) + "\t" + str(len(key)) + "\t" + key + "\t" + str(value) + "\t" + ttt_env.game_status + "\n"  )

        # cleanup 

        print("This was Game : "+ str(i))
    
    
    print("P1 Winning : " + str(p1_winning_count))
    print("P2 Winning : " + str(p2_winning_count))
    print("Draw  : " + str(draw_count))

    #  Print final Q table
    for key, value in ttt_brain.memory.items():
        out_file_final.write(str(len(key)) + "\t" + key + "\t" + str(value) + "\t" + ttt_env.game_status + "\n" )
 
    return ttt_brain

if __name__ == '__main__':
        main()