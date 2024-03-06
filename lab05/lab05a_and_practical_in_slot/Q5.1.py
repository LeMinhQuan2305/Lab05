a = str(input("The output for the input line: "))
a = a.strip()
b = {}
for i in a:
    b[i]=b.get(i, 0) +1
with open("Q5.1.txt", "w") as c:
    for i, j in b.items():
        d = f"The letter ''{str(i)}'' appears {str(j)} time(s)\n"
        c.write(str(d))
with open("Q5.1.txt","r") as c:
    for i in c:
        print(i,end="")
