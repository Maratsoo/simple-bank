# 
# Darbības ar masīviem - https://www.w3schools.com/python/python_arrays.asp
# Datu tipi, mekle float - https://www.w3schools.com/python/python_datatypes.asp
# Pārbaudēm izmanto if...else - https://www.w3schools.com/python/python_conditions.asp
# Cipari https://www.w3schools.com/python/python_numbers.asp
# 

balance = 0

while True:
    print("\nBanking Options:")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        # papildini kodu šeit
        x = float(input("deposit amount: "))
        balance += x
        print("Deposit of {x} successful. New balance: {balance}")
        pass
    elif choice == '2':
        # papildini kodu šeit
        x = int(input("Enter your choice (1-4): "))
        if balance >= x:
            print("Withdrawal of {x} successful. New balance: {balance}")
        else:
            print("Not enough money in the balance.")
        pass
    elif choice == '3':
        # papildini kodu šeit
        print("here is your balance: {balance} ")
        pass
    elif choice == '4':
        print("Exiting the banking system. Thank you!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 5.")
