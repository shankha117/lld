"""
Contains all models pertaining to money, coins, etc.
"""
from decimal import Decimal


class RupeeAmount(Decimal):
    """
    Represents a dollar amount.
    Extends the decimal.Decimal class.
    """

    def __repr__(self):
        return f"Rs('{self}')"


class Rupee:
    """Base class representing coins."""
    value = RupeeAmount('0')

    def __radd__(self, other):
        return self.value + other

    def __eq__(self, other):
        return self.value == other.value


# class OneRupee(Rupee):
#     """1 rs coin."""
#     value = RupeeAmount('1')


# class TwoRupee(Rupee):
#     """20 rs coin."""
#     value = RupeeAmount('2')


class FiveRupee(Rupee):
    """5 rs coin."""
    value = RupeeAmount('5')


class TenRupee(Rupee):
    """10 rs coin."""
    value = RupeeAmount('10')


class TwentyRupee(Rupee):
    """20 rs coin."""
    value = RupeeAmount('20')


class HundredRupee(Rupee):
    """100 rs coin."""
    value = RupeeAmount('100')
