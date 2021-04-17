import math


def sum(values: list):
    """
    Adding together the values inside the given list
    :param values: a list of numbers
    :return: the sum of the list's values
    """
    sum_value = 0
    for value in values:
        sum_value += value
    return sum_value


def mean(values: list):
    """
    The sum of the list's values divided by the number of values in the list
    :param values: a list of numbers
    :return: the mean of the list
    """
    return (sum(values) / len(values)) if len(values) != 0 else 0


def median(values: list):
    """
    The median_value is the middle value when a data set is ordered from least to greatest,
    varies if the length of the list is odd or even
    :param values: a list of numbers
    :return: the median_value of the list
    """
    length = len(values)
    sorted_values = sorted(values)

    if length == 0:
        return 0
    if length % 2 == 0:
        median_value = sorted_values[int(length / 2)] + sorted_values[int(length / 2) - 1]
        median_value /= 2
    else:
        median_value = float(sorted_values[math.floor(len(sorted_values) / 2)])
    return median_value





