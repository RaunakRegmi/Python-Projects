import math

def next_point(step):
    x = int(input(f"Input x{step} coordinates: "))
    y = int(input(f"Input y{step} coordinates: "))
    return (x, y)

def calculate_distance(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return distance


def main():
    print("----- Robot Program -----")

    current_point = (0, 0)
    step = 1
    total_distance = 0.0
    while True:
        next_point = next_point(step)

        if next_point == (999, 999):
            break

        distance = calculate_distance(current_point, next_point)
        print(f"Step: {distance:.2f}")

        total_distance = total_distance + distance
        current_point = next_point
        step = step + 1

    print("--------------------------")
    print(f"Total distance travelled by the robot: {total_distance}")


if __name__ == "__main__":
    main()