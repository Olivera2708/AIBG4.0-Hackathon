import sys
import time
import json
import options
from game_state import GameState
import evaluate
import search

while True:
    line = sys.stdin.readline().strip()
    data = json.loads(line)
    game_state = GameState.from_json(data)

    player = evaluate.get_player("my", game_state)
    special = evaluate.get_between_home(game_state.get_opponent_home())
    possible1, possible2 = evaluate.get_next_to_opponent_home(game_state.get_opponent_home())

    if game_state.board[special[0]][special[1]] == "E":
        if (player.position[0] == possible1[0] and player.position[1] == possible1[1] and game_state.board[possible2[0]][possible2[1]]) or \
            (player.position[0] == possible2[0] and player.position[1] == possible2[1] and game_state.board[possible1[0]][possible1[1]]):
            options.rest()
            continue
        
        should_attack, move = evaluate.should_attack_house(game_state)
        if should_attack:
            if player.daze_turns > 0:
                move = (2 * player.position[0] - move[0], 2 * player.position[1] - move[1])
            options.move(move[0], move[1])
            continue

        if tuple(player.position) in evaluate.get_next_to_opponent_home(game_state.get_opponent_home()):
            options.rest()
            continue


    next_move = search.get_moves(game_state.board, tuple(player.position), game_state.get_my_home(), game_state.get_my_home())
    if player.backpack_capacity > 6 or (player.backpack_capacity == 5 and search.get_closest_mineral(game_state, player) > len(next_move)):
        if tuple(player.position) == game_state.get_my_home():
            if player.energy < 150 and (player.raw_diamonds > 0 or player.raw_minerals > 0):
                options.convert(0,0,player.raw_diamonds,player.raw_minerals,0,0)
            else:
                options.convert(0,0,0,0,player.raw_diamonds,player.raw_minerals)
            continue

        if next_move is None:
            options.rest()
            continue
        next_move = next_move[1]
        if player.daze_turns > 0:
            next_move = (2 * player.position[0] - next_move[0], 2 * player.position[1] - next_move[1])
        options.move(next_move[0], next_move[1])
        pass
    else:
        neighbours = search.get_neigbour(player.position)
        boolean = False
        diamonds = game_state.get_diamonds()
        minerals = game_state.get_minerals()
        for neighbour in neighbours:
            if ((game_state.board[neighbour[0]][neighbour[1]][0] == "D" and player.backpack_capacity < 4) or (game_state.board[neighbour[0]][neighbour[1]][0] == "M" and player.backpack_capacity < 7)) and game_state.board[neighbour[0]][neighbour[1]][2] != "0":
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

        next_move_d = search.get_moves_diamond(game_state.board, tuple(player.position), diamonds_neighbours, game_state.get_my_home())
        next_move_m = search.get_moves_diamond(game_state.board, tuple(player.position), mineral_neighbours, game_state.get_my_home())

        if next_move_d != None and next_move_m != None:
            if len(next_move_d) <= len(next_move_m) and player.backpack_capacity < 4:
                next_move = next_move_d
            else:
                next_move = next_move_m
        elif next_move_d == None and next_move_m == None:
            options.rest()
            continue
        elif next_move_d == None:
            next_move = next_move_m
        else:
            next_move = next_move_d

        # if len(diamonds) == 0:
        #     next_move = search.get_moves_diamond(game_state.board, tuple(player.position), mineral_neighbours, game_state.get_my_home())
        # else:
        #     if player.backpack_capacity < 4:
        #         next_move = search.get_moves_diamond(game_state.board, tuple(player.position), diamonds_neighbours, game_state.get_my_home())
        #     else:
        #         next_move = search.get_moves_diamond(game_state.board, tuple(player.position), mineral_neighbours, game_state.get_my_home())
        
        # if next_move is None:
        #     next_move = search.get_moves_diamond(game_state.board, tuple(player.position), mineral_neighbours, game_state.get_my_home())

        # if next_move is None:
        #     options.rest()
        #     continue
        
        next_move = next_move[1]
        if player.daze_turns > 0:
            next_move = (2 * player.position[0] - next_move[0], 2 * player.position[1] - next_move[1])
        options.move(next_move[0], next_move[1])
