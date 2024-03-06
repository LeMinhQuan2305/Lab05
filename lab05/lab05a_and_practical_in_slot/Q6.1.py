n = int(input("Enter number"))
a = []
for i in range(0,n):
    b = int(input())
    a.append(b)
print(a)

for i in range(n):
    minval = 0
    index = 0
    minval = min(a[i:n])
    index = a.index(minval)
    if minval <= a[i]:
        a[i],a[index] = a[index],a[i]
    print(a)  
