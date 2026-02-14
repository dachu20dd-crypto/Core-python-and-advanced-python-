a=int(input("enter the number"))
temp=a
total=0
while a!=0:
    r=a%10
    total=total+(r*r*r)
    a=a//10

if(total==temp):
    print("it is armstrong number")
else:
    print("it is not an armstrong number")
