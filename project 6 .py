text = "X-DSPAM-Confidence:    0.8475";
x=text.find('0.8475')
print(x)
y=text.find('5')
print(y)
z=(text[x:y+1])
a=float(z)
print(a)
