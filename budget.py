class Category:
    
    def __init__(self, name):
        self.name = name 
        self.balance = 0
        self.ledger = []

    def deposit(self, amount, description):
        self.ledger.append({"amount": amount, "description": description})
        self.balance += amount

    def withdraw(self, amount, description):
        if self.check_funds(amount) == False:
            self.ledger.append({"amount": -amount, "description": description})
            self.balance -= amount
            return True
        else:
            return False

    def transfer(self, amount, other_category):
        if self.check_funds(amount) == False:
            self.withdraw(amount, f"Transfer to {other_category.name}")
            other_category.deposit(amount, f"Transfer from {self.name}")
            return True
        else:
            return False

    def get_balance(self):
        return self.balance

    def check_funds(self, amount):
        if amount > self.balance:
            return True
        else:
            return False

    def budget(self):
        print(f'{self.name:*^30}')
        for entry in self.ledger:
            print('{:<23}'.format(entry['description'][0:23]), end="")
            print('{:>7.2f}'.format(entry['amount']))
        print(f'Total: {self.balance}')


def create_spend_chart(categories):
    chart_content = []
    for category in categories:
        neg_bal = 0
        for entry in category.ledger:
            if entry['amount'] < 0:
                neg_bal += abs(entry['amount'])
        chart_content.append([category.name, neg_bal])

    sum = 0
    for item in chart_content:
        sum += item[1]
    
    for n in range(0, len(chart_content)):
        chart_content[n][1] = ((chart_content[n][1]/sum)*100) // 10 
    
    def check_line(dec):
        dec = dec // 10
        for item in chart_content:
            if dec <= item[1]:
                print(' o', end="")
       
        print()        

    for i in range(100, -10, -10):
        print(f'{i:>3}|', end="")
        check_line(i)
        
    dash = '---'*len(chart_content)
    print('   ', dash)
    longest_name = ''
    for item in chart_content:
        if len(item[0]) > len(longest_name) :
            longest_name = item[0]
    
    for item in chart_content:
        spaces = ' '*(len(longest_name)-len(item[0]))
        item[0] += spaces

    for n in range(0, len(longest_name)):
        print('     ', end="")
        for item in chart_content:
            print(item[0][n], '', end="")
        print()

