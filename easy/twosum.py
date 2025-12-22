"""
Dado um array de inteiros nums e um número inteiro alvo‚retorno índices dos dois números tais que somam alvo.O.

Você pode supor que cada entrada teria exatamente uma solução, e você não pode usar o mesmo elemento duas vezes.

Pode retornar a resposta em qualquer ordem.

 

Exemplo 1:

Entrada: nums = [2,7,11,15], alvo = 9
Saída: [0,1]
Explicação: Porque nums[0] + nums[1] == 9, voltamos [0, 1].
Exemplo 2:

Entrada: nums = [3,2,4], alvo = 6
Saída: [1,2]
Exemplo 3:

Entrada: nums = [3,3], alvo = 6
Saída: [0,1]

"""


class Solution(object):
    def twoSum(self, nums, target):
        for x in range(len(nums)):
            for y in range(x + 1, len(nums)):
                if nums[x] + nums[y] == target:
                    return x, y


solution = Solution()
result = solution.twoSum([3,2,6] , 8)

print(result)

''' OUTPUT = (1,2) '''