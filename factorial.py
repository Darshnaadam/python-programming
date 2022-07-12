from ast import Num
from math import factorial


num = int(input("Enter a Number: "))
factorial = 1
if num < 0:
    print("sorry, factorial does not exits for negative number")
elif num == 0:
    print("factorial of 0 is 1")
else:
    for i in range(1, num+1):
        factorial = factorial*i
    print("The factorial of ", num, "is", factorial)
