# Program to test the entered number is within 100 or 1000 or 2000

num=int(input("Enter any numerical value: "))

if (num<=100):
    print("Your number is within 100")
elif (num<=1000):
    print("Your number is within 1000")
elif (num<=2000):
    print("Your number is within 2000")
else:
    print("invalid number")