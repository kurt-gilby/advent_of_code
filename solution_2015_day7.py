from helper import get_input


def create_instructions_table(
    input_list: list[str, str], instruction_dict: dict[str:str]
) -> dict[str:str]:
    key = input_list[1].strip()
    value = input_list[0].strip()
    instruction_dict[key] = value
    return instruction_dict


def get_not_value(int_val) -> int:
    x = bin(int_val)[2:].zfill(16)
    y = [str(1) if b == "0" else str(0) for b in x]
    y = "".join(y)
    y = "0b" + y
    y = int(y, 2)
    return y


def split_input_output(instruction: str) -> tuple[str, str]:
    inst = instruction.split("->")
    input = inst[0].strip()
    output = inst[1].strip()
    return input, output


# 2 records
def get_start_values(instructions: list[str], override: bool) -> dict[str:int]:
    init_dict = {}
    for instruction in instructions:
        input, output = split_input_output(instruction)
        if input.isdigit():
            if output == "b" and override:
                input = 16076
            init_dict[output] = int(input)
    return init_dict


# 96 records
def get_shift_instructions(
    init_dict: dict[str:int], instructions: list[str]
) -> dict[str:int]:
    shift_dict = {}
    for key in init_dict.keys():
        for instruction in instructions:
            input, output = split_input_output(instruction)
            if input.startswith(key + " ") and "SHIFT" in input:
                l, op, r = input.split()
                l, op, r = l.strip(), op.strip(), r.strip()
                if "LSHIFT" in input:
                    shift_dict[output] = int(init_dict[key]) << int(r)
                if "RSHIFT" in input:
                    shift_dict[output] = int(init_dict[key]) >> int(r)
    return shift_dict


# 112
def get_and_instructions(
    init_dict: dict[str:int], instructions: list[str]
) -> dict[str:int]:
    and_dict = {}
    for key in init_dict.keys():
        for instruction in instructions:
            input, output = split_input_output(instruction)
            if (
                input.startswith(key + " ") or input.startswith("1")
            ) and "AND" in input:
                l, op, r = input.split()
                l, op, r = l.strip(), op.strip(), r.strip()
                if r in init_dict:
                    if input.startswith("1"):
                        and_dict[output] = 1 & int(init_dict[r])
                        continue
                    and_dict[output] = int(init_dict[l]) & int(init_dict[r])

    return and_dict


# 80
def get_or_instructions(
    init_dict: dict[str:int], instructions: list[str]
) -> dict[str:int]:
    or_dict = {}
    for key in init_dict.keys():
        for instruction in instructions:
            input, output = split_input_output(instruction)
            if input.startswith(key + " ") and "OR" in input:
                l, op, r = input.split()
                l, op, r = l.strip(), op.strip(), r.strip()
                if r in init_dict:
                    or_dict[output] = int(init_dict[l]) | int(init_dict[r])

    return or_dict


def get_not_instructions(
    init_dict: dict[str:int], instructions: list[str]
) -> dict[str:int]:
    not_dict = {}
    for key in init_dict.keys():
        for instruction in instructions:
            input, output = split_input_output(instruction)
            if input.endswith(key) and "NOT" in input:
                op, r = input.split()
                op, r = op.strip(), r.strip()
                if r in init_dict:
                    not_dict[output] = get_not_value(int(init_dict[r]))

    return not_dict


def get_assignment_instructions(
    init_dict: dict[str:int], instructions: list[str]
) -> dict[str:int]:
    ass_dict = {}
    for key in init_dict.keys():
        for instruction in instructions:
            input, output = split_input_output(instruction)
            if input.startswith(key) and len(input.split()) == 1:
                l = input.split()[0]
                l = l.strip()
                if l in init_dict:
                    ass_dict[output] = int(init_dict[l])

    return ass_dict


def solved_part_one(override: bool):
    year = "2015"
    file = "input_day_7.txt"
    path = f"./{year}/{file}"
    input_lines = get_input(path)
    init_dict = get_start_values(input_lines, override)
    run = True
    while run:
        init_length = len(init_dict)

        shift_dict = get_shift_instructions(init_dict, input_lines)
        init_dict.update(shift_dict)

        and_dict = get_and_instructions(init_dict, input_lines)
        init_dict.update(and_dict)

        or_dict = get_or_instructions(init_dict, input_lines)
        init_dict.update(or_dict)

        not_dict = get_not_instructions(init_dict, input_lines)
        init_dict.update(not_dict)

        ass_dict = get_assignment_instructions(init_dict, input_lines)
        init_dict.update(ass_dict)

        fin_length = len(init_dict)
        if init_length == fin_length:
            run = False
    if not override:
        print(f'Signal on "a" : {init_dict["a"]}')
    else:
        print(f'Overridden Signal on "a" : {init_dict["a"]}')


if __name__ == "__main__":
    solved_part_one(False)
    solved_part_one(True)
