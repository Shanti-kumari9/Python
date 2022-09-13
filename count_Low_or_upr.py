str1 = input("Enter any string")
l=0
u=0
for i in str1:
  if i.islower()==True:
        l = l+1
  if i.isupper() == True:
        u = u+1
print("Total uppercase characters are--",u)
print("Total lowercase characters are--",l)