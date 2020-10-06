fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"
count=0
fh = open(fname)
for line in fh:
    line.rstrip()
    if line.startswith('From'):
        if line.startswith('From:'):
            continue
        x=line.split()
        print(x[1])
        count=count+1
print(count)
    
