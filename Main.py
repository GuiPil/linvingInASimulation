from Birb import *
from Env import *

count = 1
birb_list = []

enviro = Grid(6, 6)
enviro.build_grid()

for x in range(3):
    birb = Birb()
    birb_list.append(birb)

initial_drop(birb_list, enviro)

# for x in birb_list:
#     print(x.position.id)
#
# # for x in enviro.parcels.values():
#     print("Neighbour of parcel {} is {}".format(x.id, to_id(x.next_to)))


# main loop

for x in range(10):
    for birb in birb_list:
        birb.move()
        print("Birb {} is on the parcel number {}".format(birb.id, birb.position.id))


