def show_balance(balance):
    print(balance)


def deposit(balance):
    amount = float(input("Enter amount to deposit: "))
    new_balance = balance + amount
    return new_balance


def withdraw(balance):
    amount = float(input("Enter amount to withdraw: "))
    new_balance = balance - amount
    return new_balance


def logout(name):
    print(f"Goodbye, {name}!")
