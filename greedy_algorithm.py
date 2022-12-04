import time


def jins_sol_until_1():
    n, k = map(int, input().split())
    count = 0

    while n > 1:
        if n % k == 0:
            count += 1
            n //= k
        else:
            if n < k:
                count += n % k - 1
                n -= n % k - 1
            else:
                count += n % k
                n -= n % k

    print(count)


def sol_until_1():
    n, k = map(int, input().split())
    result = 0

    while True:
        target = (n // k) * k
        result += n - target
        n = target
        if n < k:
            break
        result += 1
        n //= k

    result += n - 1
    print(result)


def jins_sol_multiple_or_summation():
    numbers = input()
    num_list = []
    for number in numbers:
        num_list.append(number)

    start_time = time.time()
    result = 0
    num_list = list(map(int, num_list))

    if num_list[0] < 2 or num_list[1] < 2:
        result = num_list[0] + num_list[1]
    else:
        result = num_list[0] * num_list[1]

    del num_list[:2]

    for number in num_list:
        if number > 1:
            result *= number
        else:
            result += number
    print(result)
    end_time = time.time()
    print(end_time - start_time)


def sol_multiple_or_summation():
    data = input()

    start_time = time.time()
    result = int(data[0])

    for i in range(1, len(data)):
        num = int(data[i])
        if num <= 1 or result <= 1:
            result += num
        else:
            result *= num
    print(result)
    end_time = time.time()
    print(end_time - start_time)


def jins_sol_advanturer_guild():
    n = input()
    fear_levels = list(map(int, input().split()))

    start_time = time.time()

    result = 0
    group_num = 0

    fear_levels.sort()

    for fear in fear_levels:
        group_num += 1
        if group_num >= fear:
            result += 1
            group_num = 0

    print("Result :", result)
    end_time = time.time()
    print(end_time - start_time)


def sol_advanturer_guild():
    n = input()
    data = list(map(int, input().split()))

    start_time = time.time()

    data.sort()

    result = 0
    count = 0

    for i in data:
        count += 1
        if count >= i:
            result += 1
            count = 0
            
    print(result)

    end_time = time.time()
    print(end_time - start_time)


jins_sol_advanturer_guild()
