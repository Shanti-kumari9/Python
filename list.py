a=[1,0,0,2,11,0,7,0,9]
i=0
d=[]
e=[]
while i<len(a):
    if a[i] == 0:
        d.append(a[i])
    else:
        e.append(a[i])
    i=i+1
e.append(d)
a.extend(d)
print(e)
# check how many 0 we have in list a and append all  0 in anyother list.

