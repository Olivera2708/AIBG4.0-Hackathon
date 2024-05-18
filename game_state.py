from player import Player

class GameState:
    def __init__(self, turn, first_player_turn, player1, player2, board):
        self.turn = turn
        self.first_player = first_player_turn
        self.player1 = player1
        self.player2 = player2
        self.board = board

    @classmethod
    def from_json(cls, json_data):
        player1 = Player.from_json(json_data["player1"])
        player2 = Player.from_json(json_data["player2"])
        return cls(
            turn=json_data["turn"],
            first_player_turn=json_data["firstPlayerTurn"],
            player1=player1,
            player2=player2,
            board=json_data["board"]
        )
    
    def get_my_home(self):
        if self.first_player:
            return (0, 9)
        else:
            return (9, 0)
        
    def get_opponent_home(self):
        if self.first_player:
            return (9, 0)
        else:
            return (0, 9)
    