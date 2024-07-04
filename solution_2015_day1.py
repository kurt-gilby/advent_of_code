from helper import get_input, get_input_items


def get_current_floor(steps_list: list[str]) -> int:
    """
    Takes in a list of values which can be "(" or ")".
    Calculates the current floor, starting from "0" and incrementing by 1,
    for every "(" and decremnenting by 1 for every ")".
    returns the position of the value when current floor for the 1st time is -1.
    pos = index value of character in list + 1
    """
    current_floor = 0
    for idx, step in enumerate(steps_list):
        if step != "(" and step != ")":
            raise ValueError
        if step == "(":
            current_floor += 1
        if step == ")":
            current_floor -= 1
        if current_floor == -1:
            return idx + 1


def get_solution_part1():
    """
    Reads the input file and adds all the characters of "(" and
    all the characters of ")".
    takes the difference of the two to give the ending floor position
    """
    year = "2015"
    file = "input_day_1.txt"
    path = f"./{year}/{file}"
    input_lines = get_input(path)
    items = get_input_items(input_lines)
    up_items = [item for item in items if item == "("]
    down_items = [item for item in items if item == ")"]
    current_item = len(up_items) - len(down_items)
    print(f"Part one solution: {current_item}")


def get_solution_part2():
    """
    Reads the input file, converts to a list of characters.
    Takes in a list of values which can be "(" or ")".
    Calculates the current floor, starting from "0" and incrementing by 1,
    for every "(" and decremnenting by 1 for every ")".
    returns the position of the value when current floor for the 1st time is -1.
    pos = index value of character in list + 1

    """
    year = "2015"
    file = "input_day_1.txt"
    path = f"./{year}/{file}"
    input_lines = get_input(path)
    items = get_input_items(input_lines)
    pos = get_current_floor(items)
    print(f"Part two solution: {pos}")


if __name__ == "__main__":
    get_solution_part1()
    get_solution_part2()
