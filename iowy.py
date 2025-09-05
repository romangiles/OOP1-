while 1:
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Quit")



    option = input("Enter your operation")

    if option == "1":
        n1 = int(input("enter number"))
        n2 = int(input("enter number"))
        print(n1+n2)

    elif option == "2":
        n1 = int(input("enter number"))
        n2 = int(input("enter number"))
        print(n1-n2)

    elif option == "3":
        n1 = int(input("enter number"))
        n2 = int(input("enter number"))
        print(n1*n2)

    elif option == "4":
        n1 = int(input("enter number"))
        n2 = int(input("enter number"))
        print(n1/n2)

    elif option == "5":
        break

