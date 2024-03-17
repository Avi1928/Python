import math
num=int(input("Enter the no. :-"))
preserve=num
sum=0
while(num!=0):
    rem=num%10
    sum= pow(rem,3)+sum
    num=num//10
if(preserve == sum):    
    print(preserve ,"is a armstrong number.")  
else:
    {
      print(preserve ,"is not a armstrong number.")
    }