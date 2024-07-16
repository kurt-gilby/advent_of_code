from helper import get_input
from itertools import permutations


def get_destinations_map(directions: list[str]) -> dict[str:int]:
    destinations = {}
    tot_destinations = []
    for direction in directions:
        line = direction.replace(" to ", "->").replace(" = ", " ")
        line_split = line.split()
        station_split = line_split[0].split("->")
        destinations[station_split[0] + "->" + station_split[1]] = int(line_split[1])
        destinations[station_split[1] + "->" + station_split[0]] = int(line_split[1])
        tot_destinations.append(station_split[0])
        tot_destinations.append(station_split[1])
    tot_destinations = list(set(tot_destinations))

    return destinations, tot_destinations


def get_all_routes(tot_dest):
    if len(tot_dest) == 0:
        return []
    if len(tot_dest) == 1:
        return [tot_dest]

    combos = []

    for i in range(len(tot_dest)):
        current = tot_dest[i]
        remaining = tot_dest[:i] + tot_dest[i + 1 :]
        for p in get_all_routes(remaining):
            combos.append([current] + p)
    return combos


def solved_part_one_and_two():
    year = "2015"
    file = "input_day_9.txt"
    path = f"./{year}/{file}"
    input_lines = get_input(path)
    destinations, tot_dest = get_destinations_map(input_lines)

    routes = get_all_routes(tot_dest)
    min_dist = float("inf")
    max_dist = 0
    for route in routes:
        tot_dist = 0
        for i in range(len(route) - 1):
            dist = destinations[route[i] + "->" + route[i + 1]]
            tot_dist += dist
        min_dist = min(tot_dist, min_dist)
        max_dist = max(tot_dist, max_dist)
    print(f"The distance of the shortest route is {min_dist}")
    print(f"The distance of the longest route is {max_dist}")


if __name__ == "__main__":
    solved_part_one_and_two()
