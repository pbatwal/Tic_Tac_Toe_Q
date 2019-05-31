# Tic_Tac_Toe_Q
This project presents a Tic-Tac-Toe Simulator using Q Learning
I have created few files here.
1 : TTT ENV - This is the TTT Environment which has basic games rules, win/draw check etc
2 : TTT Player - This is a player which gets the current board position from the TTT ENV and calls a TTT Brain to make the decision
3 : TTT Brain - This is the brain which keeps snapshot of every position and makes a move based on available positions and current board position 
4 : TTT Trainer - This is a trainng program which created a TTT Brain, TTT ENV and 2 TTT Players. It makes the player plag against itself for a configurable times using same brain
5 : TTTGUIMain - This is the TKInter GUI if a human player wants to play against Human or Computer (Default is Player 2 (O) is computer
6 : TTT Brain Dump TXT File : this is how the brain is serializezd to a file object. a trained brain can then be used with test and live play

This software uses Q Learning with a policy function : Q(SA) = (1-alpha)*Q(SA) + alpha*gamma*Q(S'A)
pls contact me for details and suggestions : piyush.batwal@gmail.com
