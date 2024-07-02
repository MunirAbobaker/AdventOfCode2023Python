class Solution:
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
        #print(first, last)
        return int(first + last)
    
    def csum(self) -> int:
        return sum([self.find_first_last_digit(x) for x in self.data])
    

if __name__ == "__main__":
    s = Solution()
    print("Solution to day 1 is", s.csum())
        
    
    
        