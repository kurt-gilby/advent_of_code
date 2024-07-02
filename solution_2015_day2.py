from main import get_input
from solution_2015_day1 import get_input_items


def split_input_items_to_demensions(items_list, split_char):
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


def get_smallest_of_three(x, y, z):
    if x <= y and x <= z:
        return x
    if y <= x and y <= z:
        return y
    if z <= x and z <= y:
        return z


def get_two_smallest_of_three(x, y, z):
    smallest = get_smallest_of_three(x, y, z)
    next_smallest = 99999999999999999999999999
    if smallest == x:
        next_smallest = get_smallest_of_three(next_smallest, y, z)
        return smallest, next_smallest
    if smallest == y:
        next_smallest = get_smallest_of_three(x, next_smallest, z)
        return smallest, next_smallest
    if smallest == z:
        next_smallest = get_smallest_of_three(x, y, next_smallest)
        return smallest, next_smallest


def get_wrapping_needed(lengths, widths, heights):
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


def get_total_wrapping_needed(wrapping_needed_list):
    tot = 0
    for warp in wrapping_needed_list:
        tot += warp
    return tot


def sloved_get_total_wrapping_needed(path):
    input_lines = get_input(path)
    lengths, widths, heights = split_input_items_to_demensions(input_lines, "x")
    wrapping_needed = get_wrapping_needed(lengths, widths, heights)
    total = get_total_wrapping_needed(wrapping_needed)
    print(f"Total wrapping needed: {total}")


def get_ribbon_needed(lengths, widths, heights):
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


def get_total_ribbon_needed(ribbon_needed):
    tot = 0
    for ribbon in ribbon_needed:
        tot += ribbon
    return tot


def sloved_get_total_ribbon_needed(path):
    input_lines = get_input(path)
    lengths, widths, heights = split_input_items_to_demensions(input_lines, "x")
    ribbon_needed = get_ribbon_needed(lengths, widths, heights)
    total = get_total_ribbon_needed(ribbon_needed)
    print(f"Total ribbon needed: {total}")


if __name__ == "__main__":
    year = "2015"
    file = "input_day_2.txt"
    path = f"./{year}/{file}"
    sloved_get_total_wrapping_needed(path)
    sloved_get_total_ribbon_needed(path)
