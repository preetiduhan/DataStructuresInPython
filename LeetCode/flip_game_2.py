'''
You are playing the following Flip Game with your friend: Given a string that contains only these two characters: + and -, you and your friend take turns to flip two consecutive “++” into “–”. The game ends when a person can no longer make a move and therefore the other person will be the winner.

Write a function to tell if we can win

'''
def flip_game(s):
    if(len(s)<=1 ):
        return False
    else:
        for i in range(1,len(s)):
            if s[i-1]==s[i] and s[i]=='+':
                next_state = s[:i-1]+ "--" + s[i+1:]
                if(not flip_game(next_state)):
                    return True
        return False
out=flip_game("+-++")
print(out)        
        
    
            
    
    
    
    
    


