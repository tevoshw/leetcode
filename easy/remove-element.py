class Solution(object):
    def removeElement(self, nums, val):
            k = 0
            for x in range(len(nums)):
                  if nums[x] != val:
                        nums[k] = nums[x]
                        k += 1
            return k
                      
solution = Solution()
nums = [1,4,2,4,3,4,4,5,4,6,4]
k = solution.removeElement(nums, 4)
print(nums[0:k])
