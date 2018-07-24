#Average of n numbers

n=input("Enter number of elements")
a=[]

for i in range(0,n):
 e=int(input("Enter the Element"))
 a.append(e)

b=(sum(a)/n)
print "Average"(b)  