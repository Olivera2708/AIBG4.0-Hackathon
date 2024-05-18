# from collections import deque
# import numpy as np


# def move_matrix(position, board):
#     x_pos, y_pos = position
#     turns = np.full((10, 10), np.inf)
#     queue = deque([(x_pos, y_pos, 0)])
#     turns[x_pos, y_pos] = 0
#     directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
#     while queue:
#         x, y, turn = queue.popleft()
#         for dx, dy in directions:
#             nx, ny = x, y
#             while 0 <= nx < 10 and 0 <= ny < 10 and board[nx][ny] == 'E':
#                 if turns[nx, ny] == np.inf:
#                     turns[nx, ny] = turn + 1
#                     queue.append((nx, ny, turn + 1))
#                 nx += dx
#                 ny += dy
#     return turns

# def get_steps(start, end):
#     if start[0] == end[0]:
#         return abs(start[1]-end[1])
#     return abs(start[0]-end[0])

# def mine_energy(ore):
#     if "D" in ore:
#         return -6
#     else:
#         return -5
    
# def attack_energy():
#     return -100

# def rest_energy():
#     return 20

# def moves_energy(steps, backpack_capacity):
#     return -steps*min(1 + backpack_capacity, 8)

