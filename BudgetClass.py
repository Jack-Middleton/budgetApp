class Budget:
    def __init__(self, balance):
        self.balance = balance
    
    def __repr__(self):
        return f"{self.balance}"
    
    def deposit(self, amount):
        self.balance = self.balance + amount
        return amount
        
    def withdraw(self, amount):
        self.balance = self.balance - amount
        return amount
    