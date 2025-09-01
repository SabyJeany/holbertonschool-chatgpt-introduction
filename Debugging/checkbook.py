#!/usr/bin/python3
class Checkbook:
    def __init__(self):
        self.balance = 0.0

    def deposit(self, amount):
        if amount<0: 
            print("Amount must be non-negative")
            return
        self.balance+=amount
        print(f"Deposited ${amount:.2f}, Balance: ${self.balance:.2f}")

    def withdraw(self, amount):
        if amount<0:
            print("Amount must be non-negative")
            return
        if amount>self.balance:
            print("Insufficient funds")
            return
        self.balance-=amount
        print(f"Withdrew ${amount:.2f}, Balance: ${self.balance:.2f}")

    def get_balance(self):
        print(f"Balance: ${self.balance:.2f}")

def main():
    cb = Checkbook()
    while True:
        action = input("Action (deposit, withdraw, balance, exit): ").lower()
        if action=="exit": break
        elif action=="deposit":
            try:
                amt = float(input("Amount: "))
            except: print("Invalid number"); continue
            cb.deposit(amt)
        elif action=="withdraw":
            try:
                amt=float(input("Amount: "))
            except: print("Invalid number"); continue
            cb.withdraw(amt)
        elif action=="balance":
            cb.get_balance()
        else: print("Invalid action")

if __name__=="__main__":
    main()

