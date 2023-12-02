import re

"""
This solves the second problem, I overwrote the code to solve the first problem with this one.
"""
pathToFile = "C:/Users/David/PycharmProjects/AdventOfCode/2023/DayOneInput.txt"
answer = 0
wordToInt = {'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}

with open(pathToFile, 'r') as f:
    lines = f.readlines()
    for line in lines:
        # String to put all number words (changed to ints) and ints into this string to form final number
        intString = ''
        # String to take first and last ints from intString
        finalValue = ''
        # Uses look ahead '?=' in regex to find overlapping number words
        ints = re.findall(r'(?=(one|two|three|four|five|six|seven|eight|nine|\d))', line)
        # replace number words with int string value, else adds int string values, to intString
        for value in ints:
            if value in wordToInt.keys():
                value = wordToInt[value]
                intString += value
            else:
                intString += value
        # Get first and last value of string
        finalValue += intString[0]
        finalValue += intString[-1]

        answer += int(finalValue)
    print(answer)
