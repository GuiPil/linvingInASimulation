from enum import IntEnum
from operator import itemgetter


class Grid:

    def __init__(self, height, length):
        self.height = height
        self.length = length
        self.corners = []
        self.t_border = []
        self.b_border = []
        self.l_border = []
        self.r_border = []
        self.parcels = {}

    def build_grid(self):
        for x in range(self.height*self.length):
            parcel = Parcel()
            self.parcels.update({parcel.id: parcel})

        self.build_corner()
        self.build_border()

        for x in self.parcels.values():
            x.build_next(self)

    def build_corner(self):
        self.corners.append(1)
        self.corners.append(self.length)
        self.corners.append(1 + (self.length * (self.height - 1)))
        self.corners.append(self.height * self.length)

    def build_border(self):

        for x in range(1, self.length):
            if x not in {1, self.length}:
                self.t_border.append(x)

        for x in range(1, 1+(self.length * (self.height - 1)), self.length):
            if x not in {1, 1+(self.length * (self.height - 1))}:
                self.l_border.append(x)

        for x in range(self.length, self.length * self.height, self.length):
            if x not in {self.height, self.length}:
                self.r_border.append(x)

        for x in range(1+(self.length * (self.height - 1)), self.height * self.length):
            if x not in {1+(self.length * (self.height - 1)), self.height * self.length}:
                self.b_border.append(x)


class Parcel:

    p_id = 0

    def __init__(self):
        self.id = Parcel.p_id+1
        Parcel.p_id += 1
        self.next_to = []
        self.birb_on = []
    #function that build the list of neighbourg of each parcel

    def build_next(self, grid: Grid):

        # We manage the corner first, to what next to add
        bl_corner = 1+(grid.length * (grid.height - 1))
        br_corner = grid.height * grid.length

        if self.id in grid.corners:

            if self.id == 1:
                self.next_to.extend(itemgetter(self.id+1, self.id+grid.length)(grid.parcels))
            elif self.id == grid.length:
                self.next_to.extend(itemgetter(self.id-1, self.id+grid.length)(grid.parcels))
            elif self.id == bl_corner:
                self.next_to.extend(itemgetter(self.id+1, self.id-6)(grid.parcels))
            elif self.id == br_corner:
                self.next_to.extend((itemgetter(self.id-1, self.id-6)(grid.parcels)))

        # then the borders
        elif self.id in grid.t_border:
            self.next_to.extend(itemgetter(self.id-1, self.id+1, self.id+grid.length)(grid.parcels))

        elif self.id in grid.b_border:
            self.next_to.extend(itemgetter(self.id+1, self.id-1, self.id-grid.length)(grid.parcels))

        elif self.id in grid.l_border:
            self.next_to.extend(itemgetter(self.id+1, self.id-grid.length, self.id+grid.length)(grid.parcels))

        elif self.id in grid.r_border:
            self.next_to.extend(itemgetter(self.id-1, self.id-grid.length, self.id+grid.length)(grid.parcels))

        # finally the rest
        else:
            self.next_to.extend(itemgetter(self.id+1, self.id-1, self.id-grid.length, self.id+grid.length)(grid.parcels))


def to_id(par: Parcel):
    if len(par) >= 1:
        ids = []
        for p in par:
            ids.append(p.id)
        return ids
    else:
        return par.id

