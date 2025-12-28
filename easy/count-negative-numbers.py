"""
Input: grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
Output: 8
Explanation: There are 8 negatives number in the matrix.
"""

class Solution(object):
    def countNegatives(self, grid):
        k = 0
        print(len(grid))
        for x in range(len(grid)):
            for y in range(len(grid[x])):
                if grid[x][y] < 0:
                    k += 1
                    print(f"O número {grid[x][y]} é negativo")

        return k

solution = Solution()
result = solution.countNegatives(  [[1,2,3,5], [-4,-5,-6]] )
print(f"OUTPUT: {result}")

