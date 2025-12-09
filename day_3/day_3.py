INPUT_FILE_PATH = "day_3\\input_day_3.txt"
OUTPUT_FILE_1 = "day_3\\result_day_3_part_1.txt"
OUTPUT_FILE_2 = "day_3\\result_day_3_part_2.txt"

def part_1() -> None:

    with open(INPUT_FILE_PATH) as input_file, open(OUTPUT_FILE_1, "a") as output_file:
        total_joltage = 0
        for line in input_file:
            output_file.write(f"Betrachtete Bank: {line}\n")
            first_digit = 0
            first_digit_index = 0
            second_digit = 0
            for char in line.strip()[:-1]:
                if int(char) > first_digit:
                    first_digit = int(char)
                    first_digit_index = line.index(char)
                if first_digit == 9:
                    break

            output_file.write(f"Found first digit {first_digit} at index {first_digit_index}.\n")

            for char in line.strip()[(first_digit_index + 1):]:
                if int(char) > second_digit:
                    second_digit = int(char)
                if second_digit == 9:
                    break
            
            found_joltage = first_digit * 10 + second_digit
            total_joltage += found_joltage

            output_file.write(f"Found joltage of {found_joltage} in this bank.\nTotal joltage is now {total_joltage}\n")
            output_file.write("-----------------\n")


        output_file.write(f"\nFinal joltage: {total_joltage}")


def part_2() -> None:

    with open(INPUT_FILE_PATH) as input_file, open(OUTPUT_FILE_2, "a") as output_file:
        total_joltage = 0
        for line in input_file:
            output_file.write(f"Betrachtete Bank: {line}\n")
            found_digits = []
            current_index = 0
            for i in range(11, -1, -1):
                current_index = find_index_of_highest_digit(line, current_index, i)
                found_digits.append(line[current_index])
                current_index += 1

            total_joltage += build_joltage_from_digits(found_digits) 

            output_file.write(f"Found joltage of {build_joltage_from_digits(found_digits)} in this bank.\nTotal joltage is now {total_joltage}\n")
            output_file.write("-----------------\n")

        output_file.write(f"\nFinal joltage: {total_joltage}")
                
def build_joltage_from_digits(input_list: list) -> int:
    digit_string = ""
    for elem in input_list:
        digit_string += elem

    return int(digit_string)


def find_index_of_highest_digit(line: str, lower_limit: int, upper_limit: int) -> int:
    highest_digit = 0
    current_sub_index = 0
    if upper_limit == 0:
        upper_limit = len(line) * (-1)

    for char in line.strip()[lower_limit:upper_limit*(-1)]:
        if int(char) > highest_digit:
            highest_digit = int(char)
            current_sub_index = line.strip()[lower_limit:upper_limit*(-1)].index(char)
        if highest_digit == 9:
            break

    return current_sub_index + lower_limit



if __name__ == "__main__":
    part_2()