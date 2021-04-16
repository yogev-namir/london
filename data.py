import pandas

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

def filter_by_feature(dict, feature, value):
    """
    :param data: full dictionary from the exel file
    :param feature: the desire key, string
    :param values: a set of integers. A range of achievable values
    :return: two dictionaries, one with the required values and the other with the complementary values
    """
    dict_1 = {}
    dict_2 = {}
    values_of_feature = [0 if a==value else 1 for a in dict.get(feature)]
    for key in dict:
        d1_key_value = []  # good
        d2_key_value= [] #bad
        for i in range(len(values_of_feature)):
            # checks for each item which dictionary is appropriate for him
            d2_key_value.append(dict.get(key)[i]) if values_of_feature[i] else d1_key_value.append(dict.get(key)[i])
        dict_1.update({key: d1_key_value})
        dict_2.update({key: d2_key_value})
    return (dict_1, dict_2)

def print_details(data, features, statistic_functions):
    for feature in features:
        outputs = []
        for func in statistic_functions:
            output = func(data.get(feature))  # sends the appropriate data
            outputs.append(str(output))
        print(f'{feature}: ' + ', '.join(outputs))


def filter_by_threshold(data, treatment, threshold, is_above):
    """"
    :param data: full dictionary from the exel file
    :param treatment: the desire key, string
    :param threshold: an int that signs a limit of values
    :param is_above: 1 or 0, check above the threshold or under

    :return: one dictionary, depends on the 'is_above' variable
    """
    dict_1 = {}
    dict_2 = {}
    values_of_feature = [0 if a > threshold else 1 for a in data.get(treatment)]
    for key in data:
        d1_key_value = []  # above threshold
        d2_key_value = []  # equal or under threshold
        for i in range(len(values_of_feature)):
            # checks for each item which dictionary is appropriate for him
            d2_key_value.append(data.get(key)[i]) if values_of_feature[i] else d1_key_value.append(data.get(key)[i])
        dict_1.update({key: d1_key_value})
        dict_2.update({key: d2_key_value})
    return dict_1 if is_above else dict_2


def population_statistics(feature_description, data, treatment, target,
                          threshold, is_above, statistic_functions):
    dict_above = filter_by_threshold(data, treatment, threshold, is_above)
    print(f"{feature_description}")
    outputs = []
    for func in statistic_functions:
        output = func(dict_above.get(target))  # sends the appropriate data
        outputs.append(str(output))
    print(f'{target}: ' + ', '.join(outputs))


