def create_list():
    return ['PlayStation', 'Xbox', 'Steam', 'iOS', 'Google Play']


def get_info(my_list):
    first_element = my_list[0]
    second_last_element = my_list[-2]
    number_of_elements = len(my_list)

    return (first_element, second_last_element, number_of_elements)


def get_partial(my_list):
    partial = my_list[1:4]
    return partial


def get_last_three(my_list):
    last_three = my_list[-3:]
    reversed_last_three = last_three[::-1]
    return reversed_last_three


def double_list(my_list):
    doubled = my_list + my_list
    return doubled


def amend(my_list):
    new_list = my_list[:]
    new_list[1] = "None"
    new_list.append("Bye")

    return new_list


if __name__ == "__main__":
    test_list = create_list()

    print(test_list)
    print(get_info(test_list))
    print(get_last_three(test_list))
    print(double_list(test_list))
    print(amend(test_list))