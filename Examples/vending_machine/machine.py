"""
Contains vending machine model.
"""
from .import money


# Coin types used by machine
COIN_CLASSES = [
    money.FiveRupee,
    money.TenRupee,
    money.TwentyRupee,
    money.HundredRupee
]


class VendingMachine:
    """
    A virtual vending machine.
    """
    def __init__(self):
        self.inserted_coins = []

    def insert_coin(self, coin):
        """
        Accepts a Coin instance and inserts it into the vending machine.
        """
        if not isinstance(coin, money.Rupee):
            raise ValueError()

        self.inserted_coins.append(coin)

    def get_balance(self):
        """
        Returns the balance remaining.
        """
        return sum(self.inserted_coins)

    def get_change(self):
        """
        Returns change representing positive balance. The largest
        denominations are always used first.
        """
        coins = []
        balance = self.get_balance()
        balance -= balance * 100 % 5

        while balance > 0:
            for coin_class in reversed(COIN_CLASSES):
                if balance - coin_class.value >= 0:
                    coin = coin_class()  # Create a coin instance
                    coins.append(coin)
                    balance -= coin_class.value
                    break

        return coins