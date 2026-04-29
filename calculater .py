num1 = float(input("enter first number:"))
num2 = float(input("enter second mumber:"))
print("choice operation:")
print("1 . Add(+)")
print("2 . Subtract(-)")
print("3 . Multiply(*)")
print("4 . Divide(/)")
choice = input("enter choice(1/2/3/4):")
if choice == '1':
    print(num1 + num2)
elif choice == '2':
    print(num1 - num2)
elif choice == '3':
    print(num1 * num2)
elif choice == '4':
    print(num1 / num2)
else:
    print("invalid")
    


