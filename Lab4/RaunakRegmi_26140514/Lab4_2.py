def get_data():
    house_counts = []

    for i in range(8):
        if i == 7:
            user_input = f"Provide the number of houses with 6+ occupancy: "
        else:
            user_input = f"Provide the number of houses with {i} occupancy: "

        count = int(input(user_input))
        house_counts.append(count)

    return house_counts


def cal_percentage(h0, h1, h2, h3, h4, h5, h6, h7):
    house_data = [h0, h1, h2, h3, h4, h5, h6, h7]
    total_houses = sum(house_data)

    percentages = []
    for houses in house_data:
        if total_houses > 0:
            percentage = (houses / total_houses) * 100
            percentages.append(percentage)
        else:
            percentages.append(0.0)

    return percentages


def display_result(h0, h1, h2, h3, h4, h5, h6, h7, p0, p1, p2, p3, p4, p5, p6, p7):
    print()

    print("Occupants:    ", end="")
    occupancy_labels = ["0", "1", "2", "3", "4", "5", "6", "7"]
    for label in occupancy_labels:
        print(f"{label:>7}", end="")
    print()

    print("No. houses:   ", end="")
    house_counts = [h0, h1, h2, h3, h4, h5, h6, h7]
    for count in house_counts:
        print(f"{count:>7}", end="")
    print()

    print("Percentage:   ", end="")
    percentages = [p0, p1, p2, p3, p4, p5, p6, p7]
    for percent in percentages:
        print(f"{percent:>6.1f}%", end="")
    print()

 or 2
if __name__ == "__main__":
    data = get_data()
    h0, h1, h2, h3, h4, h5, h6, h7 = data

    p = cal_percentage(h0, h1, h2, h3, h4, h5, h6, h7)
    p0, p1, p2, p3, p4, p5, p6, p7 = p

    display_result(h0, h1, h2, h3, h4, h5, h6, h7,
                   p0, p1, p2, p3, p4, p5, p6, p7)