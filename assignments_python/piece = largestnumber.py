piece = int(input("How many numbers will you enter?"))
start = 1
list2 = []
while start <= piece:
    print_piece = int(input("Please enter the number :"))
    list2.append(print_piece)
    start += 1
list2.sort()
print(list2[-1])


# list1 = []
# for i in range(1, piece+1):
#     print_piece = int(input("Please enter the number :"))
#     i = print_piece
#     list1.append(i)
# a = sorted(list1)
# print(a[-1])
    







# while start <= piece:
#     print(print_piece)
#     start += 1