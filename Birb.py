from Env import *
from numpy import random as rd

class Birb:
    birb_id = 0

    def __init__(self):
        self.id = Birb.birb_id
        Birb.birb_id += 1
        self.position = Parcel
        self.past_position = Parcel


def initial_drop(birbs, grid):

    for x in birbs :
        x.position = rd.randint(1, len(grid.parcels))
