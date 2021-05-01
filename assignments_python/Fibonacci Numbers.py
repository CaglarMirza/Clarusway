
liste = []
for i in range(11):
    liste.append(1 if i<=1 else liste[i-2]+liste[i-1] )

print(liste)



# liste = []

# for i in range(11):
#     if i<=1:
#         liste.append(i)
#     else:
#         liste.append(liste[i-2]+liste[i-1])
# print(liste)


