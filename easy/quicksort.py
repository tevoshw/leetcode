class Solution(object):

    
    def quickSort(self, nums):
        for x in range( len(nums) ):
            for y in range(0, len(nums) - x - 1):
                           if nums[y] > nums[y + 1]:
                                nums[y], nums[y +1] = nums[y + 1], nums[y]
    
        print(nums)

solution = Solution()
nums = [1,24,3,4,4,7,5,54,7,6,56]
solution.quickSort(nums)


# OR
nums.sort()
print(nums)

