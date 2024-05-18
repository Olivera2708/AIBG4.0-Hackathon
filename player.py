class Player():
    def __init__(self, name, energy, xp, coins, position, increased_backpack_duration, daze_turns, frozen_turns, backpack_capacity, raw_minerals, processed_minerals, raw_diamonds, processed_diamonds):
        self.name = name
        self.energy = energy
        self.xp = xp
        self.coins = coins
        self.position = position
        self.increased_backpack_duration = increased_backpack_duration
        self.daze_turns = daze_turns
        self.frozen_turns = frozen_turns
        self.backpack_capacity = backpack_capacity
        self.raw_minerals = raw_minerals
        self.processed_minerals = processed_minerals
        self.raw_diamonds = raw_diamonds
        self.processed_diamonds = processed_diamonds

    @classmethod
    def from_json(cls, json_data):
        return cls(
            name=json_data["name"],
            energy=json_data["energy"],
            xp=json_data["xp"],
            coins=json_data["coins"],
            position=json_data["position"],
            increased_backpack_duration=json_data["increased_backpack_duration"],
            daze_turns=json_data["daze_turns"],
            frozen_turns=json_data["frozen_turns"],
            backpack_capacity=json_data["backpack_capacity"],
            raw_minerals=json_data["raw_minerals"],
            processed_minerals=json_data["processed_minerals"],
            raw_diamonds=json_data["raw_diamonds"],
            processed_diamonds=json_data["processed_diamonds"]
        )