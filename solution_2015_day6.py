from helper import get_input


def parse_instructions(insturction: str, init_key: int) -> tuple[dict, int]:
    """
    Reads the instruction and the key of the last instruction

    e.g. of instruction: 'turn on 0,0 through 9,9' or 'toggle 0,0 through 9,0' or 'turn off 4,4 through 5,5'

    Convert to dict of the form {key: [start_coordinate, end_coordinate , state ]}

    Returns dict and key
    """
    split_instruct = insturction.split("through")

    state = None
    if split_instruct[0].startswith("turn off"):
        state = 0
        split_instruct[0] = split_instruct[0].replace("turn off", "")
    if split_instruct[0].startswith("turn on"):
        state = 1
        split_instruct[0] = split_instruct[0].replace("turn on", "")
    if split_instruct[0].startswith("toggle"):
        state = -1
        split_instruct[0] = split_instruct[0].replace("toggle", "")

    split_instruct = [i.strip() for i in split_instruct]
    split_instruct = [i.split(",") for i in split_instruct]
    for idx, l in enumerate(split_instruct):
        for idx2, i in enumerate(l):
            split_instruct[idx][idx2] = int(split_instruct[idx][idx2])

    split_instruct.append(state)
    instruct_dict = {}
    instruct_dict[init_key] = split_instruct
    return instruct_dict


def get_instructions_dict() -> dict:
    year = "2015"
    file = "input_day_6.txt"
    path = f"./{year}/{file}"
    input_lines = get_input(path)
    key = 0
    instructions_dict = {}
    for line in input_lines:
        instruct_dict = parse_instructions(line, key)
        instructions_dict[key] = instruct_dict[key]
        key += 1
    return instructions_dict


def initialize_grid(rows: int, cols: int, init_state: str):
    columns = [init_state * cols]
    grid = columns * rows
    return grid


def initialize_grid2(rows: int, cols: int, init_state: str):
    grid = []
    for r in range(rows):
        grid.append(init_state * cols)
    print(grid)
    return grid


def get_coords_range(start: tuple, end: tuple) -> tuple[int, int]:
    start_row = int(start[0])
    end_row = int(end[0])
    start_col = int(start[1])
    end_col = int(end[1])
    row_range = range(start_row, end_row + 1)
    col_range = range(start_col, end_col + 1)
    return row_range, col_range


def do_action(row_range: range, col_range: range, grid: list, action: str) -> list[str]:
    if action != None:
        for r in row_range:
            col_val_list = list(grid[r])
            for c in col_range:
                col_val_list[c] = action
            grid[r] = "".join(col_val_list)
        return grid
    else:
        for r in row_range:
            col_val_list = list(grid[r])
            for c in col_range:
                state = col_val_list[c]
                if state == "o":
                    col_val_list[c] = "."
                if state == ".":
                    col_val_list[c] = "o"
            grid[r] = "".join(col_val_list)
        return grid


def turn_on_lights(start: tuple, end: tuple, grid: list) -> list[str]:
    row_range, col_range = get_coords_range(start, end)
    grid = do_action(row_range, col_range, grid, "o")
    return grid


def turn_off_lights(start: tuple, end: tuple, grid: list) -> list[str]:
    row_range, col_range = get_coords_range(start, end)
    grid = do_action(row_range, col_range, grid, ".")
    return grid


def toggle_lights(start: tuple, end: tuple, grid: list) -> list[str]:
    row_range, col_range = get_coords_range(start, end)
    grid = do_action(row_range, col_range, grid, None)
    return grid


def solved_part_one():
    instructions = get_instructions_dict()
    grid = initialize_grid(1000, 1000, ".")
    udpated_grid = None
    for key, inst in instructions.items():
        if udpated_grid == None:
            input_grid = grid
        else:
            input_grid = udpated_grid
        action = inst[2]
        start_coods = inst[0]
        end_coods = inst[1]
        if action == 1:
            udpated_grid = turn_on_lights(start_coods, end_coods, input_grid)
            continue
        if action == 0:
            udpated_grid = turn_off_lights(start_coods, end_coods, input_grid)
            continue
        if action == -1:
            udpated_grid = toggle_lights(start_coods, end_coods, input_grid)
            continue

    count = 0
    for row in udpated_grid:
        for col in row:
            if col == "o":
                count += 1
    print(f"Part One: {count} : Lights are on!")


def increase_brightness(start: tuple, end: tuple, grid: list, value: int) -> list[str]:
    row_range, col_range = get_coords_range(start, end)
    for r in row_range:
        for c in col_range:
            grid[r][c] = grid[r][c] + value
    return grid


def decrease_brightness(start: tuple, end: tuple, grid: list, value: int) -> list[str]:
    row_range, col_range = get_coords_range(start, end)
    for r in row_range:
        for c in col_range:
            if grid[r][c] > 0:
                grid[r][c] = grid[r][c] - value
    return grid


def initialize_num_grid(rows: int, cols: int, init_state: int):
    grid = []
    for r in range(rows):
        grid.append([0] * cols)
    return grid


def solved_part_two():
    instructions = get_instructions_dict()
    grid = initialize_num_grid(1000, 1000, 0)
    udpated_grid = None
    for key, inst in instructions.items():
        if udpated_grid == None:
            input_grid = grid
        else:
            input_grid = udpated_grid
        action = inst[2]
        start_coods = inst[0]
        end_coods = inst[1]
        if action == 1:
            udpated_grid = increase_brightness(start_coods, end_coods, input_grid, 1)
            continue
        if action == -1:
            udpated_grid = increase_brightness(start_coods, end_coods, input_grid, 2)
            continue
        if action == 0:
            udpated_grid = decrease_brightness(start_coods, end_coods, input_grid, 1)
            continue

    total = 0
    for row in udpated_grid:
        for col in row:
            total = total + col
    print(f"Part Two: {total} : Brightness Level!")


if __name__ == "__main__":
    solved_part_one()
    solved_part_two()
