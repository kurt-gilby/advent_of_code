from helper import generate_md5_hash, get_input


def get_hash_with_five_zero(item: str) -> tuple[str, str]:
    """
    Take a secret Item and adds numbers to it and checks if the hash generated for the value starts with "00000"
    Returns the 1st combination of the values secret + number that has hash generated with starts with  "00000"
    it this is not found with in the number bounds it returns the Item with "No hash found message"
    """
    item_length = len(item)
    start_number = 0
    end_number = 10 ** (item_length)
    for num in range(start_number, end_number + 1):
        item_hash = generate_md5_hash(item + str(num))
        if item_hash[:5] == "00000":
            return item, str(num), item_hash
    return item, "No Hash Found"


def get_hash_with_six_zero(item: str) -> tuple[str, str]:
    """
    Take a secret Item and adds numbers to it and checks if the hash generated for the value starts with "00000"
    Returns the 1st combination of the values secret + number that has hash generated with starts with  "00000"
    it this is not found with in the number bounds it returns the Item with "No hash found message"
    """
    item_length = len(item)
    start_number = 0
    end_number = 10 ** (item_length + 2)
    for num in range(start_number, end_number + 1):
        item_hash = generate_md5_hash(item + str(num))
        if item_hash[:6] == "000000":
            return item, str(num), item_hash
    return item, "No Num", "No Hash Found"


def solved_return_item_num_for_frist_hash_with_five_zeros():
    """
    Take a secret Item
    Returns the 1st combination of the values secret + number that has hash generated with starts with  "00000"
    """
    year = "2015"
    file = "input_day_4.txt"
    path = f"./{year}/{file}"
    input_lines = get_input(path)
    for item in input_lines:
        item, num, hash_val = get_hash_with_five_zero(item)
        print(f"Secret : {item} Number: {num} Hash : {hash_val}")


def solved_return_item_num_for_frist_hash_with_six_zeros():
    """
    Take a secret Item
    Returns the 1st combination of the values secret + number that has hash generated with starts with  "000000"
    """
    year = "2015"
    file = "input_day_4.txt"
    path = f"./{year}/{file}"
    input_lines = get_input(path)
    for item in input_lines:
        item, num, hash_val = get_hash_with_six_zero(item)
        print(f"Secret : {item} Number: {num} Hash : {hash_val}")


if __name__ == "__main__":
    solved_return_item_num_for_frist_hash_with_five_zeros()
    solved_return_item_num_for_frist_hash_with_six_zeros()
