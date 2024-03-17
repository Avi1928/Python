n=int(input("Enter the no."))
f=0
for i in range(1,n+1):
    if(n%i==0):
        f=f+1
if(f==2):
    print("It is prime number.")
else:
    print("It is not a prime number.")


