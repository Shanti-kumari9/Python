
print("what do u want to do...?")
print(1,"Addtion", 2,"Subtraction",3,"Multplication",4,"Division")
choice = input("enter you choice: ")
num1=int(input("enter the number1....:"))
num2=int(input("enter the number 2.....:"))
if choice =='1':
    print(num1+num2)
elif choice=='2':
    print(num1-num2)
elif choice=='3':
    print(num1*num2)
elif choice == '4':
    print(num1/num2)
else:
    print("Invailed choice..")