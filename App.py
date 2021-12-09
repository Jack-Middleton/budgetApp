from BudgetClass import Budget


def budget():
    budget_file = open("budget.txt", "w+")
    create = True
    while create:
        control = int(input("enter an option, 1.create a food budget, 2.create entertainment budget, 3.create clothing budget or 4. edit budgets: "))
        if control == 1:
            new_budget = int(input("input starting budget for food: "))
            food = Budget(new_budget)
            food_budget = (str(food))
            budget_file.write(food_budget)
        elif control == 2:
            new_budget = int(input("input starting budget for entertainment: "))
            entertainment = Budget(new_budget)
            entertainment_budget = ("\n" + str(entertainment))
            budget_file.write(entertainment_budget)        
        elif control == 3:
            new_budget = int(input("enter starting clothing budget: "))
            clothing = Budget(new_budget)
            clothing_budget = ("\n" + str(clothing))    
            budget_file.write(clothing_budget)     
        else:
            break

    edit = True
    while edit:
        outer_control = int(input("enter an option, 1. work with food budget, 2. work with entertainment budget or 3. work with clothing budget or 4. Cancel: "))
        if outer_control == 1:
            food_control = int(input("What would you like to do, 1. deposit funds to food, 2. withdraw funds from food, 3. transfer funds from elsewhere or 4. Cancel: "))
            # options 1 and 2 will deposit and withdraw funds from the food object
            if food_control == 1:
                new_budget = int(input("how much would you like to deposit to food? "))
                food.deposit(new_budget)
                budget_file.seek(0)
                food_budget = budget_file.readline()
                budget_file.seek(0)
                budget_file.rstrip(10)
                food_budget = int(food_budget)
                food_budget = (food_budget + new_budget)
                food_budget = str(food_budget)
                budget_file.write(food_budget)
            elif food_control == 2:
                new_budget = int(input("how much would you like to withdraw? "))
                food.withdraw(new_budget)
                budget_file.seek(0)
                food_budget = budget_file.readline()
                food_budget = str(new_budget)
                budget_file.write(food_budget)
            elif food_control == 3:
                # this allows the user to transfer funds from entertainment or clothing and add them to food
                transfer = int(input("where would you like to transfer funds from, 1. entertainment or 2. clothing or 3. Cancel: "))
                if transfer == 1:
                    new_budget = int(input(("how much would you like to move? ")))
                    entertainment.withdraw(new_budget)
                    food.deposit(new_budget)
                    #adds funds to food_budget
                    budget_file.seek(0)
                    food_budget = budget_file.readline()
                    food_budget = str(new_budget)
                    budget_file.write(food_budget)
                    #removes funds from entertainment_budget
                    budget_file.seek(0)
                    budget_file.readline()
                    entertainment_budget = budget_file.readline()
                    entertainment_budget = str(new_budget)
                    budget_file.write(entertainment_budget)
                elif transfer == 2:
                    new_budget = int(input(("how much would you like to move? ")))
                    clothing.withdraw(new_budget)
                    food.deposit(new_budget)
                    #adds funds to food
                    budget_file.seek(0)
                    food_budget = budget_file.readline()
                    food_budget = str(new_budget)
                    budget_file.write(food_budget)
                    #removes funds from clothing
                    budget_file.seek(0)
                    budget_file.readline()
                    budget_file.readline()
                    clothing_budget = budget_file.readline()
                    clothing_budget = str(new_budget)
                    budget_file.write(clothing_budget)
                else:
                    continue
            else:
                continue
        elif outer_control == 2:
            entertainment_control = int(input("What would you like to do, 1. deposit funds to entertainment, 2. withdraw funds from entertainment, 3. transfer funds from elsewhere or 4. Cancel: "))
            # options 1 and 2 will deposit and withdraw funds from the entertainment object
            if entertainment_control == 1:
                new_budget = int(input("how much would you like to deposit to entertainment? "))
                entertainment.deposit(new_budget)
                budget_file.seek(0)
                budget_file.readline()
                entertainment_budget = budget_file.readline()
                entertainment_budget = str(new_budget)
                budget_file.write(entertainment_budget)
            elif entertainment_control == 2:
                new_budget = int(input("how much would you like to withdraw? "))
                entertainment.withdraw(new_budget)
                budget_file.seek(0)
                budget_file.readline()
                entertainment_budget = budget_file.readline()
                entertainment_budget = str(new_budget)
                budget_file.write(entertainment_budget)
            elif entertainment_control == 3:
                # this allows the user to transfer funds from food or clothing and add them to entertainment
                transfer = int(input("where would you like to transfer funds from, 1. food or 2. clothing or 3. Cancel: "))
                if transfer == 1:
                    new_budget = int(input(("how much would you like to move? ")))
                    food.withdraw(new_budget)
                    entertainment.deposit(new_budget)
                    # add funds to entertainment budget
                    budget_file.seek(0)
                    budget_file.readline()
                    entertainment_budget = budget_file.readline()
                    entertainment_budget = str(new_budget)
                    budget_file.write(entertainment_budget)
                    # remove funds from food budget
                    budget_file.seek(0)
                    food_budget = budget_file.readline()
                    food_budget = str(new_budget)
                    budget_file.write(food_budget)
                elif transfer == 2:
                    new_budget = int(input(("how much would you like to move? ")))
                    clothing.withdraw(new_budget)
                    entertainment.deposit(new_budget)
                    #add funds to entertainment budget
                    budget_file.seek(0)
                    budget_file.readline()
                    entertainment_budget = budget_file.readline()
                    entertainment_budget = str(new_budget)
                    budget_file.write(entertainment_budget)
                    # removes funds from clothing budget
                    budget_file.seek(0)
                    budget_file.readline()
                    budget_file.readline()
                    clothing_budget = budget_file.readline()
                    clothing_budget = str(new_budget)
                    budget_file.write(new_budget)
                else:
                    continue
            else:
                continue
        elif outer_control == 3:
            clothing_control = int(input("What would you like to do, 1. deposit funds to clothing, 2. withdraw funds from clothing, 3. transfer funds from elsewhere or 4. Cancel: "))
            # options 1 and 2 will deposit and withdraw funds from the clothing object
            if clothing_control == 1:
                new_budget = int(input("how much would you like to deposit to clothing? "))
                clothing.deposit(new_budget)
                budget_file.seek(0)
                budget_file.readline()
                budget_file.readline()
                clothing_budget = budget_file.readline()
                clothing_budget = str(new_budget)
                budget_file.write(new_budget)
            elif clothing_control == 2:
                new_budget = int(input("how much would you like to withdraw? "))
                clothing.withdraw(new_budget)
                budget_file.seek(0)
                budget_file.readline()
                budget_file.readline()
                clothing_budget = budget_file.readline()
                clothing_budget = str(new_budget)
                budget_file.write(new_budget)
            elif clothing_control == 3:
                # this allows the user to transfer funds from entertainment or food and add them to clothing
                transfer = int(input("where would you like to transfer funds from, 1. entertainment or 2. food or 3. Cancel: "))
                if transfer == 1:
                    new_budget = int(input(("how much would you like to move? ")))
                    entertainment.withdraw(new_budget)
                    clothing.deposit(new_budget)
                    # add funds to clothing budget
                    budget_file.seek(0)
                    budget_file.readline()
                    budget_file.readline()
                    clothing_budget = budget_file.readline()
                    clothing_budget = str(new_budget)
                    budget_file.write(new_budget)
                    # remove funds from entertainment
                    budget_file.seek(0)
                    budget_file.readline()
                    entertainment_budget = budget_file.readline()
                    entertainment_budget = str(new_budget)
                    budget_file.write(entertainment_budget)
                elif transfer == 2:
                    new_budget = int(input(("how much would you like to move? ")))
                    food.withdraw(new_budget)
                    clothing.deposit(new_budget)
                    # add funds to clothing budget
                    budget_file.seek(0)
                    budget_file.readline()
                    budget_file.readline()
                    clothing_budget = budget_file.readline()
                    clothing_budget = str(new_budget)
                    budget_file.write(new_budget)
                    # remove funds from food budget
                    budget_file.seek(0)
                    food_budget = budget_file.readline()
                    food_budget = str(new_budget)
                    budget_file.write(food_budget)
                else:
                    continue
            else:
                continue
        else:
            print(f"your food budget is {food.balance}, your entertainment budget is {entertainment.balance} and your clothing balance is {clothing.balance}.")
            askYesNo = input("would you like to continue making changes? Y/N: ").upper()
            if askYesNo == "N" or askYesNo == "NO":
                edit = False
                budget_file.close()

        
budget()