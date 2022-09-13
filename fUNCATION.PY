# Q10. Which function of string return the numerical value?
# Hide Answer
# Ans. len()  

# =================================================================================

# Q2. isalpha() returns True if the string contains only alphabet.(T/F)

# Hide Answer
# Ans. True

# ===============================================================================
# 
# DIFFERENT between lower() and islower()?

# Hide Answer
# Ans. lower() function converts the given string in lowercase while islower() check whether given string is in lowercase r not.


# Q8. Write a program to accept a string and convert it into lowercase.

# Hide Answer
# Ans. 
# str1 = input("Enter any string")
# print(str1.lower())

# ===============================================================================================

# Q9. Write a program to count the number of lowercase and uppercase character in a 
# string accepted from the user.

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
