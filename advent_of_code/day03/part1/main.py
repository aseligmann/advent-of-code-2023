import os
import re
import numpy as np
import scipy


def parse_line(lines):
    n_lines = len(lines)
    n_chars_per_line = len(lines[0])

    # Matrix describing validity
    mat_valid = np.full((n_lines, n_chars_per_line), False)

    # Mark symbols
    for row, line in enumerate(lines):
        for col, char in enumerate(line):
            if char.isdigit() or char == ".":
                continue
            mat_valid[row, col] = True

    # Dilate
    mat_valid = scipy.ndimage.binary_dilation(
        mat_valid,
        [
            [True, True, True],
            [True, True, True],
            [True, True, True],
        ],
    )

    # Unmark dots
    for row, line in enumerate(lines):
        for col, char in enumerate(line):
            if not char.isdigit():
                mat_valid[row, col] = False

    # Expand digits
    mat_valid_new = mat_valid
    rows, cols = mat_valid.shape
    for row in range(rows):
        for col in range(cols):
            if mat_valid[row, col]:
                # Traverse left
                col_tmp = col
                while col_tmp > 0:
                    col_tmp -= 1
                    if lines[row][col_tmp].isdigit():
                        mat_valid_new[row, col_tmp] = True
                    else:
                        break
                # Traverse right
                col_tmp = col
                while col_tmp < cols - 1:
                    col_tmp += 1
                    if lines[row][col_tmp].isdigit():
                        mat_valid_new[row, col_tmp] = True
                    else:
                        break
    mat_valid = mat_valid_new

    # Extract numbers
    numbers = []
    number_tmp = ""
    for row in range(rows):
        for col in range(cols):
            if mat_valid[row, col]:
                char = lines[row][col]
                if char.isdigit():
                    # If number, append to tmp
                    number_tmp += char
            elif number_tmp != "":
                # Otherwise if tmp is not empty, append to list and reset
                numbers.append(int(number_tmp))
                number_tmp = ""

    return numbers


def main():
    print("Advent of Code 2023 - Day 03 - part 1")
    dirname = os.path.dirname(__file__)
    input_file = os.path.join(dirname, "input.txt")

    results = []
    with open(input_file, "r") as f:
        lines = []
        for line in f:
            lines.append(line.rstrip("\n"))
        res = parse_line(lines)
        results.append(res)

    results = np.asarray(results)
    sum = results.sum()
    print(f"Sum: {sum}")


if __name__ == "__main__":
    main()
