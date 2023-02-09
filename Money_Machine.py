class MoneyMachine:
    coin_values = {"pennies": 0.01, "nickel": 0.5, "dime": 0.10, "quarter": 0.25}
    currency = "$"

    def __init__(self):
        self.profit = 0
        self.money_received = 0

    def report(self):
        """
        Prints the current profit
        e.g.
        Money: $0
        """
        print(f"current profit is {self.currency}{self.profit}")

    def process_coins(self):
        """Returns the total calculated from coins inserted."""
        print("Please insert Coins")
        self.money_received = int(input("How many quarters? ")) * self.coin_values['quarter']
        self.money_received += int(input("How many dime? ")) * self.coin_values['dime']
        self.money_received += int(input("How many nickel? ")) * self.coin_values['nickel']
        self.money_received += int(input("How many pennies? ")) * self.coin_values['pennies']
        return self.money_received

    def make_payment(self, cost):
        """Returns True when payment is accepted, or False if insufficient."""
        self.process_coins()
        if self.money_received >= cost:
            change = round(self.money_received-cost, 2)
            print(f"Here is your change {self.currency}{change}")
            self.profit += cost
            self.money_received = 0
            return True
        else:
            print(f" Sorry Thats not a enough maney. Money Refunded")
            self.money_received = 0
            return False
