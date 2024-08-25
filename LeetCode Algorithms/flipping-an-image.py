""" https://leetcode.com/problems/flipping-an-image/ """

class Solution:
    def flipAndInvertImage(self, image):

        # Reverse Each Row
        for row in range(len(image)):
            image[row].reverse()            

        # Invert the Image
        for i in range(len(image)):
            for j in range(len(image[0])):
                if (image[i][j] == 0):
                    image[i][j] = 1
                else:
                    image[i][j] = 0

        return image

print(Solution().flipAndInvertImage([[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]))
