import services

while True:
    print("\n--- ATM MENU ---")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Statement")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        print("Balance:", services.check_balance())

    elif choice == "2":
        try:
            amt = int(input("Enter amount: "))
            print(services.deposit(amt))
        except ValueError:
            print("Invalid input")

    elif choice == "3":
        try:
            amt = int(input("Enter amount: "))
            print(services.withdraw(amt))
        except ValueError:
            print("Invalid input")

    elif choice == "4":
        for t in services.get_transactions():
            print(t)

    elif choice == "5":
        print("Thank you for using ATM")
        break

    else:
        print("Invalid choice")