
#Take input from user & give factorial of given number

num=int(input("Enter a num:"))
fact=1

for i in range (1,num + 1):
    fact=fact*i
print("The factorial of ", num, "is",fact)