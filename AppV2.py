from BudgetClass import Budget

food = Budget(0)
entertainment = Budget(0)
clothing = Budget(0)


def edit_food():
    user_choice = input("would you like to 1. withdraw or 2. deposit to your food budget? press enter to cancel: ")
    if user_choice == "1":
        new_budget = int(input("How much would you like to withdraw? "))
        food.withdraw(new_budget)
    elif user_choice == "2":
        new_budget = int(input("How much would you like to deposit? "))
        food.deposit(new_budget)



def edit_entertainment():
    user_choice = input("would you like to 1. withdraw or 2. deposit to your entertainment budget? press enter to cancel: ")
    if user_choice == "1":
        new_budget = int(input("How much would you like to withdraw? "))
        entertainment.withdraw(new_budget)
    elif user_choice == "2":
        new_budget = int(input("How much would you like to deposit? "))
        entertainment.deposit(new_budget)
    



def edit_clothing():
    user_choice = input("would you like to 1. withdraw or 2. deposit to your clothing budget? press enter to cancel: ")
    if user_choice == "1":
        new_budget = int(input("How much would you like to withdraw? "))
        clothing.withdraw(new_budget)
    elif user_choice == "2":
        new_budget = int(input("How much would you like to deposit? "))
        clothing.deposit(new_budget)
    



def food_to_clothing():
    new_budget = input("How much would you like to move? ")    
    clothing.deposit(food.withdraw(new_budget))

def food_to_entertainment():
    new_budget = input("How much would you like to move? ")    
    entertainment.deposit(food.withdraw(new_budget))

def entertainment_to_clothing():
    new_budget = input("How much would you like to move? ")    
    clothing.deposit(entertainment.withdraw(new_budget))

def entertainment_to_food():
    new_budget = input("How much would you like to move? ")    
    food.deposit(entertainment.withdraw(new_budget))

def clothing_to_entertainment():
    new_budget = input("How much would you like to move? ")    
    entertainment.deposit(clothing.withdraw(new_budget))
    
def clothing_to_food():
    new_budget = input("How much would you like to move? ")    
    food.deposit(clothing.withdraw(new_budget))

def edit_file():
    budget_file = open("budget.txt", "w")
    # writes the food budget to the file 
    food_budget = ("your food budget is: "+ str(food))
    budget_file.write(food_budget)
    
    #writes the entertainment budget to the file
    entertainment_budget = ("\n your entertainment budget is: " + str(entertainment))
    budget_file.write(entertainment_budget)
    
    #writes the clothing budget to the file
    clothing_budget = ("\nyour clothing budget is: " + str(clothing))    
    budget_file.write(clothing_budget)
    budget_file.close()



def main():
    control = True
    while control:
        user_choice = input("which budget would you like to work with? 1. food 2. entertainment or 3. clothing. Press enter to cancel: ")
        # edits the balance within the food object
        if user_choice == "1":
            user_choice = input("would you like to 1. withdraw or deposit or 2. transfer funds from elsewhere? ")
            if user_choice == "1":
                edit_food()
            elif user_choice == "2":
                user_choice = input("Would you like to move funds from 1. clothing or 2. entertainment? ")
                if user_choice == "1":
                    clothing_to_food()
                elif user_choice == "2":
                    entertainment_to_food()
                    
                    
        #edits the balance in the entertainment object
        elif user_choice == "2":
            user_choice = input("would you like to 1. withdraw or deposit or 2. transfer funds from elsewhere? ")
            if user_choice == "1":
                edit_entertainment()
            elif user_choice == "2":
                user_choice = input("Would you like to move funds from 1. clothing or 2. food? ")
                if user_choice == "1":
                    clothing_to_entertainment()
                elif user_choice == "2":
                    food_to_entertainment()
                    
                    
            # edits the clothing object
            elif user_choice == "3":
                user_choice = input("would you like to 1. withdraw or deposit or 2. transfer funds from elsewhere? ")
                if user_choice == "1":
                    edit_clothing()
                elif user_choice == "2":
                    user_choice = input("Would you like to move funds from 1. entertainment or 2. food? ")
                    if user_choice == "1":
                        entertainment_to_clothing()
                    elif user_choice == "2":
                        food_to_clothing()       
        else:
            control = False
         


                    
main()              
edit_file()

