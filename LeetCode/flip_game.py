'''
You are playing the following Flip Game with your friend: Given a string that contains only these two characters: + and -, you and your friend take turns to flip two consecutive “++” into “–”. The game ends when a person can no longer make a move and therefore the other person will be the winner.

Write a function to compute all possible states of the string after one valid move.

Example:

Input: s = “++++“
Output:
[
”--++”,
"+--+",
"++--"
]
Note: If there is no valid move, return an empty list [].
'''
def flip_game(s):
    if len(s)<=1:
        return 
    else:
        print([s[:i-1]+"--"+s[i+1:] for i in range(1, len(s)) if s[i-1:i+1]=="++"])
flip_game("++++")
            
    
    
    
    
    


