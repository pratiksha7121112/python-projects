while True:
    
    print("OPTIONS")
    print("")
    print("1. KM to Mile")
    print("")
    print("2. Mile to KM")
    print("")
    print("3. KG to Pound")
    print("")
    print("4. Pound to KG")
    print("")
    print("5. Quit")
    print("")
    choice = input("Select an option: ")
    if choice == "1":
        print("")
        km = int(input("Enter your number: "))
        result_1 = km * 0.621371
        print("")
        print("Result:",result_1,"Miles")
        print("")
    elif choice == "2":
        print("")
        Mile = int(input("Enter your number: "))
        result_2 = Mile / 1.60934
        print("")
        print("Result:",result_2,"KMs")
        print("")
    elif choice == "3":
        print("")
        kg = int(input("Enter your number: "))
        result_3 = kg * 2.20462
        print("")
        print("Result:",result_3,"Pounds")
        print("")
    elif choice == "4":
        print("")
        pound = int(input("Enter your number: "))
        result_4 = pound /  0.453592 
        print("")
        print("Result:",result_4,"KGs")
        print("")
    elif choice == "5":
        break
    else:
        print("Invalid option")
        print("")        