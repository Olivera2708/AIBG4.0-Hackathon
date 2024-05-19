from collections import deque
import search

def get_next_to_opponent_home(home):
    if home == (0, 9):
        return (1, 9), (0, 8)
    else:
        return (8, 0), (9, 1)
    
def get_between_home(home):
    if home == (0, 9):
        return (1, 8)
    else:
        return (8, 1)


def move_matrix(position, board, player):
    x_pos, y_pos = position
    turns = [[float('inf')] * 10 for _ in range(10)]
    queue = [(x_pos, y_pos, 0)]
    turns[x_pos][y_pos] = 0
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    while queue:
        x, y, turn = queue.pop(0)
        for dx, dy in directions:
            nx, ny = x, y
            while 0 <= nx < 10 and 0 <= ny < 10 and (board[nx][ny] == 'E' or board[nx][ny] == "A" or board[nx][ny] == "B" or board[nx][ny] == player):
                if turns[nx][ny] == float('inf'):
                    turns[nx][ny] = turn + 1
                    queue.append((nx, ny, turn + 1))
                nx += dx
                ny += dy
    return turns

def get_steps(start, end):
    if start[0] == end[0]:
        return abs(start[1]-end[1])
    return abs(start[0]-end[0])

def mine_energy(ore):
    if "D" in ore:
        return -6
    else:
        return -5
    
def attack_energy():
    return -100

def rest_energy():
    return 20

def moves_energy(steps, backpack_capacity):
    return -steps*min(1 + backpack_capacity, 8)

def get_player(player, game_state):
    if player == "my":
        if game_state.first_player:
            return game_state.player1
        else:
            return game_state.player2
    else:
        if game_state.first_player:
            return game_state.player2
        else:
            return game_state.player1
        

def should_attack_house(game_state):
    try:
        my_player = get_player("my", game_state)
        opponent_player = get_player("opponent", game_state)

        if game_state.first_player:
            pl_my = "1"
            pl_op = "2"
        else:
            pl_my = "2"
            pl_op = "1"

        my_matrix = move_matrix(my_player.position, game_state.board, pl_my)
        opponent_matrix = move_matrix(opponent_player.position, game_state.board, pl_op)

        opponent_home = game_state.get_opponent_home();
        next_to_home1, next_to_home2 = get_next_to_opponent_home(opponent_home)

        opponent_moves_to_home_1 = opponent_matrix[next_to_home1[0]][next_to_home1[1]]
        opponent_moves_to_home_2 = opponent_matrix[next_to_home2[0]][next_to_home2[1]]

        if opponent_moves_to_home_1 < opponent_moves_to_home_2:
            next_to_home = next_to_home1
            opponent_moves_to_home = opponent_moves_to_home_1
        elif opponent_moves_to_home_1 < opponent_moves_to_home_2:
            next_to_home = get_between_home(opponent_home)
            opponent_moves_to_home = opponent_moves_to_home_1
        else:
            next_to_home = next_to_home2
            opponent_moves_to_home = opponent_moves_to_home_2

        my_moves_to_opponent_home = my_matrix[next_to_home[0]][next_to_home[1]]

        path_to_opponent_home = search.get_moves(game_state.board, tuple(my_player.position), next_to_home, game_state.get_my_home())
        steps_to_opponent_home = search.steps_from_moves(path_to_opponent_home)
        energy_consumption = moves_energy(steps_to_opponent_home, my_player.backpack_capacity)

        if my_player.xp > opponent_player.xp or (my_player.xp == opponent_player.xp and my_player.coins > opponent_player.coins):
            if my_moves_to_opponent_home <= opponent_moves_to_home and my_player.energy > energy_consumption:
                return True, path_to_opponent_home[1]
        return False, None
    except:
        return False, None
