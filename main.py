from enum import Enum
from random import randrange

class Ways(Enum):
    EAST = 0b0000
    NORTH = 0b0010
    WEST = 0b0100
    SOUTH = 0b1000


class Cell:
    symbols = {
        0b0000: ' ',
        0b0001: '╶',
        0b0010: '╵',
        0b0011: '└',
        0b0100: '╷',
        0b0101: '─',
        0b0110: '┘',
        0b0111: '┴',
        0b1000: '╴',
        0b1001: '┌',
        0b1010: '│',
        0b1011: '├',
        0b1100: '┐',
        0b1101: '┬',
        0b1110: '┤',
        0b1111: '┼',
    }
    
    def __init__(self, open_to: Ways) -> None:
        self.open_to = open_to
    
    def __str__(self) -> str:
        return self.symbols[self.open_to]


class Grid:

    def __init__(self, width: int, height: int) -> None:
        self.size = width, height
        pass

def test():
    w, h = 10, 10
    grid = [[Cell(randrange(16)) for __ in range(w)] for _ in range(h)]
    string = '\n'.join('─'.join(map(str, row)) for row in grid)
    print(string)

if __name__ == '__main__':
    test()
    for i, s in Cell.symbols.items():
        print(f"{i}:'{s}'\t{ord(s)}'")
