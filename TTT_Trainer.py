import TTT_ENV
import TTT_Brain
import TTT_Player
import json

# Main function
def main():
    
    strength = 100000
    
    ttt_brain = get_trained_brain(strength)

    print("Program Complete")


def get_trained_brain(strength) :

    
    # Create brain 
    ttt_brain = TTT_Brain.TTT_Brain()

    # Switch to train mode
    ttt_brain.train = True

    # open a file to record qtable
    
    out_file_final = open("brain_dump_final.txt", "w")
    out_file_final_table = open("brain_dump_final_table.txt", "w")
    #out_file_pos1 = open("position_A1A2A3B1B2B3C1C2C3.txt", "w")
    out_file_pos10 = open("position_A1A2A3B1B2XB3C1C2C3.txt", "w")


    # Play games (Training)

    game_count  = strength
    p1_winning_count = 0
    p2_winning_count = 0
    draw_count = 0
    file_str = ""
    value_last = None
    key2 = "A1XA2A3OB1B2OB3C1C2C3X"

    reward1 =  1 #6-len(p1.positions)
    punishment1 = -1 #-6+len(p1.positions)

    reward2 = 1 # 6-len(p2.positions)
    punishment2 = -1 #-6+len(p2.positions)

    draw_reward = 0.5

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
            #p1.get_reward(draw_reward)
            #p2.get_reward(draw_reward)
            draw_count += 1
        
        #  Print Q table
       
        '''
        key1 = "A1A2A3B1B2B3C1C2C3"
        value1 = ttt_brain.memory.get(key1)
        out_file_pos1.write(str(i) + "\t" + str(len(key1)) + "\t" + key1 + "\t" + str(value1) + "\n")
        '''

        
        value2 = ttt_brain.memory.get(key2)
        if str(value2) != value_last :
            out_file_pos10.write(str(i) + "\t" + str(len(key2)) + "\t" + key2 + "\t" + str(value2) + "\n")
            value_last = str(value2)

        

        

        # cleanup 

        if i%10000 == 0 :
            print("This was Game : "+ str(i))

        # End of Game
    
    
    
    
    print("P1 Winning : " + str(p1_winning_count))
    print("P2 Winning : " + str(p2_winning_count))
    print("Draw  : " + str(draw_count))

    #  Print final Q table
    #for key, value in ttt_brain.memory.items():
    #    out_file_final_table.write(str(len(key)) + "\t" + key + "\t" + str(value)  + "\n" )
 
    # print the position table
    #for item in ttt_brain.position_by_key :
    #    out_file_position.write(item + "\n" )
    #print(ttt_brain.position_by_key)
    
    for item in ttt_brain.position_history : 
        out_file_position.write(item + "\n")
    
    # Dump the file as JSON (save in file)
    brain_dump = json.dumps(ttt_brain.memory, indent=4)
    out_file_final.write(brain_dump)
    out_file_final.close()
    
    
    return ttt_brain

if __name__ == '__main__':
        main()