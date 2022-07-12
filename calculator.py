# calculate item prices of a kirana store 

sum = 0
while(True):
    UserInput = input("Enter the Item price or enter q for Your total Bill : \n")
    if (UserInput != 'q'):
     sum = sum + int(UserInput)

    else:
        print(f"Your total Bill price is {sum}")
        break
    

