l=[]
n=int(input("enter n: "))
for i in range(n):
    e=int(input("enter a value : " ))
    l.append(e)

min=l[0]

for i in range(1,n):
   if l[i]<min:
      min=l[i]
print( "min value is :",min)      

max=l[0]

for i in range(1,n):
   if l[i]>max:
      max=l[i]
print("max value is :",max)      

