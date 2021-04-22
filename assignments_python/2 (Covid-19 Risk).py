age=  input("Are you a cigarette addict older than 75 years old?").lower().strip()
chronic = input("Do you have a severe chronic disease?").lower().strip()
immune = input("Is your immune system too weak?").lower().strip()

if age == "yes":
    print('in risk')
elif age == "no":
    if chronic == "yes":
        print('in risk')
    elif chronic == "no":
        if immune == "yes":
            print("in risk")
        elif immune == "no":
             print(" yasiyosun bu hayati")
        else:
            print('gecerli immue deger girin')
    else:
        print('gecerli chorinic deger girin')
else:
    print('gecerli age deger girin')

#########################

while True:
    age=  input("Are you a cigarette addict older than 75 years old?").lower().strip()
    if age == "yes":
        age = True
        break
    elif age == "no":
        age = False
        break
    
    print("lusfen  ", age, " yerine 'Yes' yada 'No' bir deger girin yazin")
            
print(age)
############################

# liste = [age, chronic, immune]
# liste2 = []

# for i in range(len(liste)):
#     if liste[i] == "yes"
#         liste2.insert(i, True)
#     elif liste[i] == "no":
#         liste2.insert(i, False)  

# if len(liste2) != len(liste):
#     print("lutfen tum degerleri dogru giriniz")
# elif True in  liste2:
#     print("You are in risky group")
# else:
#     print("You are not in risky group")
# risk = liste2[0] or liste2[1] or liste2[2]

###############################
'''
if age == "yes":
    age = True
elif age == "no":
    age = False

if chronic == "yes":
    chronic = True
elif chronic == "no":
    chronic = False

if immune == "yes":
    immune = True
elif immune == "no":
    immune = False

booldeger = [age, chronic, immune]
bool1 = bool(age or chronic or immune)
if bool1 == True:
    print("You are in risky group")
elif bool1== False:
    print("You are not in risky group")

print(booldeger)
'''





