import time


def jins_sol_up_down_left_right():
    n = int(input())
    directions = input().split()

    start_time = time.time()

    point = [1, 1]

    vector = {
        #     x   y
        "U": [0, -1],
        "D": [0, 1],
        "L": [-1, 0],
        "R": [1, 0],
    }

    for direction in directions:
        togo_point = [point[i] + vector[direction][i] for i in range(len(point))]

        if (
            togo_point[0] < 1
            or togo_point[0] > n
            or togo_point[1] < 1
            or togo_point[1] > n
        ):
            continue
        point = togo_point

    print(point[0], point[1])

    end_time = time.time()
    print("process time: ", end_time - start_time)


def sol_up_down_left_right():
    n = int(input())
    plans = input().split()

    start_time = time.time()
    x, y = 1, 1
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    move_types = ["L", "R", "U", "D"]

    for plan in plans:
        for i in range(len(move_types)):
            if plan == move_types[i]:
                nx = x + dx[i]
                ny = y + dy[i]
        if nx < 1 or ny < 1 or nx > n or ny > n:
            continue
        x, y = nx, ny

    print(x, y)

    end_time = time.time()
    print("process time: ", end_time - start_time)


def jins_sol_time():
    n = int(input())

    start_time = time.time()
    hours = [0 for hour in range(n + 1)]
    minutes = [0 for minute in range(60)]
    seconds = [0 for second in range(60)]

    minutes_3 = [3, 13, 23, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 43, 53]
    seconds_3 = [3, 13, 23, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 43, 53]

    """
    아래 solution 참조해서 기억할 것. 너무나도 쉽다.
    """
    end_time = time.time()
    print("process time: ", end_time - start_time)


def sol_time():
    h = int(input())
    start_time = time.time()
    count = 0
    for i in range(h + 1):
        for j in range(60):
            for k in range(60):
                if "3" in str(i) + str(j) + str(k):
                    count += 1
    print(count)
    end_time = time.time()
    print("process time: ", end_time - start_time)


def jins_sol_kingdom_knight():
    point = input()
    start_time = time.time()
    count = 0

    if point[0] < "a" or point[0] > "h" or point[1] < "1" or point[1] > "8":
        print("error!")

    point_list = list(point)
    point_list[0] = ord(point_list[0]) - ord("a")
    point_list[1] = ord(point_list[1]) - ord("1")

    vectors = [(1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2)]

    for vector in vectors:
        togo_point = [point_list[i] + vector[i] for i in range(2)]
        if (togo_point[0] >= 0 and togo_point[0] < 8) and (
            togo_point[1] >= 0 and togo_point[1] < 8
        ):
            count += 1

    print(count)

    end_time = time.time()
    print("process time: ", end_time - start_time)


def sol_kingdom_knight():
    input_data = input()

    start_time = time.time()
    row = int(input_data[1])
    column = int(input_data[0]) - int(ord("a")) + 1

    steps = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]

    result = 0
    for step in steps:
        next_row = row + step[0]
        next_column = column + step[1]
        if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <= 8:
            result += 1

    print(result)
    end_time = time.time()
    print("process time: ", end_time - start_time)


def jins_sol_re_sort_string():
    strings = input()
    start_time = time.time()

    result = ""
    sum_of_num = 0
    sum_of_str = ""

    for string in strings:
        if ord(string) >= 48 and ord(string) <= 57:
            sum_of_num += int(string)
        else:
            sum_of_str += string

    result = "".join(sorted(sum_of_str)) + '' if sum_of_num == 0 else str(sum_of_num)

    print(result)
    end_time = time.time()
    print("process time: ", end_time - start_time)


def sol_re_sort_string():
    data = input()

    start_time = time.time()

    result = []
    value = 0
    
    for x in data:
        if x.isalpha():
            result.append(x)
        else:
            value += int(x)
            
    result.sort()
    
    if value != 0:
        result.append(str(value))

    print(''.join(result))
    
    end_time = time.time()
    print("process time: ", end_time - start_time)

