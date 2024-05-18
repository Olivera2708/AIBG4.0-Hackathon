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

    should_attack, move = evaluate.should_attack_house(game_state)
    if should_attack:
        options.move(move[0], move[1])
        continue

    player = evaluate.get_player("my", game_state)

    if tuple(player.position) in evaluate.get_next_to_opponent_home(game_state.get_opponent_home()):
        options.rest()
        continue

    if player.backpack_capacity > 0:
        if tuple(player.position) == game_state.get_my_home():
            if player.energy < 150 and (player.raw_diamonds > 0 or player.raw_minerals > 0):
                options.convert(0,0,player.raw_diamonds,player.raw_minerals,0,0)
            else:
                options.convert(0,0,0,0,player.raw_diamonds,player.raw_minerals)
            continue

        next_move = search.get_moves(game_state.board, tuple(player.position), game_state.get_my_home(), game_state.get_my_home())
        if next_move is None:
            options.rest()
            continue
        next_move = next_move[1]
        if player.daze_turns > 0:
            next_move[0], next_move[1] = next_move[1], next_move[0]
        options.move(next_move[0], next_move[1])
        pass
    else:
        neighbours = search.get_neigbour(player.position)
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
            next_move = search.get_moves_diamond(game_state.board, tuple(player.position), mineral_neighbours, game_state.get_my_home())
        else:
            next_move = search.get_moves_diamond(game_state.board, tuple(player.position), diamonds_neighbours, game_state.get_my_home())
        if next_move is None:
            next_move = search.get_moves_diamond(game_state.board, tuple(player.position), mineral_neighbours, game_state.get_my_home())

        if next_move is None:
            options.rest()
            continue
        next_move = next_move[1]
        if player.daze_turns > 0:
            next_move[0], next_move[1] = next_move[1], next_move[0]
        options.move(next_move[0], next_move[1])

