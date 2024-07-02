from main import get_input


def get_input_items(list):
    items = []
    for item in list:
        for i in item:
            items.append(i)
    return items


def get_current_floor(steps_list):
    current_floor = 0
    for idx, step in enumerate(steps_list):
        if step == "(":
            current_floor += 1
        if step == ")":
            current_floor -= 1
        if current_floor == -1:
            return idx + 1


def get_solution_part1():
    year = "2015"
    file = "input_day_1.txt"
    path = f"./{year}/{file}"
    input_lines = get_input(path)
    items = get_input_items(input_lines)
    up_items = [item for item in items if item == "("]
    down_items = [item for item in items if item == ")"]
    current_item = len(up_items) - len(down_items)
    print(f"Part one solution: {current_item}")


if __name__ == "__main__":
    get_solution_part1()
    year = "2015"
    file = "input_day_1.txt"
    path = f"./{year}/{file}"
    input_lines = get_input(path)
    items = get_input_items(input_lines)
    pos = get_current_floor(items)
    print(f"Part two solution: {pos}")
