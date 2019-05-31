import TTT_Player

############################################################################################################################################################
# This is the Environment Class
class TTT_ENV :
    
    def __init__ (self):

        # Define Board
        self.board_positions = ["A1", "A2", "A3", "B1", "B2", "B3", "C1", "C2", "C3"]

        # Define Current Board Position : This will goto Reset Board as well
        self.current_board_positions = { self.board_positions[0] : "", 
                                            self.board_positions[1] : "",
                                            self.board_positions[2] : "",
                                            self.board_positions[3] : "",
                                            self.board_positions[4] : "",
                                            self.board_positions[5] : "",
                                            self.board_positions[6] : "",
                                            self.board_positions[7] : "",
                                            self.board_positions[8] : "" 
                                            }

        # Define Winning Position List
        self.winning_positions = [["A1", "A2", "A3"],
                                    ["B1", "B2", "B3"],
                                    ["C1", "C2", "C3"],
                                    ["A1", "B1", "C1"],
                                    ["A2", "B2", "C2"],
                                    ["A3", "B3", "C3"],
                                    ["A1", "B2", "C3"],
                                    ["A3", "B2", "C1"]
                                    ]
    
        
        # Define Player list
        self.players = []

        # Define Winning Status
        self.game_status = ""

        self.winner = ""
        
        
        # End of Init

    # This is a function to add player
    def add_player(self, player):

        # Create a player class object here based on name of the player passed from ENV UI / runtime
        ttt_player  = TTT_Player.TTT_Player(player)
        
        # Append to player list
        self.players.append(ttt_player)

        # return the player object
        return  ttt_player

    # This is a orchestration function to make a player move
    def move(self, player) :
  
        # Call player to make move
        selected_position = player.make_move(self.current_board_positions)

        # Update board position
        self.update_board_position(selected_position, player.name)

        # Check for Winner
        if self.check_winning_position(player) : 
            self.game_status = "WINNER"
            self.winner = player.name
            return selected_position

        # Check for Draw
        if self.check_draw() :
            self.game_status = "DRAW"
            self.winner = "NONE"
            return selected_position

        return selected_position

        

    # This is a function for UI to make a Human Player Move
    def move_UI(self, selected_position, player) :
        
        # Update board position
        self.update_board_position(selected_position, player.name)

        # Check for Winner
        if self.check_winning_position(player) : 
            self.game_status = "WINNER"
            self.winner = player.name
            return selected_position

        # Check for Draw
        if self.check_draw() :
            self.game_status = "DRAW"
            self.winner = "NONE"
            return selected_position

        return selected_position


    # This is a function to check the game is playable (DRAW)
    def check_draw(self) :
        
        # Check available positions If there is a playable move
        for postion, value in self.current_board_positions.items() :
            if value == "" : 
                return False
         
        return True
        
        
    # This is a function to update the current board position
    def update_board_position(self, selected_position, value) :

        #Update the board postion with player selected postion
        self.current_board_positions[selected_position] = value

    
    # This is a function to check Winner
    def check_winning_position(self, player) :

        winner = True

        # Logic to check the player position in winning position list here
        # Get players position
        positions = []
        
        for key, position in self.current_board_positions.items() :
            if position == player.name :
                positions.append(key)
        
        # Check for Winning positions
        
        for item in self.winning_positions:
            
            winner = True
             
            for position in item:
                if not position in positions:
                    winner = False
                    break
            
            if winner : break
        
        return winner


############################################################################################################################################################

# This is main function to run the program Locally
if __name__ == "__main__":
    
    pass