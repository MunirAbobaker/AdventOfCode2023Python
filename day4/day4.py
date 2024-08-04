import regex

class Day4Part1:
    def __init__(self, filename):
        self.data = {}
        self._load_data(filename)

    def _load_data(self, filename):
        self.data = {}
        with open(filename) as f:
            for line in f:
                card, numbers = line.strip().split(':')
                numbers = numbers.strip().split('|')
                numbers1 = regex.findall(r'\d+', numbers[0])
                numbers2 = regex.findall(r'\d+', numbers[1])
                x = set(numbers1)
                y = set(numbers2)
                self.data[card.replace(' ', '')] = [x, y]
    def calculate_scratchcards_worth(self):
        scratchcards_worth = 0.0
        for _, numbers in self.data.items():
            x = numbers[0]
            y = numbers[1]
            if len(x.intersection(y)) > 0:
                scratchcards_worth += 2**(len(x.intersection(y))-1)
        return scratchcards_worth
    
    def get_solution(self):
        return self.calculate_scratchcards_worth()
    


if __name__ == '__main__':
    day4 = Day4Part1('input.txt')
    print(day4.get_solution())
    