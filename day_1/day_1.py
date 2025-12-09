'''PART 1'''
zero_counter = 0
current_position = 50
output_txt = f"Starting position: {current_position}\n\n"

with open("day_1\input_day_1.txt") as input_lines, open("day_1\\result_day_1_part_1.txt", "w") as output_file:
    for line in input_lines:
        line = line.strip()
        steps = int(line[1:])
        
        if line.startswith("R"):
            current_position = current_position + (steps % 100)
            if current_position > 99:
                current_position = current_position - 100
        elif line.startswith("L"):
            current_position = current_position - (steps % 100)
            if current_position < 0:
                current_position = 100 + current_position
        
        if current_position == 0:
            zero_counter += 1

        output_txt += f"Instruction: {line}\nNew current position: {current_position}\nZero Counter: {zero_counter}\n----------\n"
    
    output_txt += f"\nFinal zero counter: {zero_counter}"
    output_file.write(output_txt)


'''PART 2'''
zero_counter = 0
current_position = 50
output_txt = f"Starting position: {current_position}\n\n"
with open("day_1\input_day_1.txt") as input_lines, open("day_1\\result_day_1_part_2.txt", "w") as output_file:
    for line in input_lines:
        line = line.strip()
        times_hit_zero = 0
        steps = int(line[1:])
        move_starts_at = current_position
        if steps >= 100:
            times_hit_zero += int(steps / 100)
        
        if line.startswith("R"):
            current_position = current_position + (steps % 100)
            if current_position > 99:
                current_position = current_position - 100
                if current_position != 0 and move_starts_at != 0:
                    times_hit_zero += 1
        elif line.startswith("L"):
            current_position = current_position - (steps % 100)
            if current_position < 0:
                current_position = 100 + current_position
                if current_position != 0 and move_starts_at != 0:
                    times_hit_zero += 1
        
        if current_position == 0:
            times_hit_zero += 1

        zero_counter += times_hit_zero

        output_txt += f"Starting position: {move_starts_at}\nInstruction: {line}\nNew current position: {current_position}\nClicks at 0: {times_hit_zero}\nZero Counter: {zero_counter}\n----------\n"
    
    output_txt += f"\nFinal zero counter: {zero_counter}"
    output_file.write(output_txt)