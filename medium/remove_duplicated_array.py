"""

Input: nums = [1,1,2]
Output: 2, nums = [1,2,_]
"""


class Solution:
    def remove(self, nums):
        nums = list(set(nums))
        print(nums)


            
solution = Solution()
nums = [0,0,1,1,1,2,2,3,3,4,5,5,5,5,5,6,6,7,8,9,0,7,5,5,5,5,5,5]
solution.remove(nums)