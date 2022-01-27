x=int(input("Enter x:"))
y=int(input("Enter y:"))
z=int(input("Enter z:"))
n=int(input("Enter n:"))

a=[[i,j,k] for i in range(3) for j in range(3) for k in range(3) if i+j+k!=n]
print (a)

