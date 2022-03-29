from collections import deque

ops = ["append", "pop", "popleft", "appendleft"]
d = deque()


num_ops = int(input())
ops_left = num_ops

while ops_left > 0:

    operation = input().split()
    if operation[0] == ops[0]:
        d.append(operation[1])
        ops_left -= 1
    elif operation[0] == ops[1]:
        d.pop()
        ops_left -= 1
    elif operation[0] == ops[2]:
        d.popleft()
        ops_left -= 1
    elif operation[0] == ops[3]:
        d.appendleft(operation[1])
        ops_left -= 1
    else:
        pass

for i in d:
    print(i, end=' ')
