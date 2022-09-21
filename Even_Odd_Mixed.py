n=int(input())
m=str(n)
c=0
c1=0
while n>0:
    r=n%10
    n=n//10
    if r%2==0:
        c+=1
    if r%2!=0:
        c1+=1
if c==len(m):
    print("Even")
elif c1==len(m):
    print("Odd")
else:
    print("Mixed")
    
    