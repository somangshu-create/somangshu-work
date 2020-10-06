#Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. 
#You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.

#From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008

#Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.
name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
x = open(name)
a=dict()
p=list()
#creating a dictionary
for line in x:
	if line.startswith('From'):
		if line.startswith('From:'):
			continue
		y=line.split()
		z=(y[5])
		#print(z)
		b=(z[0:2])
		#print(b)
		#parsed out the hour part
		#right till here
		#adding items to the list
		p.append(b)
#print(p)
#now  adding items/tuples to the dictionary
for c in p:
    a[c]=a.get(c,0)+1		
#sorting the tuples
d=sorted(a.items())
for (e,f) in d:
    print(e,f)    		
		
    
    
 
