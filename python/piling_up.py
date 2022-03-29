from collections import deque

t = int(input())


def stack(n, s):
    for max_in_q in reversed(sorted(q)):
        if max_in_q == q[0]:
            q.popleft()
        elif max_in_q == q[-1]:
            q.pop()
        else:
            return "No"
    return "Yes"


for _ in range(t):
    n = int(input())
    s = list(map(int, input().split()))
    q = deque(s)
    r = stack(len(s), q)
    print(r)
