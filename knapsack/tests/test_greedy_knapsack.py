import unittest

import pytest

from knapsack import greedy_knapsack as kp


class TestClass(unittest.TestCase):
    """
    Test cases for knapsack
    """

    def test_sorted(self):
        """
        kp.calc_profit takes the required argument (profit, weight, max_weight)
        and returns whether the answer matches to the expected ones
        """
        profit = [10, 20, 30, 40, 50, 60]
        weight = [2, 4, 6, 8, 10, 12]
        max_weight = 100
        assert kp.calc_profit(profit, weight, max_weight) == 210

    def test_negative_max_weight(self):
        """Returns ``ValueError`` when ``max_weight`` is negative."""
        profit = [10, 20, 30]
        weight = [2, 4, 6]
        max_weight = -1
        with pytest.raises(
            ValueError, match="max_weight must greater than zero."
        ):
            kp.calc_profit(profit, weight, max_weight)

    def test_negative_profit_value(self):
        """Returns ``ValueError`` for any negative profit value."""
        profit = [10, -20, 30]
        weight = [2, 4, 6]
        max_weight = 15
        with pytest.raises(ValueError, match="Profit can not be negative."):
            kp.calc_profit(profit, weight, max_weight)

    def test_negative_weight_value(self):
        """Returns ``ValueError`` for any negative weight value."""
        profit = [10, 20, 30]
        weight = [2, -4, 6]
        max_weight = 15
        with pytest.raises(
            ValueError, match="Weight can not be negative."
        ):
            kp.calc_profit(profit, weight, max_weight)

    def test_null_max_weight(self):
        """Returns ``ValueError`` when ``max_weight`` is zero."""
        profit = [10, 20, 30]
        weight = [2, 4, 6]
        max_weight = 0
        with pytest.raises(
            ValueError, match="max_weight must greater than zero."
        ):
            kp.calc_profit(profit, weight, max_weight)

    def test_unequal_list_length(self):
        """Returns ``ValueError`` if ``profit`` and ``weight`` lengths differ."""
        profit = [10, 20, 30]
        weight = [2, 4]
        max_weight = 10
        with pytest.raises(
            ValueError, match="The length of profit and weight must be same."
        ):
            kp.calc_profit(profit, weight, max_weight)


if __name__ == "__main__":
    unittest.main()
