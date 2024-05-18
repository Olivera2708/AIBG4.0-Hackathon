from queue import PriorityQueue

def get_legal_moves(board, position, home):
    moves = []

    x = position[0] - 1
    while x >= 0:
        if board[x][position[1]] == 'E' or board[x][position[1]] == board[home[0]][home[1]]:
            moves.append((x, position[1]))
        else: break
        x -= 1

    x = position[0] + 1
    while x < 10:
        if board[x][position[1]] == 'E' or board[x][position[1]] == board[home[0]][home[1]]:
            moves.append((x, position[1]))
        else: break
        x += 1

    y = position[1] - 1
    while y >= 0:
        if board[position[0]][y] == 'E' or board[position[0]][y] == board[home[0]][home[1]]:
            moves.append((position[0], y))
        else: break
        y -= 1
    
    y = position[1] + 1
    while y < 10:
        if board[position[0]][y] == 'E' or board[position[0]][y] == board[home[0]][home[1]]:
            moves.append((position[0], y))
        else: break
        y += 1
    return moves

def distance(start, end):
    if start[0] == end[0] or start[1] == end[1]:
        return 1
    return 2

def manhattan_distance(start, end):
    return abs(start[0] - end[0]) + abs(start[1] - end[1])

def steps_len(current, move):
    if current[0] == move[0]:
        return abs(current[1] - move[1])
    return abs(current[0] - move[0])

def steps_from_moves(path):
    length = 0
    for i in range(len(path) - 1):
        length += steps_length(path[i], path[i+1])
    return length

def steps_length(position1, position2):
    if position1[0] == position2[0]:
        return abs(position1[1] - position2[0])
    return abs(position1[0] - position2[0])

def get_moves(board, player_position, goal_position, home):
    queue = PriorityQueue()
    queue.put((0, player_position, [player_position]))
    visited = set()

    while not queue.empty():
        _, current, path = queue.get()
        if current == goal_position:
            return path
        if current not in visited:
            visited.add(current)
            for move in get_legal_moves(board, current, home):
                if move not in visited:
                    priority = len(path) + distance(move, goal_position) + steps_from_moves(path) + manhattan_distance(move, goal_position)
                    queue.put((priority, move, path + [move]))
    return None

def get_moves_diamond(board, player_position, goal_positions, home):
    queue = PriorityQueue()
    queue.put((0, player_position, [player_position]))
    visited = set()

    while not queue.empty():
        _, current, path = queue.get()
        if current in goal_positions:
            return path
        if current not in visited:
            visited.add(current)
            for move in get_legal_moves(board, current, home):
                if move not in visited:
                    priority = len(path) + min([distance(move, goal_position) for goal_position in goal_positions]) + steps_from_moves(path) + min([manhattan_distance(move, goal_position) for goal_position in goal_positions])
                    queue.put((priority, move, path + [move]))
    return None

def get_neigbour(position):
    result = []
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    for direction in directions:
        new_position = (direction[0] + position[0], direction[1] + position[1])
        if 0 <= new_position[0] < 10 and 0 <= new_position[1] < 10:
            result.append(new_position)
    return result

# if __name__ == "__main__":
#     with open("test.json") as file:
#         json_data = json.load(file)
#     # print(json_data["board"][0][0])
#     p = json.dumps(json_data, indent=4)
#     # print(p)
#     # print((1,1)==(1,1))
#     board = json_data["board"]
#     # moves = get_moves(board, (0, 8), (8, 3))
#     moves = get_legal_moves(board, (9, 9), (9, 0))
#     print(moves)