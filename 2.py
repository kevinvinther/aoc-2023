import re


def parse(line):
    balls = []
    for group in line.split(';'):
        matches = re.findall("(\d+)\s(\w+)", group)
        if matches: 
            balls.append([[int(num), color] for num, color in matches])
    return balls

def count_balls(balls, reqs, game_id):
    balls_count = {}
    needed = {}
    for num, color in enumerate(['red', 'green', 'blue']):
        needed[color] = reqs[num][0]
    is_ok = True

    for group in balls:
        for color in ['green', 'blue', 'red']:
            balls_count[color] = 0
        for pair in group:
            balls_count[pair[1]] += pair[0]

        if balls_count['red'] > needed['red'] or balls_count['blue'] > needed['blue'] or balls_count['green'] > needed['green']:
            is_ok = False

    if is_ok: 
        return game_id
    return 0

def minimum_balls(balls):
    balls_max = {}
    for color in ['green', 'blue', 'red']:
        balls_max[color] = 0

    for group in balls:
        for pair in group:
            if balls_max[pair[1]] < pair[0]:
                balls_max[pair[1]] = pair[0]

    return balls_max['red'] * balls_max['green'] * balls_max ['blue']


def part1(input, requirements):
    sum = 0
    game_id = 0
    for line in input.readlines():
        game_id += 1
        sum += count_balls(parse(line), requirements, game_id)

    return sum


def part2(input):
    sum = 0 
    for line in input.readlines():
        sum += minimum_balls(parse(line))

    return sum

if __name__ == "__main__":
    requirements = [[12, 'red'], [13, 'green'], [14, 'blue']]
    input = open("2.txt")
    print("Part 1: " + str(part1(input, requirements)))
    input = open("2.txt")
    print("Part 2: " + str(part2(input)))
