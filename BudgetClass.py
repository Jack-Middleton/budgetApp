"""
needed:
budget class 
depositing funds function
withdrawing funds function
"""


class Budget:
    def __init__(self, balance):
        self.balance = balance
    
    def __repr__(self):
        return f"{self.balance}"
    
    def deposit(self, amount):
        self.balance = self.balance + amount
        return self.balance
        
    def withdraw(self, amount):
        self.balance = self.balance - amount
        return self.balance

















    # def balance_food(self):    
    #     withdraw_f = str(input("Would you like to withdraw from food? Y/N: ").upper())
    #     if withdraw_f == "Y" or withdraw_f == "YES":
    #         amount_f = - int(input("how much would you like to withdraw? "))
    #         return amount_f
    #     else:
    #         deposit_f = str(input("Would you like to deposit to food? Y/N: ").upper())
    #         if deposit_f == "Y" or deposit_f == "YES":
    #             amount_f = + int(input("how much would you like to deposit? "))
    #         else:
    #             amount_f = 0
    #             return amount_f
            
    # def balance_entertainment(self):
    #     withdraw_e = str(input("Would you like to withdraw from entertainment? Y/N: ").upper())
    #     if withdraw_e == "Y" or withdraw_e == "YES":
    #         amount_e = - int(input("how much would you like to withdraw? "))
    #         return amount_e
    #     else:
    #         deposit_e = str(input("Would you like to deposit to entertainment? Y/N: ").upper())
    #         if deposit_e == "Y" or deposit_e == "YES":
    #             amount_e = + int(input("how much would you like to deposit? "))
    #         else:
    #             amount_e = 0
    #             return amount_e
            
    # def balance_clothing(self):
    #     withdraw_c = str(input("Would you like to withdraw from clothing? Y/N: ").upper())
    #     if withdraw_c == "Y" or withdraw_c == "YES":
    #         amount_c = - int(input("how much would you like to withdraw? "))
    #         return amount_c
    #     else:
    #         deposit_c = str(input("Would you like to deposit to clothing? Y/N: ").upper())
    #         if deposit_c == "Y" or deposit_c == "YES":
    #             amount_c = + int(input("how much would you like to deposit? "))
    #         else:
    #             amount_c = 0
    #             return amount_c
    
