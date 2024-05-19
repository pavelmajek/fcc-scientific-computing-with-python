# Budget App solution for freeCodeCamp Scientific Computing with Python certification

from math import floor

class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def __str__(self):
        title_line = f"{self.name:*^30}\n"

        item_list = ""
        for item in self.ledger:
            item_list += f'{item["description"][:23]:<23}{item["amount"]:>7.2f}\n'

        total = f'Total: {sum(map(lambda x: x["amount"], self.ledger)):.2f}'

        output = title_line + item_list + total
        return output

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        else:
            return False

    def get_balance(self):
        return sum(map(lambda item: item["amount"], self.ledger))

    def transfer(self, amount, destination_category):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {destination_category.name}")
            destination_category.deposit(amount, f"Transfer from {self.name}")
            return True
        else:
            return False

    def check_funds(self, amount):
        if amount > sum(map(lambda item: item["amount"], self.ledger)):
            return False
        else:
            return True

    # helper functions to solve create_spend_chart function
    def get_withdrawals(self):
        total = 0
        for item in self.ledger:
            if item["amount"] < 0:
                total += abs(item["amount"])
        return total

    def get_percentage(self, total_withdrawals):
        percentage = self.get_withdrawals()/total_withdrawals * 100
        return floor((percentage/10)*10)


def create_spend_chart(categories):
    total_withdrawals = 0
    perc_list = []
    for category in categories:
        total_withdrawals += category.get_withdrawals()
    for category in categories:
        perc_list.append(category.get_percentage(total_withdrawals))

    title = "Percentage spent by category\n"

    chart = ""
    for i in range(11):
        percpart = ""
        for value in perc_list:
            if value >= (100 - 10 * i):
                part = "o  "
            else:
                part = "   "
            percpart += part
        line = f"{100 - 10 * i:>3}| " + percpart + "\n"
        chart += line

    dash_line = "    -" + "---" * len(perc_list) + "\n"

    loop_length = max(map(lambda x: len(x.name), categories))
    chart_description = ""
    for i in range(loop_length):
        des_line = ""
        for j in categories:
            if len(j.name) > i:
                despart = j.name[i] + "  "
            else:
                despart = "   "
            des_line += despart
        line = "     " + des_line + "\n"
        chart_description += line
    chart_description = chart_description[:-1]

    output = title + chart + dash_line + chart_description
    return output
