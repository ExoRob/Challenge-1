import pandas


def user_input():
    string = raw_input("Which month would you like?")

    return string


def load_csv(month):
    filename = "dispensed-items-by-gp-and-pharmacy-{}-2018.csv".format(month)

    df = pandas.read_csv(filename)

    return df


# data = load_csv(user_input())
data = load_csv("october")

practices = set(data["Practice"])

for practice_id in list(practices):
    practice_data = data[data["Practice"] == practice_id]

    sorted_data = practice_data.sort_values("Number of Items", ascending=False)

    cut_data = sorted_data[:5]

    print cut_data
