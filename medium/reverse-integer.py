"""

Example 1:

Input: x = 123
Output: 321
Example 2:

Input: x = -123
Output: -321
Example 3:

Input: x = 120
Output: 21



"""



class Solution:
    def reverse(self, x: int) -> int:
        k = x
        if x < -2**31 or x > 2**31 - 1:
            return 0
        

        # FIRST TRY
        invertido  = 0

        # SEE IF 0 ITS THE LAST NUMBER
        while x % 10 == 0:
            # HOW WE DO 120 TURN 12? -> DIVIDED BY 10
            x =  int(x / 10)

        # INVERT IF THE NUMBER POSITIVE
        if x > 0:
            while x > 0:
                invertido = invertido * 10 + x % 10
                x //= 10
                if x < -2**31 or x > 2**31 - 1:
                    return 0
                return invertido
            
            
        # INVERT IF THE NUMBER NEGAT
        else:
            sinal = -1 if x < 0 else 1
            x = abs(x)
            invertido = 0
            while x > 0:
                invertido = invertido * 10 + x % 10
                x //= 10
                if x < -2**31 or x > 2**31 - 1:
                    return 0
                return sinal * invertido
    

        # SECOND TRY
        x = k

        if x > 0:
            x = abs(x)
            x = int(str(x)[::-1])
            if x < -2**31 or x > 2**31 - 1:
                return 0
            return x
        else:
            x = abs(x)
            x = (int(str(x)[::-1])) * -1
            if x < -2**31 or x > 2**31 - 1:
                return 0            
            return x


            
solution = Solution()
solution.reverse(3450)