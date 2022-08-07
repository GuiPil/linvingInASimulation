from Env import *
from numpy import random as rd


class Birb:
    birb_id = 0

    def __init__(self):
        self.position = None
        self.id = Birb.birb_id
        Birb.birb_id += 1
        self.past_position = []

    def move(self):
        actual_position = self.position
        next_move = rd.choice(actual_position.next_to)

        self.past_position.append(self.position)
        self.position = next_move


def initial_drop(birbs: Birb, grid: Grid):

    for x in birbs:
        x.position = rd.choice(list(grid.parcels.values()))
