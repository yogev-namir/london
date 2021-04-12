import pandas
import sys
import Statistics
import math

values=[1,1,1,4,1,3,1,1]
def sum(values: list):
    sum = 0
    for value in values:
        sum += value
    return sum

def mean(values: list):
    return sum(values) / len(values)

def median(values: list):
    length = len(values)
    sorted_values = sorted(values)
    if length % 2 ==0 :
        median = (sorted_values[int(length / 2)] + sorted_values[int(length / 2) - 1])
        median /= 2

    else:
        median = math.ceil(len(sorted_values) / 2)
    return int(median)

print(sum(values))
print(mean(values))
print(median(values))



