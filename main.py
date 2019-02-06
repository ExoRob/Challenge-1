import pandas


def user_input():
    string = raw_input("Which month would you like?")

    return string


def load_csv(month):
    filename = "dispensed-items-by-gp-and-pharmacy-{}-2018.csv".format(month)

    df = pandas.read_csv(filename)

    return df


data = load_csv(user_input())

