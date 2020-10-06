fname = input("Enter file name: ")
fh = open(fname)
a=fh.read()
x = list()
y=a.split()
for line in y:
    if line not in x :
        x.append(line)
    x.sort()
print(x)   

