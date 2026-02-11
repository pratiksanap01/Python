# WAP to find the greatest of 3 numbers entered by user 

num1 = int(input("Number 1 :"))
num2 = int(input("Number 2 :"))
num3 = int(input("Number 3 :"))

if(num1 > num2 and num1 > num3):
    print("Number 1 is greatest")
elif(num2 > num3):
    print("Number 2 is greatest")
else:
    print("Number 3 is greatest")