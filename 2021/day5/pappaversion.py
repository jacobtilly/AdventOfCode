import time
import requests

def format_input(string):
    string = string.replace(' -> ',',')
    string = string.split(',')
    return string

def initialize(aoc_day):
    cookies = {'session': '53616c7465645f5f48331fe666f5707d9e3befd781f5c51fabba07d8bda7cd73c2ca4daa386497befcf8f4d830f9f123'}
    input_source = requests.post('https://adventofcode.com/2021/day/' + str(aoc_day) + '/input', cookies=cookies)
    input_list = input_source.text[:-1].split('\n')
    input_list = list(map(format_input, input_list))
    max_point = max([int(a) for alist in input_list for a in alist])
    input_list = [[int(a) for a in alist] for alist in input_list]
    return input_list, max_point

def aoc_part_1(input_list, max_point):
    map_list = [[0 for a in range(max_point + 1)] for b in range(max_point + 1)]
    for coords in input_list:
        if coords[0] == coords[2]:
            for y_point in range(min(coords[1],coords[3]),max(coords[1],coords[3])+1):
                map_list[y_point][coords[0]] += 1
        elif coords[1] == coords[3]:
            for x_point in range(min(coords[0],coords[2]),max(coords[0],coords[2])+1):
                map_list[coords[1]][x_point] += 1
    return len([a for alist in map_list for a in alist if a>1])

def aoc_part_2(input_list, max_point):
    map_list = [[0 for a in range(max_point+1)] for b in range(max_point+1)]
    for coords in input_list:
        x1 = coords[0]
        y1 = coords[1]
        x2 = coords[2]
        y2 = coords[3]
        if x2>x1:
            delta_x = 1
        elif x2<x1:
            delta_x = -1
        else:
            delta_x = 0
        if y2>y1:
            delta_y = 1
        elif y2<y1:
            delta_y = -1
        else:
            delta_y = 0
        while (x1 != x2) or (y1 != y2):
            map_list[y1][x1] += 1
            x1 += delta_x
            y1 += delta_y
        map_list[y1][x1] += 1
    return len([a for alist in map_list for a in alist if a>1])

# Main
aoc_day = 5
input_list, max_point = initialize(aoc_day)
start_time = time.time()
print()
print('******************************************')
print('Day ' + str(aoc_day) + ' answer to part 1: ', aoc_part_1(input_list, max_point))
print('Day ' + str(aoc_day) + ' answer to part 2: ', aoc_part_2(input_list, max_point))
print(f'Execution time: {time.time()-start_time:.5f} s')
print('******************************************')
print()
