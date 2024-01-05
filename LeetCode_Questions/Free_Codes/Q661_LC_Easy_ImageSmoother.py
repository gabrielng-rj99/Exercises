'''     661. Image Smoother     Easy

An image smoother is a filter of the size 3 x 3 that can be
applied to each cell of an image by rounding down the average
of the cell and the eight surrounding cells (i.e., the average
of the nine cells in the blue smoother). If one or more of the
surrounding cells of a cell is not present, we do not consider
it in the average (i.e., the average of the four cells in the red smoother).


Given an m x n integer matrix img representing the grayscale of
an image, return the image after applying the smoother on each cell of it.

 

Example 1:
    Input: img = [[1,1,1],[1,0,1],[1,1,1]]
    Output: [[0,0,0],[0,0,0],[0,0,0]]
Explanation:
    For the points (0,0), (0,2), (2,0), (2,2): floor(3/4) = floor(0.75) = 0
    For the points (0,1), (1,0), (1,2), (2,1): floor(5/6) = floor(0.83333333) = 0
    For the point (1,1): floor(8/9) = floor(0.88888889) = 0

Example 2:
    Input: img = [[100,200,100],[200,50,200],[100,200,100]]
    Output: [[137,141,137],[141,138,141],[137,141,137]]
Explanation:
    For the points (0,0), (0,2), (2,0), (2,2): floor((100+200+200+50)/4) = floor(137.5) = 137
    For the points (0,1), (1,0), (1,2), (2,1): floor((200+200+50+200+100+100)/6) = floor(141.666667) = 141
    For the point (1,1): floor((50+200+200+200+200+100+100+100+100)/9) = floor(138.888889) = 138
 

Constraints:

m == img.length
n == img[i].length
1 <= m, n <= 200
0 <= img[i][j] <= 255'''

from numpy import array
class Solution:
    def imageSmoother(self, img: list[list[int]]):
        m = len(img)
        n = len(img[0])

        new_img = []

        for i in range(m):
            new_line = []
            for j in range(n):
                temp_list = []

                center  = img[i][j]  

                top     = img[i-1][j]   if i>0 else None     # the Nones is for corner cases
                bot     = img[i+1][j]   if i<(m-1) else None
                left    = img[i][j-1]   if j>0 else None
                right   = img[i][j+1]   if j<(n-1) else None
                
                topLeft = img[i-1][j-1] if i>0 and j>0 else None 
                topRight= img[i-1][j+1] if i>0 and j<(n-1) else None
                botLeft = img[i+1][j-1] if i<(m-1) and j>0 else None
                botRight= img[i+1][j+1] if i<(m-1) and j<(n-1) else None

                temp_list = [topLeft, top, topRight, left, center, right, botLeft, bot, botRight]
                
                for index in range(len(temp_list)-1, -1, -1): # remove backwards to not disturb
                    if temp_list[index] is None:              # the iteration deleting elements 
                        del temp_list[index]                  # treating the data

                new_img_ij = sum(temp_list)//len(temp_list) # now we can easily make a avarage
                new_line += [new_img_ij]

            new_img += [new_line]

        return array(new_img)
    
        
testcases = [
    [[1,1,1],[1,0,1],[1,1,1]],                          # [[0,0,0],[0,0,0],[0,0,0]]
    [[100,200,100],[200,50,200],[100,200,100]],         # [[137,141,137],[141,138,141],[137,141,137]]
    [[2,3,4],[5,6,7],[8,9,10],[11,12,13],[14,15,16]],   # [[4,4,5],[5,6,6],[8,9,9],[11,12,12],[13,13,14]]
]

for test in testcases:
    print(Solution().imageSmoother(test), '\n')