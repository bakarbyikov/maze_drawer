from random import random, randrange
from typing import List, Tuple

from misc import Ways, bin_ways, symbols
from settings import opened_chance


class Cell:
    
    def __init__(self, open_to: List[Ways] = []) -> None:
        self.open_to = bin_ways()
        self.open_to.add(sum([i.value for i in open_to])%16)
        self.frozen = bin_ways()

    def freeze(self, way: Ways) -> None:
        self.frozen.add(way.value)
    def unfreeze(self, way: Ways) -> None:
        self.frozen.remove(way.value)
    def freeze_all(self) -> None:
        self.frozen.add(0b1111)

    def open(self, way: Ways) -> bool:
        pretendents = way.value & ~self.frozen
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
        for i, w in enumerate((Ways.EAST, Ways.SOUTH)):
            to_open.append(random() < opened_chance)
            if to_open[-1]:
                self.open(w)
        self.freeze_all()
        
        return tuple(to_open)

    def __str__(self) -> str:
        return symbols[self.open_to.value]
