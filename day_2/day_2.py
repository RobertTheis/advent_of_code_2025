INPUT_FILE_PATH = "day_2\input_day_2.txt"
OUTPUT_FILE_PATH_A = "day_2\\result_day_2_part_1.txt"
OUTPUT_FILE_PATH_B = "day_2\\result_day_2_part_2.txt"

def part_1() -> None:
    false_id_list = []
    false_id_sum = 0
    range_list = transform_input(file=INPUT_FILE_PATH)

    for range in range_list:
        for value in range:
            value_str = str(value)
            if len(value_str) % 2 == 0:
                mid = len(value_str) // 2
                pre = value_str[:mid]
                suf = value_str[mid:]
                if pre == suf:
                    false_id_list.append(value)

    with open(OUTPUT_FILE_PATH_A, "a") as output_file:
        output_file.write("Gefundene IDs:\n")
        for id in false_id_list:
            output_file.write(str(id) + "\n")
            false_id_sum += id
        output_file.write(f"\nSumme der gefundenen IDs: {false_id_sum}")


def part_2() -> None:
    false_id_list = []
    false_id_sum = 0
    range_list = transform_input(file=INPUT_FILE_PATH)

    for range in range_list:
        for value in range:
            value_str = str(value)
            substrings = split_into_equal_substrings(value=value_str)
            for elem in substrings:
                if len(set(elem)) == 1:
                    false_id_list.append(value)
                    break

    with open(OUTPUT_FILE_PATH_B, "a") as output_file:
        output_file.write("Gefundene IDs:\n")
        for id in false_id_list:
            output_file.write(str(id) + "\n")
            false_id_sum += id
        output_file.write(f"\nSumme der gefundenen IDs: {false_id_sum}")


def transform_input(file: str) -> list:
    '''Function to read and prepare the input from the input file for the task ahead. 
       Converts the input line into a list of arrays that contain every number in the given range.
    '''
    range_list = []
    result_list = []
    with open(file) as input_line:
        for line in input_line:
            range_list = line.split(",")

    for id_range in range_list:
        complete_range = []
        min_max = id_range.split("-")
        for i in range(int(min_max[0]), int(min_max[1]) + 1):
            complete_range.append(i)
        result_list.append(complete_range)

    return result_list


def split_into_equal_substrings(value: str) -> list:
    n = len(value)
    results = []

    if n % 2 == 0:
        substring_sizes = range(2, n // 2 + 1)
    else:
        substring_sizes = range(1, n // 2 + 1, 2)

    for s in substring_sizes:
        if n % s == 0:
            substrings = [value[i:i+s] for i in range(0, n, s)]
            results.append(substrings)

    return results



if __name__ == "__main__":
    part_1()
    part_2()