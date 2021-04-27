value = input("Please enter a integer number : ")
list_sum = []
if not (value.isnumeric()):
    print(f" '{value}' is an invalid entry. Don't use non-numeric, float, or negative values!")
else:
    for i in list(value):
        list_sum.append(int(i)**len(value))

    if sum(list_sum) == int(value):
        print(f"'{value}' is an Armstrong number")
    else:
        print(f"'{value}' is not an Armstrong number")


        # whilenin icine alip tekrar sordurmayi yap