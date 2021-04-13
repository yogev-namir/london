import pandas
import sys
import math


def sum(values: list):
    sum = 0
    for value in values:
        sum += value
    return sum

def mean(values: list):
    return (sum(values) / len(values)) if len(values)!=0 else  0

def median(values: list):
    length = len(values)
    sorted_values = sorted(values)
    if length==0: return 0
    if length % 2 ==0 :
        median = (sorted_values[int(length / 2)] + sorted_values[int(length / 2) - 1])
        median /= 2

    else:
        median = float(sorted_values[math.floor(len(sorted_values) / 2)])
    return median





