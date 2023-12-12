import os
import re
import numpy as np


def parse_lines(lines):
    seed_to_soil = []
    soil_to_fertilizer = []
    fertilizer_to_water = []
    water_to_light = []
    light_to_temperature = []
    temperature_to_humidity = []
    humidity_to_location = []

    current_map = None
    for line in lines:
        if "seed-to-soil map" in line:
            current_map = seed_to_soil
        elif "soil-to-fertilizer map" in line:
            current_map = soil_to_fertilizer
        elif "fertilizer-to-water map" in line:
            current_map = fertilizer_to_water
        elif "water-to-light map" in line:
            current_map = water_to_light
        elif "light-to-temperature map" in line:
            current_map = light_to_temperature
        elif "temperature-to-humidity map" in line:
            current_map = temperature_to_humidity
        elif "humidity-to-location map" in line:
            current_map = humidity_to_location

        if (current_map is not None) and (len(line) > 0) and (line[0].isdigit()):
            range_values = re.findall(r"(\d+)", line)
            for i, value in enumerate(range_values):
                range_values[i] = int(value)
            # for i in range(range_values[2]):
            #     current_map[range_values[1] + i] = range_values[0] + i

            mapping = {}
            mapping["src_min"] = range_values[1]
            mapping["src_max"] = range_values[1] + range_values[2] - 1
            mapping["dst_min"] = range_values[0]
            mapping["dst_max"] = range_values[0] + range_values[2] - 1
            mapping["offset"] = mapping["dst_min"] - mapping["src_min"]
            current_map.append(mapping)

    seeds = re.findall(r"(\d+)", lines[0])
    for i, seed in enumerate(seeds):
        seeds[i] = int(seed)

    def get_mapping(value, mappings):
        mapping = None
        for m in mappings:
            if (value >= m["src_min"]) and (value <= m["src_max"]):
                mapping = m
                break
        if mapping is None:
            return value
        else:
            return value + mapping["offset"]

    locations = []
    for seed in seeds:
        soil = get_mapping(seed, seed_to_soil)
        fertilizer = get_mapping(soil, soil_to_fertilizer)
        water = get_mapping(fertilizer, fertilizer_to_water)
        light = get_mapping(water, water_to_light)
        temperature = get_mapping(light, light_to_temperature)
        humidity = get_mapping(temperature, temperature_to_humidity)
        location = get_mapping(humidity, humidity_to_location)
        locations.append(location)

    return locations


def main():
    print("Advent of Code 2023 - Day 05 - part 1")
    dirname = os.path.dirname(__file__)
    input_file = os.path.join(dirname, "input.txt")

    results = None
    with open(input_file, "r") as f:
        lines = []
        for line in f:
            line = line.rstrip("\n")
            lines.append(line)
        results = parse_lines(lines)

    result = np.amin(results)
    print(f"Lowest: {result}")


if __name__ == "__main__":
    main()
