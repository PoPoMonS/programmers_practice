import time


def recursive_function(i):
    if i == 100:
        return
    print(i, "번째 재귀함수에서", i + 1, "번째 재귀함수를 호출합니다.")  # 1 ~ 100 까지 증가하며 호출된 후,
    recursive_function(i + 1)
    print(i, "번째 재귀함수를 종료합니다.")  # 99 ~ 1 까지 감소하며 종료된다. stack 구조와 동일.
    # 무한대로 recursive function 이 호출되진 않는다. 제한이 있어 자동 종료됨.


def factorial_iterative(n):
    result = 1

    for i in range(1, n + 1):
        result *= i

    return result


def factorial_recursive(n):
    if n <= 1:
        return 1

    return n * factorial_recursive(n - 1)


def euclidean_algorithm_gcd(a, b):
    r = a % b
    if r == 0:
        return b

    return euclidean_algorithm_gcd(b, r)
