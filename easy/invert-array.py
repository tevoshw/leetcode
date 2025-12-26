# JSUT USING A CPP LOGIC IN THIS, BUT OK ;)

list1 = [1,2,3,4,5]
list2 = []

for x in range (len(list1)):
    k = (len(list1) - x - 1)
    list2.append(list1[k])

print(list1, list2)