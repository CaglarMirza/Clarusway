asal_list = []
n = 100
for i in range(2,n):
    for x in range(2,i):
        if (i%x) == 0:
            break
    else:
        asal_list.append(i)

print(asal_list)
