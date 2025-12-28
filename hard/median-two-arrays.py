class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        array = nums1 + nums2


        # DO A QUICKSORT TO ORGANIZE THE ELEMENTS
        for x in range(len(array)):
            for y in range(len(array) - x - 1):
                if array[y] > array[y + 1]:
                    array[y], array[y + 1] = array[y + 1], array[y]

        # GET THE MEDIAN OF THE ARRAY
        print( len(array) )
        print( len(array) / 2)
        print( int(len(array) / 2))

        if len(array) % 2 != 0:
            median = array[int(len(array) / 2)]
        else:
            median = (array[int( (len(array) / 2) - 1)] + array[int( (len(array) / 2) )]) / 2
            median.float()

       

solution = Solution()
solution.findMedianSortedArrays([1,2], [3,4])