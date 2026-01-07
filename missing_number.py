# DESCOBRIR O TAMANHO DO ARRAY
list = [3,4,5,6,7,9,0,1,8]


# ORGANIZAR O ARRAY COM BUBBLE SORT

for x in range( len(list) ):
    for y in range(0, len(list) - x - 1):
        if list[y] > list[y + 1]:
            list[y], list[y +1] = list[y + 1], list[y]


# VERIFICAR UM POR UM
for x in range( len(list)+ 1):
    if x not in list:
        list.append(x)
        k = x
print(f"First try with my methods: {k}")

### OR OTHER WAY

# SUM OF ALL RANGE (0,X + 1) - SUM OF ALL ARRAY = NUMBER MISSING
n = len(list)
k =  n * (n + 1) // 2 - sum(list)
print(f"Other way: {k}")