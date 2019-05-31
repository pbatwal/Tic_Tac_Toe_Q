############################################################################################################################################################
from collections import OrderedDict

# This is a player class
class TTT_Player:

    def __init__ (self, name):

        self.name = name

        self.positions = OrderedDict()

        #  Select a choice based on Brain's response
        self.ttt_brain = None

        self.computer_player = False

    def make_move(self, current_board_positions) :

        # This line can be changed to select a brain : 
        # Ask brain to select a choice based on current board position
        key, selected_position = self.ttt_brain.make_decision(current_board_positions)

        # Update position Table
        self.positions.update({ key : selected_position})

        # Return Selected Choice
        return selected_position

    def get_reward(self, reward) :
        
        # Update brains memory based on reward
        self.ttt_brain.update_memory(self.positions, reward)