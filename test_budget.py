from BudgetClass import Budget

def test_budget_1():
    test_object = Budget(100)
    assert test_object.balance == 100
    
def test_budget_2():
    test_object = Budget(100)
    test_object.deposit(50)
    assert test_object.balance == 150
    
def test_budget_3():
    test_object = Budget(100)
    test_object.withdraw(50)
    assert test_object.balance == 50
    
def test_budget_4():
    test_object1 = Budget(100)
    test_object2 = Budget(100)
    test_object1.deposit(test_object2.withdraw(50))
    assert test_object1.balance == 150
    assert test_object2.balance == 50