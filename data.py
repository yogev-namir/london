from typing import Dict

import pandas

features = ["hum", "t1", "cnt", "season", "is_holiday"]
"""
xl = {'names': ['omer', 'yogev'], 'age': '25', 'city': 'motzkin'}
feature = ["names"]
data = {}
for key in xl.keys():
    if key in feature:
        data[key] = xl[key]
print(data)
"""


def load_data(path, features):
    """
        gets a file's path and returns a dict- it's keys are the features givens
        and their's value are given in the file
        :param path: the file's path
        :param features: the relevant features to save
        :return: a dict with the suitable keys and values
    """
    data = {}
    df = pandas.read_csv(path)
    data_raw = df.to_dict(orient="list")
    for key in data_raw.keys():
        if key in features:
            data[key] = data_raw[key]

    return data


feature = "season"
values = {1}
dict = {'season': [0,1,1,0,1]}


data1 = {feature: []}
data2 = {feature: []}
for key in dict.keys():
    if key == feature:
        for value in dict[key]:
            if value in values:
                data1[key].append(value)
            else:
                data2[key].append(value)
print (data1, data2)

"""
def filter_by_fiture(data,feature, values):

    """"""
    :param data: full dictionary from the exel file
    :param feature: the desire key, string
    :param values: a set of integers. A range of achievable values
    :return: two dictionaries, one with the required values and the other with the complementary values
    """"""
    data1 = {feature: []}
    data2 = {feature: []}
    for key in dict.keys():
        if key == feature:
            for value in dict[key]:
                if value in values:
                    data1[key].append(value)
                else:
                    data2[key].append(value)
    
    return (data1, data2)
"""





