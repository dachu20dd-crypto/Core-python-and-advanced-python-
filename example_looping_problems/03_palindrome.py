a=int(input("enter the number"))
temp=a
rev=0
while a!=0:
    rem=a%10
    rev=rev*10+rem
    a=a//10

if(rev==temp):
    print("it is a palindrome number")
else:
    print("it is not palindrome number")
