lst = []

while True:
    print("1. Add")
    print("2. Remove")
    print("3. Display")
    print("4. Quit")

    choice = input("Enter choice: ")

    if choice == "1":
        val = input("Integer: ")
        try:
            num = int(val)
            lst.append(num)
            print("List after adding:", lst)
        except:
            print("Invalid input")

    elif choice == "2":
        if len(lst) == 0:
            print("List is empty")
        else:
            val = input("Integer: ")

            try:
                num = int(val)
                if num in lst:

                    lst.remove(num)
                    print("List after removing:", lst)
                else:
                    print("Element not found")
            except:
                print("Invalid input")

    elif choice == "3":
        if len(lst) == 0:
            print("List is empty")
        else:
            print(lst)

    elif choice == "4":
        break

    else:
        print("Invalid choice")