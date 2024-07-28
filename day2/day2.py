import enum
from typing import List, Dict, Tuple

class Day2Part1:
    class Color(enum.Enum):
        BLUE = "blue"
        GREEN = "green"
        RED = "red"

    def __init__(self, config: List[int], file_path: str):
        self.config = config
        self.games = self.load_games(file_path)

    def parse_color_value(self, value: str) -> Tuple[int, str]:
        amount, color = value.strip().split(' ')
        return int(amount), color

    def parse_game_values(self, values: str) -> List[List[int]]:
        game_sub_values = []
        for v in values.split(';'):
            blue, green, red = 0, 0, 0
            for amount, color in map(self.parse_color_value, v.split(',')):
                if color == Day2Part1.Color.BLUE.value:
                    blue = amount
                elif color == Day2Part1.Color.GREEN.value:
                    green = amount
                elif color == Day2Part1.Color.RED.value:
                    red = amount
            game_sub_values.append([blue, green, red])
        return game_sub_values

    def load_games(self, file_path: str) -> Dict[str, List[List[int]]]:
        with open(file_path) as f:
            lines = f.readlines()
        
        return {
            key: self.parse_game_values(values)
            for line in lines
            for key, values in [line.split(':')]
        }

    def get_number_valid_games(self) -> List[str]:
        return [
            key for key, game in self.games.items()
            if all(
                all(self.config[idx] >= int(color) for idx, color in enumerate(run))
                for run in game
            )
        ]

    def sum_valid_games(self) -> int:
        valid_games = self.get_number_valid_games()
        return sum(map(lambda valid_game: int(valid_game.split(' ')[1]), valid_games))
    
    def get_solution(self) -> int:
        return self.sum_valid_games()

if __name__ == "__main__":
    config = [14, 13, 12]
    day2part1 = Day2Part1(config, "../data/day2.txt")
    total_sum = day2part1.get_solution()
    print(f"Number of valid games: {total_sum}")