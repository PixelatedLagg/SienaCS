from collections import deque

input_array = list(map(int, input().split()))
target = input_array[0]
num_s = input_array[1]
num_l = input_array[2]

board = {i: i for i in range(1, target + 1)}

for _ in range(num_s):
    start, end = map(int, input().split())
    board[start] = end

for _ in range(num_l):
    start, end = map(int, input().split())
    board[start] = end

def min_rolls_to_reach_target():
    queue = deque([(1, 0)])
    visited = set([1]) 
    while queue:
        pos, rolls = queue.popleft()
        if pos == target:
            return rolls  #shortest path!
        for dice_roll in range(1, 7):
            new_pos = pos + dice_roll
            if new_pos <= target:
                new_pos = board[new_pos]     
                if new_pos not in visited:
                    visited.add(new_pos)
                    queue.append((new_pos, rolls + 1))
    return "NOT POSSIBLE"

print(min_rolls_to_reach_target())