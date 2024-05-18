import sys
import time
import json
import options
from game_state import GameState
import evaluate

while True:
    # line = sys.stdin.readline().strip()
    line = {
        "turn": 61,
        "firstPlayerTurn": True,
        "player1": {
            "name": "Vas bot",
            "energy": 552,
            "xp": 105,
            "coins": 125,
            "position": [1, 6],
            "increased_backpack_duration": 0,
            "daze_turns": 0,
            "frozen_turns": 0,
            "backpack_capacity": 0,
            "raw_minerals": 0,
            "processed_minerals": 0,
            "raw_diamonds": 0,
            "processed_diamonds": 0
        },
        "player2": {
            "name": "Topic Team",
            "energy": 571,
            "xp": 100,
            "coins": 125,
            "position": [2, 4],
            "increased_backpack_duration": 0,
            "daze_turns": 0,
            "frozen_turns": 0,
            "backpack_capacity": 0,
            "raw_minerals": 0,
            "processed_minerals": 0,
            "raw_diamonds": 0,
            "processed_diamonds": 0
        },
        "board": [
            ["E", "E", "E", "E", "E", "E", "D_2_0", "M_6_0", "E", "B"],
            ["E", "D_3_0", "M_6_0", "E", "E", "E", "1", "M_3_0", "E", "E"],
            ["E", "M_6_0", "E", "E", "2", "E", "E", "E", "E", "E"],
            ["E", "E", "E", "E", "E", "M_6_0", "E", "M_6_0", "E", "E"],
            ["E", "E", "E", "E", "E", "E", "M_6_0", "E", "M_6_0", "M_6_0"],
            ["E", "E", "E", "M_6_0", "E", "E", "E", "E", "E", "E"],
            ["D_3_0", "E", "E", "E", "M_6_0", "E", "E", "E", "E", "E"],
            ["M_6_0", "M_6_0", "M_6_0", "M_6_0", "E", "E", "E", "E", "E", "E"],
            ["E", "E", "E", "E", "M_6_0", "E", "E", "E", "E", "E"],
            ["A", "E", "E", "E", "E", "E", "E", "E", "E", "E"]
        ]
    }

    # data = json.loads(line)
    game_state = GameState.from_json(line)

    # print(evaluate.move_matrix((0,0), game_state.board))
    # break

    print("rest", flush=True)

