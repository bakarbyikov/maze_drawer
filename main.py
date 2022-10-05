from enum import Enum
from random import choices, randrange, sample
from typing import List
import numpy as np

from misc import symbols, Ways, bin_ways
        

class Cell:
    
    def __init__(self, open_to: List[Ways]) -> None:
        self.open_to = bin_ways()
        self.open_to.add(sum([i.value for i in open_to])%16)
        self.frozen = bin_ways()

    def freeze(self, way: Ways) -> None:
        self.frozen.add(way.value)
    def unfreeze(self, way: Ways) -> None:
        self.frozen.remove(way.value)

    def open(self, way: Ways) -> None:
        self.open_to.add(way.value)
    def close(self, way: Ways) -> None:
        self.open_to.remove(way.value)
    
    def __str__(self) -> str:
        return symbols[self.open_to.value]


class Grid:

    def __init__(self, width: int, height: int) -> None:
        self.size = width, height
        self.field = np.full((width, height), Cell)
        self.freeze_borders()
    
    def freeze_borders(self):
        for w, pos in zip(Ways, (":,-1")):
            for c in self.field[pos]:
                c.freeze(w)

def test():
    w, h = 10, 10
    grid = [[Cell(sample(list(Ways), randrange(5))) for __ in range(w)] for _ in range(h)]
    string = '\n'.join('─'.join(map(str, row)) for row in grid)
    print(string)

if __name__ == '__main__':
    test()
    c = Cell()
    for w in Ways:
        c.open(w)
        print(f"{c.open_to.value :b}")

    c.close(Ways.NORTH)
    print(f"{c.open_to.value :b}")

    # test()
