'''
Robot Return to Origin
Easy

There is a robot starting at position (0, 0), the origin, on a 2D plane. Given a sequence of its moves, judge if this robot ends up at (0, 0) after it completes its moves.

The move sequence is represented by a string, and the character moves[i] represents its ith move. Valid moves are R (right), L (left), U (up), and D (down). If the robot returns to the origin after it finishes all of its moves, return true. Otherwise, return false.

Note: The way that the robot is "facing" is irrelevant. "R" will always make the robot move to the right once, "L" will always make it move left, etc. Also, assume that the magnitude of the robot's movement is the same for each move.

Example 1:

Input: "UD"
Output: true 
Explanation: The robot moves up once, and then down once. All moves have the same magnitude, so it ended up at the origin where it started. Therefore, we return true.
'''
class Solution:
    def judgeCircle(self, moves: str) -> bool:
        count ={'L':0,'R':0,'U':0,'D':0}
        for move in moves:
            if move in count:
                count[move] = count[move]+1
        if count['L'] != count['R']:
            return False
        if count['U'] != count['D']:
            return False
        return True
        
