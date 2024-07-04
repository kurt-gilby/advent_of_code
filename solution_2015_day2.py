from helper import (
    get_input,
    get_smallest_of_three,
    get_total_of_list_of_floats,
    get_two_smallest_of_three,
)


def split_input_items_to_demensions(
    items_list: list[str], split_char: str
) -> tuple[list[float], list[float], list[float]]:
    """
    Takes an input like "2x4x5" and "3x15x70"
    retruns the [2,3] , [4,15] and [5,70] as the lists with Lengths, Width and heights
    """
    lengths = []
    widths = []
    heights = []
    for item in items_list:
        split_text = item.split(split_char)
        for idx, d in enumerate(split_text):
            if idx == 0:
                lengths.append(float(d))
            if idx == 1:
                widths.append(float(d))
            if idx == 2:
                heights.append(float(d))
    return lengths, widths, heights


def get_wrapping_needed(
    lengths: list[float], widths: list[float], heights: list[float]
) -> list[float]:
    """
    Takes the list of lengths, widths and heigths of cuboid objects.
    Returns the list of warpping needed for each object where wrapping needed = 2 * (lw + wh + hl) + slack where slack is the area of the smallest side
    """
    wrapping_needed = []
    for idx, d in enumerate(lengths):
        l = d
        w = widths[idx]
        h = heights[idx]

        lw = l * w
        wh = w * h
        hl = h * l
        slack = get_smallest_of_three(lw, wh, hl)

        wn = 2 * (lw + wh + hl)
        wn += slack
        wrapping_needed.append(wn)
    return wrapping_needed


def get_total_wrapping_needed(wrapping_needed_list: list[float]) -> float:
    """
    Takes the wrapping needed list
    Returns the total of the list.
    """
    tot = get_total_of_list_of_floats(wrapping_needed_list)
    return tot


def sloved_get_total_wrapping_needed(path: str) -> float:
    """
    Takes the input as a file path with the list of dimensions of all the gifts
    Returns the total wrapping paper needed is square feet.
    """
    input_lines = get_input(path)
    lengths, widths, heights = split_input_items_to_demensions(input_lines, "x")
    wrapping_needed = get_wrapping_needed(lengths, widths, heights)
    total = get_total_wrapping_needed(wrapping_needed)
    print(f"Total wrapping needed: {total}")
    return total


def get_ribbon_needed(
    lengths: list[float], widths: list[float], heights: list[float]
) -> list[float]:
    """
    Takes the list of lengths, widths and heigths of cuboid objects.
    Returns the list of ribbon needed for each object where ribbon needed = l * w * h  + slack where slack is the perimeter of the smallest side
    """
    ribbon_needed = []
    for idx, d in enumerate(lengths):
        l = d
        w = widths[idx]
        h = heights[idx]

        bow = l * w * h

        x, y = get_two_smallest_of_three(l, w, h)
        smallest_perimeter = 2 * (x + y)
        ribbon_needed.append(bow + smallest_perimeter)
    return ribbon_needed


def get_total_ribbon_needed(ribbon_needed: list[float]) -> float:
    """
    Takes the ribbon needed list
    Returns the total of the list.
    """
    tot = get_total_of_list_of_floats(ribbon_needed)
    return tot


def sloved_get_total_ribbon_needed(path: str) -> float:
    """
    Takes the input as a file path with the list of dimensions of all the gifts
    Returns the total ribbon needed in cubic feet.
    """
    input_lines = get_input(path)
    lengths, widths, heights = split_input_items_to_demensions(input_lines, "x")
    ribbon_needed = get_ribbon_needed(lengths, widths, heights)
    total = get_total_ribbon_needed(ribbon_needed)
    print(f"Total ribbon needed: {total}")
    return total


if __name__ == "__main__":
    year = "2015"
    file = "input_day_2.txt"
    path = f"./{year}/{file}"
    sloved_get_total_wrapping_needed(path)
    sloved_get_total_ribbon_needed(path)
