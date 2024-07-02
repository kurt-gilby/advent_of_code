def get_input(path):
    input_lines = []
    with open(path, "r") as file:
        input_lines = file.readlines()
    return input_lines


if __name__ == "__main__":
    year = "2015"
    day = "day_1"
    question = "1"
    file = "input.txt"
    path = f"./{year}/{day}/{question}/{file}"
    input_lines = get_input(path)
    print(input_lines)
