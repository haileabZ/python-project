x=int(input("enter n number"))
lists=list(range(1,x+1))
print(lists)
for i in lists:

   if i%3==0 and i%5==0:
      lists[i-1]="fizzBuzz"
   elif i%3==0 :
       lists[i-1]="fizz"
   elif i%5==0 :
       lists[i-1]="buzz"

print(lists)
