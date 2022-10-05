from enum import Enum

symbols = ['   ', ' ╶─', ' ╵ ', ' └─', '─╴ ', '───', '─┘ ', '─┴─', 
           ' ╷ ', ' ┌─', ' │ ', ' ├─', '─┐ ', '─┬─', '─┤ ', '─┼─']

class Ways(Enum):
    EAST  = 0b0001
    NORTH = 0b0010
    WEST  = 0b0100
    SOUTH = 0b1000

    
class bin_ways:
    @staticmethod
    def bin_inverse(num: int) -> int:
        return num ^ 15
    
    def __init__(self) -> None:
        self.value = 0
    
    def add(self, way: int) -> None:
        self.value |= way

    def remove(self, way: int) -> None:
        self.value &= self.bin_inverse(way)

    def __invert__(self) -> 'bin_ways':
        return self.bin_inverse(self.value)
    
    def __str__(self) -> str:
        return bin(self.value)

def test_symbols():
    for i in range(16):
        print(f"{i:4b}:\t{symbols[i]}")

if __name__ == '__main__':
    test_symbols()