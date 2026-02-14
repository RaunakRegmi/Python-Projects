def get_data():
    house_counts = []

    for i in range(7):
        if i == 6:
            user_input = f"Provide the number of houses with 6+ occupancy: "
        else:
            user_input = f"Provide the number of houses with {i} occupancy: "

        count = int(input(user_input))
        house_counts.append(count)

    return house_counts


def cal_percentage(h0, h1, h2, h3, h4, h5, h6, h6plus):
    house_data = [h0, h1, h2, h3, h4, h5, h6, h6plus]
    total_houses = sum(house_data)

    percentages = []
    for houses in house_data:
        if total_houses > 0:
            percentage = (houses / total_houses) * 100
            percentages.append(percentage)
        else:
            percentages.append(0.0)

    return percentages


def display_result(h0, h1, h2, h3, h4, h5, h6, h6plus, p0, p1, p2, p3, p4, p5, p6, p6plus):
    print()

    print("Occupants:    ", end="")
    occupancy_labels = ["0", "1", "2", "3", "4", "5", "6", ">6"]
    for label in occupancy_labels:
        print(f"{label:>7}", end="")
    print()

    print("No. houses:   ", end="")
    house_counts = [h0, h1, h2, h3, h4, h5, h6, h6plus]
    for count in house_counts:
        print(f"{count:>7}", end="")
    print()

    print("Percentage:   ", end="")
    percentages = [p0, p1, p2, p3, p4, p5, p6, p6plus]
    for percent in percentages:
        print(f"{percent:>6.1f}%", end="")
    print()

def main():
    house_data = get_data()
    percentages = cal_percentage(house_data[0], house_data[1], house_data[2], house_data[3], house_data[4], house_data[5], house_data[6], house_data[6])

    display_result(house_data[0], house_data[1], house_data[2], house_data[3], house_data[4], house_data[5], house_data[6], house_data[6], percentages[0], percentages[1], percentages[2], percentages[3], percentages[4], percentages[5], percentages[6], percentages[7])

if __name__ == "__main__":
    main()