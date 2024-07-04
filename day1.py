import math

class SolutionPart1:
    def __init__(self) -> None:
        self.data = self.load_data()

    def load_data(self, filename:str = "./data/day1-2.txt") -> list:
        with open("./data/day1-2.txt") as f:
            lines = f.readlines()
            lines = [x.strip() for x in lines]
            print(f"Data loaded from {filename}, {len(lines)} lines found.")
            return lines
        
    def find_first_last_digit(self, s: str) -> int:
        first = next((char for char in s if char.isdigit()), 0)
        last = next((char for char in reversed(s) if char.isdigit()), 0)
        return int(first + last)
    
    def csum(self) -> int:
        return sum([self.find_first_last_digit(x) for x in self.data])
    
class SolutionPart2:

    words_to_numbers = {
    "one":1 , "two":2 , "three":3 , "four":4, "five":5, "six":6, "seven":7, "eight":8, "nine":9
    }

    def __init__(self) -> None:
        self.data = self.load_data()

    def load_data(self, filename:str = "./data/day1.txt") -> list:
        with open("./data/day1-2.txt") as f:
            lines = f.readlines()
            lines = [x.strip() for x in lines]
            print(f"Data loaded from {filename}, {len(lines)} lines found.")
            return lines
        
    def find_all_occurrences(self, s, sub):
        start = 0
        indices = []
        while True:
            index = s.find(sub, start)
            if index == -1:
                break
            indices.append(index)
            start = index + 1
        return indices
    
    def find_min_max_occurrence(self, line, k):
        all_occurances = self.find_all_occurrences(self, line, k)
        return min(all_occurances), max(all_occurances)

    def find_lower_upper(self, line, k, lower, upper, numbers):
        min_occurance, max_occurance = self.find_min_max_occurrence(self, line, k)
        if min_occurance < lower:
            lower = min_occurance
            numbers[0] = k
        if max_occurance > upper:
            upper = max_occurance
            numbers[1] = k
        return numbers, lower, upper
    
    def find_least_most_occurance(self, line):
        lower = math.inf
        upper = - math.inf
        numbers = ['', '']
        for k, v in self.words_to_numbers.items():
            if k in line:
                numbers, lower, upper = self.find_lower_upper(self, line, k, lower, upper, numbers)
            if str(v) in line:
                numbers, lower, upper = self.find_lower_upper(self, line, str(v), lower, upper, numbers)
        numbers = [str(x) if x.isdigit() else str(self.words_to_numbers[x]) for x in numbers]
        return int(numbers[0] + numbers[1])
    
    def csum(self):
        return sum([self.find_least_most_occurance(x) for x in self.data])
    

if __name__ == "__main__":
    s = SolutionPart1()
    print("Solution to day 1 is", s.csum())
        
    
    
        