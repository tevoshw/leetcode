"""
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.

"""


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        
        # INVERTER AS LISTAS
        l1 = l1[::-1]
        l2 = l2[::-1]

        # TRANSFORMAR EM STRING AS LISTAS
        l1_str = ''
        for x in range(len(l1)):
            l1_str += str(l1[x])
        
        l2_str = ''
        for x in range(len(l2)):
            l2_str += str(l2[x])
        print(l1_str, l2_str)

        # TRANSFORMAR EM NÚMEROS INTEIROS E SOMAR
        k = int(l1_str) + int(l2_str)
        print(f"O resultado total da soma de {l1_str} + {l2_str}, é: {k}")


solution = Solution()
solution.addTwoNumbers([0,0,1], [0,1 ])