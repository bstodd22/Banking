from banking_pkg import account


def validate_name(name):
    return 1 <= len(name) <= 10


def validate_pin(pin):
    return len(pin) == 4


def atm_menu(name):
    print("")
    print("          === Automated Teller Machine ===          ")
    print("User: " + name)
    print("------------------------------------------")
    print("| 1.    Balance     | 2.    Deposit      |")
    print("------------------------------------------")
    print("------------------------------------------")
    print("| 3.    Withdraw    | 4.    Logout       |")
    print("------------------------------------------")
    print("          === Automated Teller Machine ===          ")


def get_valid_name():
    while True:
        name = input("Enter name to register (1 to 10 characters): ")
        if validate_name(name):
            return name
        else:
            print("Invalid name. Please enter a name with 1 to 10 characters.")


def get_valid_pin():
    while True:
        pin = input("Enter PIN to register (4 characters): ")
        if validate_pin(pin):
            return pin
        else:
            print("Invalid PIN. Please enter a 4-character PIN.")


name = get_valid_name()
pin = get_valid_pin()
balance = 0
print(f"{name} has been registered with a balance of ${balance}")

while True:
    name_to_validate = input("Enter name: ")
    pin_to_validate = input("Enter PIN: ")
    if name_to_validate == name and pin_to_validate == pin:
        print("Login successful!")
        break
    else:
        print("Invalid credentials!")

while True:
    atm_menu(name)
    option = int(input("Choose an option: "))
    if option == 1:
        account.show_balance(balance)
    elif option == 2:
        balance = account.deposit(balance)
        account.show_balance(balance)
    elif option == 3:
        balance = account.withdraw(balance)
        account.show_balance(balance)
    elif option == 4:
        account.logout(name)
        break
    else:
        print("Invalid option, please try again.")
