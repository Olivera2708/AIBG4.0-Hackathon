import sys
import time
import json
import options
from game_state import GameState
import evaluate
import search

while True:
    line = sys.stdin.readline().strip()
#     line = {"turn":8,"firstPlayerTurn":True,"player1":{"name": "sss","energy": 981,"xp": 0,"coins": 100,"position": [7, 2],"increased_backpack_duration": 0,"daze_turns": 0,"frozen_turns": 0,"backpack_capacity": 2,"raw_minerals": 1,"processed_minerals": 0,"raw_diamonds": 0,"processed_diamonds": 0},"player2":{"name": "Topic Team","energy": 991,"xp": 0,"coins": 50,"position": [7, 7],"increased_backpack_duration": 0,"daze_turns": 0,"frozen_turns": 0,"backpack_capacity": 0,"raw_minerals": 0,"processed_minerals": 0,"raw_diamonds": 0,"processed_diamonds": 0},"board":[
# ["E", "E", "E", "D_3_0", "M_6_0", "E", "E", "E", "F_2_3", "B"],
# ["E", "D_3_0", "E", "E", "E", "M_6_0", "M_6_0", "M_6_0", "E", "E"],
# ["E", "E", "E", "E", "E", "E", "E", "E", "M_6_0", "E"],
# ["D_3_0", "E", "E", "E", "E", "E", "M_6_0", "E", "M_6_0", "E"],
# ["M_6_0", "E", "E", "E", "D_3_0", "M_6_0", "E", "E", "M_6_0", "E"],
# ["E", "M_6_0", "E", "E", "M_6_0", "E", "E", "E", "M_6_0", "E"],
# ["E", "M_6_0", "E", "M_6_0", "E", "E", "E", "E", "M_6_0", "E"],
# ["E", "M_6_0", "1", "E", "E", "E", "E", "2", "E", "E"],
# ["E", "E", "M_5_0", "M_6_0", "M_6_0", "M_6_0", "M_6_0", "E", "E", "E"],
# ["A", "E", "E", "E", "E", "E", "E", "E", "E", "E"]
# ]}

    data = json.loads(line)
    game_state = GameState.from_json(data)

    should_attack, move = evaluate.should_attack_house(game_state)
    if should_attack:
        options.move(move[0], move[1])
        continue

    if game_state.player1.backpack_capacity > 0:
        if tuple(game_state.player1.position) == game_state.get_my_home():
            if game_state.player1.energy < 150 and (game_state.player1.raw_diamonds > 0 or game_state.player1.raw_minerals > 0):
                options.convert(0,0,game_state.player1.raw_diamonds,game_state.player1.raw_minerals,0,0)
            else:
                options.convert(0,0,0,0,game_state.player1.raw_diamonds,game_state.player1.raw_minerals)
            continue

        next_move = search.get_moves(game_state.board, tuple(game_state.player1.position), game_state.get_my_home(), game_state.get_my_home())
        if next_move is None:
            options.rest()
            continue
        next_move = next_move[1]
        options.move(next_move[0], next_move[1])
        pass
    else:
        neighbours = search.get_neigbour(game_state.player1.position)
        boolean = False
        diamonds = game_state.get_diamonds()
        minerals = game_state.get_minerals()
        for neighbour in neighbours:
            if (game_state.board[neighbour[0]][neighbour[1]][0] == "D" or (game_state.board[neighbour[0]][neighbour[1]][0] == "M")) and game_state.board[neighbour[0]][neighbour[1]][2] != "0":
                options.mine(neighbour[0], neighbour[1])
                boolean = True
                break
        if boolean: continue

        diamonds_neighbours = []
        mineral_neighbours = []
        for diamond in diamonds:
            diamonds_neighbours.extend(search.get_neigbour(diamond))
        for mineral in minerals:
                mineral_neighbours.extend(search.get_neigbour(mineral))
        if len(diamonds) == 0:
            next_move = search.get_moves_diamond(game_state.board, tuple(game_state.player1.position), mineral_neighbours, game_state.get_my_home())
        else:
            next_move = search.get_moves_diamond(game_state.board, tuple(game_state.player1.position), diamonds_neighbours, game_state.get_my_home())
        if next_move is None:
            next_move = search.get_moves_diamond(game_state.board, tuple(game_state.player1.position), mineral_neighbours, game_state.get_my_home())

        # print(evaluate.move_matrix((0,0), game_state.board))
        # print(next_move)
        next_move = next_move[1]
        options.move(next_move[0], next_move[1])

