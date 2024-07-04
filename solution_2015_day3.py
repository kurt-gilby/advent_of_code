from main import get_input
from solution_2015_day1 import get_input_items


def update_grid_address(current_pos, direction):
    if direction == "^":
        current_pos[0] += 1
        return current_pos
    if direction == ">":
        current_pos[1] += 1
        return current_pos
    if direction == "<":
        current_pos[1] -= 1
        return current_pos
    if direction == "v":
        current_pos[0] -= 1
        return current_pos


def get_grid_address_visited(directions):
    curr_pos = [0, 0]
    key = tuple(curr_pos)
    gird_addresses = {}
    gird_addresses[key] = 1
    for dir in directions:
        curr_pos = update_grid_address(curr_pos, dir)
        key = tuple(curr_pos)
        if key not in gird_addresses:
            gird_addresses[key] = 1
            continue
        gird_addresses[key] += 1
    return gird_addresses


def solved_get_houses_with_at_least_one_persent():
    year = "2015"
    file = "input_day_3.txt"
    path = f"./{year}/{file}"
    input_lines = get_input(path)
    input_items = get_input_items(input_lines)
    gird_addresses = get_grid_address_visited(input_items)
    print(f"Number of Houses with aleast one present: {len(gird_addresses)}")


def get_santa_and_robo_instructions(input_items):
    santa_instructions = []
    robo_instructions = []
    for idx, item in enumerate(input_items):
        if idx % 2 == 0:
            santa_instructions.append(item)
        else:
            robo_instructions.append(item)
    return santa_instructions, robo_instructions


def solved_get_houses_with_at_least_one_persent_visted_by_santa_or_robo():
    year = "2015"
    file = "input_day_3.txt"
    path = f"./{year}/{file}"
    input_lines = get_input(path)
    input_items = get_input_items(input_lines)
    santa_instructions, robo_instructions = get_santa_and_robo_instructions(input_items)
    santa_gird_addresses = get_grid_address_visited(santa_instructions)
    robo_gird_addresses = get_grid_address_visited(robo_instructions)
    houses_visited_list = list(santa_gird_addresses.keys())
    houses_visited_list += list(robo_gird_addresses.keys())
    distinct_houses_visited = set(houses_visited_list)
    print(
        f"Number of Houses with aleast one present visited by santa or robo: {len(distinct_houses_visited)}"
    )


if __name__ == "__main__":
    solved_get_houses_with_at_least_one_persent()
    solved_get_houses_with_at_least_one_persent_visted_by_santa_or_robo()
