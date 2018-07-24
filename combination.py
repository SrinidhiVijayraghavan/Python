#combinations of the given numbers
a=(input("Enter 1st number:"))
b=(input("Enter 2nd number:"))
c=(input("Enter 3rd number:"))
d=[]
d.append(a)
d.append(b)
d.append(c)
print("Combinations of given 3 numbers is")
for i in range(0,3):
    for j in range(0,3):
        for k in range(0,3):
            if(i!=j&j!=k&k!=i):
                print(d[i],d[j],d[k])