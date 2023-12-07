import string

pathToInput = "C:/Users/David/PycharmProjects/AdventOfCode/2023/DayThreeInput.txt"
with open(pathToInput, 'r') as f:
    testData = f.readlines()

pathToExample = "C:/Users/David/PycharmProjects/AdventOfCode/2023/DayThreeExampleInput.txt"
with open(pathToExample, 'r') as f:
    exampleData = f.readlines()

pathToExample = "C:/Users/David/Desktop/DayThreeExampleInputTwo.txt"
with open(pathToExample, 'r') as f:
    exampleTwoData = f.readlines()


def problem_one(test_data):
    total = 0
    # Get size of grid:
    grid_length = len(test_data[0])-1
    grid_height = len(test_data)
    grid_size = (grid_length, grid_height)
    print(grid_size)
    print('grid_length = ' + str(grid_length))
    # list of parts, a data structure with all required part information
    parts_list = []
    # a list of symbols locations a tuple with (x,y) coordinates
    symbols_list = []
    row_number = 0

    # Loop through rows
    for row in test_data:
        # Lists of parts and symbols to hold for this row, and append to main lists after row has been processed.
        row_parts = []
        row_symbols = []
        # Part initialization values
        part = {}
        part_value = ''
        value_length = 0
        valid_part = False
        # Grid tracking values
        column_number = 0
        previous_character = 'empty'

        # Loop through columns
        for current_character in row:
            # Handle empty characters
            if current_character == '.':
                if previous_character == 'digit':
                    # set length of part value and the complete value
                    part['length'] = value_length
                    part['value'] = part_value
                    row_parts.append(part)
                    # reset part, value_length, and part_value
                    part, value_length, part_value = reset_part()
                previous_character = 'empty'
                column_number += 1
                continue

            if current_character in string.punctuation:
                # since it's a symbol, look in row above for digits to make their part valid
                if row_number > 0:
                    look_above_for_digits(parts_list[row_number - 1], column_number)
                # Add symbol to row_symbol list
                row_symbols.append((row_number, column_number))

                if previous_character == 'digit':
                    # set length of part value, the complete value, and that it's valid
                    part['length'] = value_length
                    part['value'] = part_value
                    part['valid'] = True
                    row_parts.append(part)
                    # reset part, value_length, and part_value
                    part, value_length, part_value = reset_part()
                previous_character = 'symbol'
                column_number += 1
                continue

            if current_character in string.digits:
                # since it's a digit, look in row above for symbols to make this part valid
                if row_number > 0:
                    valid_part = look_above_for_symbols(symbols_list[row_number - 1], column_number)

                if previous_character == 'empty':
                    # row and column are done, 'length', 'value', and 'valid' can change still
                    part = {'row': row_number, 'column': column_number, 'length': 0, 'value': 0, 'valid': False}
                    if valid_part:
                        part['valid'] = True
                    value_length += 1
                    part_value += current_character
                    if column_number >= grid_length-1:
                        part['value'] = part_value
                        part['length'] = value_length
                        row_parts.append(part)
                elif previous_character == 'digit':
                    if valid_part:
                        part['valid'] = True
                    value_length += 1
                    part_value += current_character
                    if column_number >= grid_length-1:
                        part['value'] = part_value
                        part['length'] = value_length
                        row_parts.append(part)
                elif previous_character == 'symbol':
                    part = {'row': row_number, 'column': column_number, 'length': 0, 'value': 0, 'valid': True}
                    if valid_part:
                        part['valid'] = True
                    value_length += 1
                    part_value += current_character
                    if column_number >= grid_length-1:
                        part['value'] = part_value
                        part['length'] = value_length
                        row_parts.append(part)
                previous_character = 'digit'
                column_number += 1
                continue
        # Troubleshooting step, checking for 0 part values
        for part in row_parts:
            if part['value'] == 0:
                print('This part value is 0: ' + row_number + ', ' + column_number)
        parts_list.append(row_parts)
        symbols_list.append(row_symbols)
        row_number += 1
        column_number += 1

    # Loop through character in line and pull out all the parts
    for row in parts_list:
        print(row)
        for part in row:
            if part['valid']:
                total += int(part['value'])
    # Trouble Shooting step
    for row in symbols_list:
        print(row)

    return total


def problem_two(test_data):
    total = 0
    return total


def reset_part():
    part = {}
    value_length = 0
    part_value = ''
    return part, value_length, part_value


def look_above_for_symbols(row_symbols, current_column):
    for symbol in row_symbols:
        if symbol[1] in range(current_column - 1, current_column + 2):
            return True
    return False


def look_above_for_digits(row_parts, current_column):
    for part in row_parts:
        if current_column in range(int(part['column']) - 1, int(part['length'] + part['column']) + 1):
            part['valid'] = True
    return False


answer = problem_one(exampleTwoData)
print('Problem One Answer: ' + str(answer))
f.close()
# answer = problem_two(testData)
# print('Problem Two Answer: ' + str(answer))
