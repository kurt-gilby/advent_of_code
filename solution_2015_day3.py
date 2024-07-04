from helper import get_input, get_input_items


def update_grid_address(
    current_pos: list[int, int], direction: str["^" | ">" | "<" | "v"]
) -> list[int, int]:
    """
    Takes a starting position of the format "[x,y]" and a direction to move
    Returns the new position "[w,z]" dependant on the direction inputted.
    """
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


def get_grid_address_visited(
    directions: list[str["^" | ">" | "<" | "v"]],
) -> dict[tuple:int]:
    """
    Takes in a list of characters as directions where "^": North | ">": East | "<": West | "v": South
    Returns a dictionary of addresses visited on the grid with starting positiion (0,0) and number of times a position is visited.
    e.g. {(0,0): 1, (1,0): 1, (1,1): 1, (0,1): 1} will be the output for "^>v"
    """
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


def solved_get_houses_with_at_least_one_persent() -> dict[tuple:int]:
    """
    Takes the input files for the directions of the route.
    Gets all the houses visited on the route
    Returns the total number of houses visited
    """
    year = "2015"
    file = "input_day_3.txt"
    path = f"./{year}/{file}"
    input_lines = get_input(path)
    input_items = get_input_items(input_lines)
    gird_addresses = get_grid_address_visited(input_items)
    print(f"Number of Houses with aleast one present: {len(gird_addresses)}")
    return gird_addresses


def get_santa_and_robo_instructions(
    input_items: list[str],
) -> tuple[list[str], list[str]]:
    """
    Takes in the list of string with the instructions.
    puts all the odd insturctions in a new list of strings for the robo.
    puts all the even instructions in a new list of string for santa.
    returns but santas instructions and robos.
    """
    santa_instructions = []
    robo_instructions = []
    for idx, item in enumerate(input_items):
        if idx % 2 == 0:
            santa_instructions.append(item)
        else:
            robo_instructions.append(item)
    return santa_instructions, robo_instructions


def solved_get_houses_with_at_least_one_persent_visted_by_santa_or_robo() -> (
    set[tuple[int]]
):
    """
    Takes the input files for the directions of the route.
    gets the instructions for santa and robo sperately
    Gets all the houses visited on the santa route
    Gets all the houses visited on the robo route
    gets all the houses visited on both routes and removes any duplicates
    Returns the total number of houses visited
    """
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
    return distinct_houses_visited


if __name__ == "__main__":
    solved_get_houses_with_at_least_one_persent()
    solved_get_houses_with_at_least_one_persent_visted_by_santa_or_robo()
