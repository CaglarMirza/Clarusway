
value = input("Please write a number : ")
if  value.isnumeric():
    if int(value) == 1:
        print(f"{value} is not a prime number")
    # elif int(value) == 2:
    #     print(f"{value} is a prime number")
    else:
        for i in range(2,int(value)):
            if (int(value)%i) == 0:
                print(f"{value} is NOT a prime number.")
                break
        else:
            print(f"{value} is a prime number.")
else:
    print("invalid value, try again")
  
    