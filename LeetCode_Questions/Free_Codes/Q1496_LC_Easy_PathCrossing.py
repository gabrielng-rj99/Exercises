'''     1496. Path Crossing      Easy

Given a string path, where path[i] = 'N', 'S', 'E' or 'W',
each representing moving one unit north, south, east, or west,
respectively. You start at the origin (0, 0) on a 2D plane
and walk on the path specified by path.

Return true if the path crosses itself at any point, that is,
if at any time you are on a location you have previously visited.
Return false otherwise.

 

Example 1:
    Input: path = "NES"
    Output: false 
        Explanation: Notice that the path doesn't cross any point more than once.

Example 2:
    Input: path = "NESWW"
    Output: true
        Explanation: Notice that the path visits the origin twice.
 

Constraints:

1 <= path.length <= 10^4
path[i] is either 'N', 'S', 'E', or 'W'.
'''

class Solution:
    def isPathCrossing(self, path: str) -> bool:
        arrmap = {(0, 0)}
        x, y = 0, 0
        for cd in path:
            if cd == 'N':
                y += 1
            elif cd == 'S':
                y -= 1
            elif cd == 'E':
                x += 1
            elif cd == 'W':
                x -= 1
            

            if (x,y) in arrmap:
                return True
            
            arrmap.add((x, y))
        
        return False

testcases = [
    "NES",
    "NESWW",
    "NEEESWNW",
]

for test in testcases:
    print(Solution().isPathCrossing(test))