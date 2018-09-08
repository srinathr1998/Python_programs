# armstrong no?
n=int(input("Enter a number :"))
s=0
l=n
c=0
while(n>0) :
    c=c+1
    n=n//10
n=l
while(n>0) :
    s=s+((n%10)**c)
    n=n//10
if(l==s):
    print('Armstrong number')
else :
    print('Not an armstrong number')
