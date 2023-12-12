import os
import re
import numpy as np
import scipy


def parse_line(lines):
    n_lines = len(lines)
    n_chars_per_line = len(lines[0])

    # Matrix describing validity
    mat_id = np.full((n_lines, n_chars_per_line), 0)

    # Mark symbols
    id = 1
    ids = []
    for row, line in enumerate(lines):
        for col, char in enumerate(line):
            if char.isdigit() or char == ".":
                continue
            mat_id[row, col] = id
            ids.append(id)
            id += 1

    # Dilate
    for current_id in ids:
        mask = scipy.ndimage.binary_dilation(
            mat_id == current_id,
            [
                [1, 1, 1],
                [1, 1, 1],
                [1, 1, 1],
            ],
        )
        mat_id[mask] = current_id

    # Unmark dots and symbols
    for row, line in enumerate(lines):
        for col, char in enumerate(line):
            if not char.isdigit():
                mat_id[row, col] = 0

    # Expand digits
    mat_id_new = mat_id
    rows, cols = mat_id.shape
    for row in range(rows):
        for col in range(cols):
            current_id = mat_id[row, col]
            if current_id > 0:
                # Traverse left
                col_tmp = col
                while col_tmp > 0:
                    col_tmp -= 1
                    if lines[row][col_tmp].isdigit():
                        mat_id_new[row, col_tmp] = current_id
                    else:
                        break
                # Traverse right
                col_tmp = col
                while col_tmp < cols - 1:
                    col_tmp += 1
                    if lines[row][col_tmp].isdigit():
                        mat_id_new[row, col_tmp] = current_id
                    else:
                        break
    mat_id = mat_id_new

    # Extract numbers
    numbers = {}
    for current_id in ids:
        numbers[current_id] = []

    number_tmp = ""
    current_id = 0
    for row in range(rows):
        for col in range(cols):
            if mat_id[row, col] > 0:
                current_id = mat_id[row, col]
                char = lines[row][col]
                if char.isdigit():
                    # If number, append to tmp
                    number_tmp += char
            elif number_tmp != "":
                # Otherwise if tmp is not empty, append to list and reset
                numbers[current_id].append(int(number_tmp))
                number_tmp = ""

    return numbers


def main():
    print("Advent of Code 2023 - Day 03 - part 2")
    dirname = os.path.dirname(__file__)
    input_file = os.path.join(dirname, "input.txt")

    results = []
    with open(input_file, "r") as f:
        lines = []
        for line in f:
            lines.append(line.rstrip("\n"))
        res = parse_line(lines)
        for key, values in res.items():
            if len(values) == 2:
                results.append(np.prod(values))

    results = np.asarray(results)
    sum = results.sum()
    print(f"Sum: {sum}")


if __name__ == "__main__":
    main()
