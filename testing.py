from budget import Category, create_spend_chart

Food = Category("Food")
Food.deposit(1000, "initial deposit")
Food.withdraw(10.15, "groceries")
Food.withdraw(15.89, "restaurant and more food")
Clothing = Category("Clothing")
Clothing.deposit(500, "initial deposit")
Clothing.withdraw(13, "had to buy")
Clothing.withdraw(33, "magnific, must buy")
Food.transfer(50, Clothing)
Auto = Category("Auto")
Auto.deposit(1000, "initial deposit")
Auto.withdraw(20, 'some repairs')

Food.budget()
print()
create_spend_chart([Food, Clothing, Auto])
#### Only problem found is that if deposit or withdraw is larger than ####
#### 7 (6 in case of withdraw) digits then it will overflow ledge     ####
#### formatting.                                                      ####