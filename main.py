import statistics
import data as Data
import sys


def main(argv):
    # gets the path and the features from input

    str_input = argv[2]
    features: list = str_input.split(", ")
    data = Data.load_data(argv[1], features)
    statistic_functions = [statistics.sum, statistics.mean, statistics.median]
    List = features[:3]
    SUMMER = 1
    WINTER = 3
    HOLIDAY = 1
    ###########################################################################

    data_summer, holder = Data.filter_by_feature(data, features[3], SUMMER)
    data_holiday, holder = Data.filter_by_feature(data, features[4], HOLIDAY)
    print(f"Question 1:")
    print(f"Summer:")
    Data.print_details(data_summer, List, statistic_functions)
    print(f"Holiday:")
    Data.print_details(data_holiday, List, statistic_functions)
    print(f"All:")
    Data.print_details(data, List, statistic_functions)
    ###########################################################################
    THRESHOLD = 13
    descriptions = ["Winter holiday recordes:", "Winter weekday records:"]

    data_winter, holder = Data.filter_by_feature(data, features[3], WINTER)
    data_holiday, data_weekday = Data.filter_by_feature(data_winter, features[4], HOLIDAY)
    list1 = [data_holiday, data_weekday]
    statistic_functions_2 = [statistics.mean, statistics.median]
    signes_list = ["<=", ">"]
    print(f"Question 2:")
    for i in range(2):
        print(f"If {features[1]}{signes_list[i]}13.0, then:")
        for j in range(2):
            Data.population_statistics(descriptions[j],
                                       list1[j], 't1', 'cnt', THRESHOLD, i, statistic_functions_2)


if __name__ == "__main__":
    main(sys.argv)
