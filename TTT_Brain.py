        
import operator
import random

############################################################################################################################################################
# This is TTT Brain Class
class TTT_Brain :

    def __init__ (self) :
        # This is the main Data store in the brain in the form of a dictionary of available positions to the selected choice mapping
        self.memory = {}

        # Learning Rate
        self.alpha = 0.01

        # Discount Factor
        self.gamma = 0.7

        # Switch to decide if training or testing
        self.train = False

        # Switch to show the memory
        self.shows = False

        # variable to analyze a position
        #self.position_by_key = { "A1":0, "A2":0, "A3":0, "B1":0, "B2":0, "B3":0, "C1":0, "C2":0, "C3":0 }
        self.position_history = []

        

    # This function looks up the memory and get the best decision for available choices
    def make_decision(self, current_board_positions) :

        
        # Convert availale positions to KEY
        key = ""
        position_table = {} 
        select_position = ""

        # Logic to construct the Key (Snapshot)
        for position, owner in current_board_positions.items() :
            key = key + position + owner

        
        
        # Get the position table from the key
        if self.memory :
            position_table = self.memory.get(key)

        # if found , look up value for best choice
        if position_table :

            if self.shows :
                print(key)
                print(position_table)
            
            # This is the algorithm to return the random choice when training else choose max value (when playing / testing)
            if self.train :             
                
                if key == "A1A2A3B1B2B3C1C2C3" :
                    select_position = "A1"
                elif key == "A1XA2A3B1B2B3C1C2C3":
                    select_position = "B2"
                elif key == "A1XA2A3B1B2OB3C1C2C3":
                    select_position = "C3"
                elif key == "A1XA2A3B1B2OB3C1C2C3X":
                    select_position = "A3"
                else :
                    num = random.randint(0, len(position_table)-1)
                    select_position = list(position_table.keys())[num]
                    
                
                
                '''
                max_value = max(position_table.items(), key=operator.itemgetter(1))[1]
                min_value = min(position_table.items(), key=operator.itemgetter(1))[1]
                diff = max_value - min_value

                if diff > max_value*0.8 :
                
                    # Create probability number 
                    pn = random.randint(0, 99)
                    
                    if pn < 10 : 
                        # select Ramdom 
                        # Return a random choice
                        num = random.randint(0, len(position_table)-1)
                        select_position = list(position_table.keys())[num]
                    else :
                        # select max
                        select_position = max(position_table.items(), key=operator.itemgetter(1))[0]
                
                else :

                    num = random.randint(0, len(position_table)-1)
                    select_position = list(position_table.keys())[num]
                '''
                #num = random.randint(0, len(position_table)-1)
                #select_position = list(position_table.keys())[num]

                            
            else : 
                select_position = max(position_table.items(), key=operator.itemgetter(1))[0]


        # If not found then Create position table
        else :
            
            # Find the available positions in the current board
            available_positions = []
            for position, value in current_board_positions.items() :
                if value == "" : 
                    available_positions.append(position)
            
            # Construct the position table
            position_table = {}
            for position in available_positions :
                position_table.update({position : 0 })

            # Store this value (snapshot) in the memory
            self.memory.update( { key : position_table } )

            # Return a Ramdom item
            num = random.randint(0, len(available_positions)-1)
            select_position = available_positions[num]
            
        # Analysis data here
        #if key == "A1A2A3B1B2B3C1C2C3" :
        #    self.position_history.append(str(position_table))
        

        
        return key, select_position
        
    # This is the function to update the memory with  rewards / punishments
    def update_memory(self, positions, reward) :
        
        score_last = reward

        for key, value in reversed(positions.items()):
            
            position_table =  self.memory.get(key)
            
            score = position_table.get(value)

            score_new = (1-self.alpha) * score + self.alpha*self.gamma*(score_last)

            position_table.update({ value : score_new })

            # Add this new position table into the monitoring table based on Key

            # Keep the old score in the memory
            score_last = score_new

        
        
