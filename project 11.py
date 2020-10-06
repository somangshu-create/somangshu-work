#Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages. 
#The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. 
#The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. 
#After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.

name = input("Enter file:")
#baiscally the next line ensures that only a specific file gets in the further programs 
if len(name) < 1 : name = "mbox-short.txt"
x = open(name)
z=dict()

#program for dictionary
for line in x:
    if line.startswith('From'):
        if line.startswith("From:"):
            continue
        
        a=line.split()
        y=(a[1])
        
        
    #collecting items for the dictionary
        d=y.split()
        #print(d)
    #adding items in the dictionary
        for email in d:
            z[email]=z.get(email,0)+1
#final dictionary output
            #print(z)
#maximum loop for the the dictionary
ecount=None
cemail=None
for b,c in z.items():
    if ecount is None or c>ecount:
        ecount=c
        cemail=b
    print(cemail,ecount)                


  
