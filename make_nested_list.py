a=[2,3,5,6,7,8]
b=[]
i=0
while i<len(a)-1:
    c=[]
    c.append(a[i])
    c.append(a[i+1])
    b.append(c)
    i+=2
print(b)


