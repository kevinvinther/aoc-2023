import re


def get_digits(line):
    return re.findall(r'\d+', line)

def add_digits(digits):
    return digits[0][0] + digits[-1][-1]

def find_text_digits(line):
    return re.findall(r'(?=(one|two|three|four|five|six|seven|eight|nine|\d))', line)

def text_to_digit(line):
    new_line = []
    for text in line:
        match text:
            case 'one':
                new_line.append('1')
            case 'two':
                new_line.append('2')
            case 'three':
                new_line.append('3')
            case 'four': 
                new_line.append('4')
            case 'five':
                new_line.append('5')
            case 'six':
                new_line.append('6')
            case 'seven':
                new_line.append('7')
            case 'eight':
                new_line.append('8')
            case 'nine':
                new_line.append('9')
            case _:
                new_line.append(text) # well, it isn't lol
    return new_line


def part1(input):
    sum = 0
    for line in input:
        sum += int(add_digits(get_digits(line)))
    return sum

def part2(input):
    sum = 0
    for line in input:
        sum += int(add_digits(text_to_digit(find_text_digits(line))))
    return sum

if __name__ == "__main__":
    real_input = open("1.txt").readlines()
    print("Part 1: " + str(part1(real_input)))
    print("Part 2: " + str(part2(real_input)))
