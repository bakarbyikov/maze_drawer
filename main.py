from collections import deque
from random import choices, randrange, sample
from typing import List, Tuple
import numpy as np

from misc import symbols, Ways, bin_ways
        

class Cell:
    
    def __init__(self, open_to: List[Ways] = []) -> None:
        self.open_to = bin_ways()
        self.open_to.add(sum([i.value for i in open_to])%16)
        self.frozen = bin_ways()

    def freeze(self, way: Ways) -> None:
        self.frozen.add(way.value)
    def unfreeze(self, way: Ways) -> None:
        self.frozen.remove(way.value)

    def open(self, way: Ways) -> bool:
        pretendents = way.value and ~self.frozen
        if pretendents:
            self.open_to.add(pretendents)
            return True
        return False
    def close(self, way: Ways) -> bool:
        pretendents = way.value and ~self.frozen
        if pretendents:
            self.open_to.remove(pretendents)
            return True
        return False

    def collapse(self) -> Tuple[bool, bool]:
        to_open = list()
        for w in (Ways.EAST, Ways.SOUTH):
            to_open.append(randrange(4) == 0)
            if to_open[-1]:
                self.open(w)
        
        return tuple(to_open)

    def __str__(self) -> str:
        return symbols[self.open_to.value]


class Grid:

    def __init__(self, width: int, height: int) -> None:
        self.width, self.height = width, height
        self.field = [[Cell() for x in range(width)] for i in range(height)]
        self.create_exits()
        self.freeze_borders()
        self.generate()
    
    def create_exits(self):
        self.field[0][0].open(Ways.NORTH)
        self.field[-1][-1].open(Ways.SOUTH)
    
    def freeze_borders(self):
        for y, row in enumerate(self.field):
            for x, c in enumerate(row):
                if x == self.width-1:
                    c.freeze(Ways.EAST)
                if y == 0:
                    c.freeze(Ways.NORTH)
                if x == 0:
                    c.freeze(Ways.WEST)
                if y == self.height-1:
                    c.freeze(Ways.SOUTH)
    
    def generate(self):
        for diag in range(self.width+self.height-1):
            for x in range(max(diag-self.height+1, 0), min(diag+1, self.width)):
                y = diag - x
                open_right, open_bottom = self.field[y][x].collapse()

                if x+1 < self.width:
                    right = self.field[y][x+1]
                    if open_right:
                        right.open(Ways.WEST)
                    right.freeze(Ways.WEST)

                if y+1 < self.height:
                    bottom = self.field[y+1][x]
                    if open_bottom:
                        bottom.open(Ways.NORTH)
                    bottom.freeze(Ways.NORTH)

    
    def freeze_map(self) -> str:
        return '\n'.join(''.join([symbols[c.frozen.value] for c in row]) for row in self.field)
    
    def __str__(self) -> str:
        return '\n'.join(''.join(map(str, row)) for row in self.field)
    

def test():
    g = Grid(10, 10)
    # print(g.freeze_map())
    print()
    print(g)

if __name__ == '__main__':
    test()
