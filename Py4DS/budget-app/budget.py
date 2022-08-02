class Category:

    def __init__(self,category):
        self.category = category
        self.ledger = []

    def __str__(self):
        """
        When object is printed, formats the ledger into a print statement
        """
        output = self.category.center(30,"*")
        for item in self.ledger:
            output += f"\n{str(item['description'][:23]).ljust(23,' ')}{(str('{:.2f}'.format(item['amount']))).rjust((7),' ')}"
        output += f"\nTotal: {self.get_balance()}"
        return output


    def deposit(self,amount,description=''):
        """
        Adds to the ledger a
        deposit statement, with an amount and description
        """
        self.ledger.append({'amount': amount, 'description': description})


    def withdraw(self,amount,description=''):
        """
        Adds to the ledger a
        withdrawal statement, with an amount and description
        """         
        if self.check_funds(amount):
            self.ledger.append({'amount': -amount, 'description': description})
            return True
        else: 
            return False


    def get_balance(self):
        """
        Returns the current balance based on the items in the ledger
        """
        return sum(item['amount'] for item in self.ledger)


    def transfer(self,amount,category):
        """
        Transfer an amount from the current category, to another
        """
        if self.check_funds(amount):
            category.deposit(amount,f"Transfer from {self.category}")
            self.withdraw(amount,f"Transfer to {category.category}")
            return True
        else: 
            return False


    def check_funds(self,amount):
        """
        Checks if there are enough funds for the withdraw and transfer
        methods to process
        """
        if amount > self.get_balance():
            return False
        else:
            return True



def create_spend_chart(categories):
    bar_chart = 'Percentage spent by category'
        
    # Find the total of all spendings in each category,
    spendings_dict = {}
    for category in categories:
        spend = 0
        for item in category.ledger:
            if item['amount'] < 0:
                spend += item['amount']
        spendings_dict[category.category] = float(str('{:.2f}'.format(spend)))


    # total spent from all categories
    total_spent = sum(spendings_dict.values())


    # calculates spend percentage and rounds down to the nearest 10
    spend_percentages = {}
    for category in categories:
        percentage = (spendings_dict[category.category] / total_spent) * 100
        if int(percentage) > 9:
            spend_percentages[category.category] = int(str(percentage)[0] + '0')
        else:
            spend_percentages[category.category] = 0


    # adds each line of the graph to a list
    lines = []
    for n in reversed(range(0, 110, 10)):
        lines.append(f"\n{str(n).rjust(3)}| ")


    # adds a marker to each line if the number on the line
    # is equal to or less than the percentage of the category
    for category in categories:
        for item in range(len(lines)):
            # print(int(line[2:4]))
            # print(spend_percentages[category.category])
            if spend_percentages[category.category] >= int(lines[item][1:4]):
                lines[item] += 'o  '
            else:
                lines[item] += '   '

    # updates bar_chart with section
    for line in lines:
        bar_chart += line
    
    # adds hyphen break section
    bar_chart += "\n    -" + "---" * len(categories) + "\n"

    # record the length of the category names
    category_lengths = []
    for category in categories:
        category_lengths.append(len(category.category))

    # while count is less or equal to the longest category length
    # append the correct letter to the correct line
    # else append blank spaces to keep others category names aligned
    category_names = ""
    count = 0
    while count < max(category_lengths):
        for category in categories:
            if count < len(category.category):
                if category == categories[0]:
                    category_names += f"{str(category.category[count]).rjust(6)}"
                elif category == categories[-1]:
                    category_names += f"{str(category.category[count]).rjust(3)}  "
                else:
                    category_names += f"{str(category.category[count]).rjust(3)}"
            else:
                if category == categories[0]:
                    category_names += "      "
                else:
                    category_names += "   "
        category_names += "\n"
        count += 1 

    # add the category names to the bar_chart
    bar_chart += category_names[:-1]
    return bar_chart