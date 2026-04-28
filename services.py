balance = 0
transactions = []

def check_balance():
    return balance

def deposit(amount):
    global balance
    balance += amount
    transactions.append(f"Deposited ₹{amount}")

def withdraw(amount):
    global balance
    if amount > balance:
        return "Insufficient balance"
    balance -= amount
    transactions.append(f"Withdrew ₹{amount}")
    return "Success"

def get_transactions():
    return transactions