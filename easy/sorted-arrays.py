class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        array = nums1 + nums2
        print(array)
        len_array = len(array)
        print(len_array)

solution = Solution()
solution.findMedianSortedArrays([1,2,3], [1,5,6])