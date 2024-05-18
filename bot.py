import sys
import time
import json
import options
from game_state import GameState

while True:
    line = sys.stdin.readline().strip()
    data = json.loads(line)

    game_state = GameState.from_json(data)
    x, y = game_state.player1.position

    options.move(x, y+1)

    # print("rest", flush=True)

