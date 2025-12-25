# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        list3 = list1 + list2
        # USING A QUICKSORT // OR WE USE THE SORT()
        for x in range(len(list3)):
            for y in range(0, len(list3) - x - 1):
                if list3[y] > list3[y + 1]:
                    list3[y], list3[y + 1] = list3[y + 1], list3[y]
        return list3
        

solution = Solution()
solution.mergeTwoLists([3,4,2], [1,2,3])