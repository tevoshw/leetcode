class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        array = nums1 + nums2


        # DO A QUICKSORT TO ORGANIZE THE ELEMENTS
        for x in range(len(array)):
            for y in range(len(array) - x - 1):
                if array[y] > array[y + 1]:
                    array[y], array[y + 1] = array[y + 1], array[y]

        # GET THE MEDIAN OF THE ARRAY
        if len(array) % 2 != 0:
            median = array[int(len(array) / 2)]
            return median
        else:
            median = float((array[int( (len(array) / 2) - 1)] + array[int( (len(array) / 2) )])) / 2
            return median

       

solution = Solution()
result1 = solution.findMedianSortedArrays([1,3], [2])
result2 = solution.findMedianSortedArrays([1,2], [3,4])
print(f"The median of the first was: {result1}, and the median of the second was: {result2}")