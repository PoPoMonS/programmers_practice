from collections import deque


def stack():
    stack = []

    stack.append(3)
    stack.append(0)
    stack.append(1)
    stack.pop()
    stack.append(9)

    print(stack)  # 오래된 순서대로
    print(stack[::-1])  # 최신 순서대로


def queue():
    queue = deque()
    
    queue.append(3)
    queue.append(0)
    queue.append(1)
    queue.popleft()
    queue.append(9)
    
    print(queue)    # 오래된 순서대로
    queue.reverse()
    print(queue)    # 최신 순서대로
    
