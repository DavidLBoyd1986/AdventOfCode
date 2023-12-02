
pathToInput = "C:/Users/David/PycharmProjects/AdventOfCode/2023/DayTwoInput.txt"
with open(pathToInput, 'r') as f:
    testData = f.readlines()

pathToExample = "C:/Users/David/PycharmProjects/AdventOfCode/2023/DayTwoExampleInput.txt"
with open(pathToExample, 'r') as f:
    exampleData = f.readlines()

maxCubes = {'red': 12, 'green': 13, 'blue': 14}


def problem_one(test_data, constraints):
    total = 0

    for line in test_data:
        print(line)
        constraint_broke = False
        split_game_data = line.split(":")
        game_number = split_game_data[0].split(' ')[1]
        game_data = split_game_data[1]

        # Loop through subsets in game
        for subset in game_data.split(';'):
            print(subset)
            # Loop through values in subset, and break if any value goes over its constraint value
            for value in subset.split(','):
                split_value = value.split(' ')
                number = int(split_value[1])
                color = split_value[2].rstrip('\n')
                if number > constraints[color]:
                    constraint_broke = True
                    print('This game was invalid\n')
                    break
            if constraint_broke:
                break
        # If you made it through all subsets, and constraint didn't break, it's a valid game
        if not constraint_broke:
            total += int(game_number)
            print('This game was valid\n')

    return total


def problem_two(test_data):
    total = 0

    for line in test_data:
        print(line)
        split_game_data = line.split(":")
        game_data = split_game_data[1]
        max_color_tracker = {'red': 0, 'green': 0, 'blue': 0}

        # Loop through subsets in game
        for subset in game_data.split(';'):
            print(subset)
            # Loop through values in subset and track the max value of each color
            for value in subset.split(','):
                split_value = value.split(' ')
                number = int(split_value[1])
                color = split_value[2].rstrip('\n')
                if number > max_color_tracker[color]:
                    max_color_tracker[color] = number
        power = 1
        for value in max_color_tracker.values():
            power *= value
        total += power

    return total


answer = problem_one(testData, maxCubes)
print('Problem One Answer: ' + str(answer))

answer = problem_two(testData)
print('Problem Two Answer: ' + str(answer))
