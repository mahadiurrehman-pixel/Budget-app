class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=''):
        self.ledger.append({'amount': amount, 'description': description})

    def withdraw(self, amount, description=''):
        if self.check_funds(amount):
            self.ledger.append({'amount': -amount, 'description': description})
            return True
        return False

    def get_balance(self):
        return sum(item['amount'] for item in self.ledger)

    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, f'Transfer to {category.name}')
            category.deposit(amount, f'Transfer from {self.name}')
            return True
        return False

    def check_funds(self, amount):
        return amount <= self.get_balance()

    def __str__(self):
        title = f'{self.name:*^30}\n'
        items = ''
        for item in self.ledger:
            description = item['description'][:23]
            amount = f'{item["amount"]:.2f}'[:7]
            items += f'{description:<23}{amount:>7}\n'
        total = f'Total: {self.get_balance():.2f}'
        return title + items + total


def create_spend_chart(categories):
    # Calculate total spent per category (withdrawals only)
    spent_amounts = []
    for category in categories:
        spent = 0
        for item in category.ledger:
            if item['amount'] < 0:
                spent += -item['amount']
        spent_amounts.append(spent)
    
    total_spent = sum(spent_amounts)
    # Percentages rounded down to the nearest 10
    percentages = [int((amount / total_spent) * 100 // 10) * 10 for amount in spent_amounts]
    
    chart = 'Percentage spent by category\n'
    
    # Y-axis labels and bars from 100 down to 0
    for i in range(100, -1, -10):
        chart += f'{i:>3}| '
        for percent in percentages:
            if percent >= i:
                chart += 'o  '
            else:
                chart += '   '
        chart += '\n'
    
    # Horizontal line
    chart += '    ' + '-' * (3 * len(categories) + 1) + '\n'
    
    
    max_length = max(len(category.name) for category in categories)
    names = [category.name.ljust(max_length) for category in categories]
    
    for i in range(max_length):
        chart += '    '
        for name in names:
            chart += ' ' + name[i] + ' '
        chart += ' '
        if i < max_length - 1:
            chart += '\n'
    
    return chart