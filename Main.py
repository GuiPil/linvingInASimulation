from Birb import *
from Env import *

count = 1
birb_list = []

enviro = Grid(6, 6)
enviro.build_grid()

for x in range(6):
    birb = Birb()
    birb_list.append(birb)

initial_drop(birb_list, enviro)

for x in birb_list:
    print("Birb [] is on the parcel number {}".format(x.id, x.position))
