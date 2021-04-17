import statistics
import data as Data
import sys


def main(argv):

    str_input = argv[2]
    features: list = str_input.split(", ")
    data = Data.load_data(argv[1], features)
    statistic_functions = [statistics.sum, statistics.mean, statistics.median]
    continuous_features = features[:3]
    SUMMER = 1
    WINTER = 3
    HOLIDAY = 1
    """
    ##############################~~QUESTION 1~~###################################
    holder is just a spare dictionary to store the second returned dictionary, it's not being used during the program
    """
    data_summer, holder = Data.filter_by_feature(data, features[3], SUMMER)
    data_holiday, holder = Data.filter_by_feature(data, features[4], HOLIDAY)
    print(f"Question 1:")
    print(f"Summer:")
    Data.print_details(data_summer, continuous_features, statistic_functions)
    print(f"Holiday:")
    Data.print_details(data_holiday, continuous_features, statistic_functions)
    print(f"All:")
    Data.print_details(data, continuous_features, statistic_functions)
    """
    ##############################~~QUESTION 2~~###############################
    """
    THRESHOLD = 13
    SECTIONS = 2

    descriptions = ["Winter holiday records:", "Winter weekday records:"]
    data_winter, holder = Data.filter_by_feature(data, features[3], WINTER)
    new_data_holiday, data_weekday = Data.filter_by_feature(data_winter, features[4], HOLIDAY)
    list_of_dictionaries = [new_data_holiday, data_weekday]
    new_statistic_functions = [statistics.mean, statistics.median]
    signs_list = ["<=", ">"]

    print(f"\nQuestion 2:")
    for i in range(SECTIONS):
        print(f"If {features[1]}{signs_list[i]}13.0, then:")
        for j in range(SECTIONS):
            Data.population_statistics(descriptions[j],
                                       list_of_dictionaries[j], features[1], features[2],
                                       THRESHOLD, i, new_statistic_functions)


if __name__ == "__main__":
    main(sys.argv)
