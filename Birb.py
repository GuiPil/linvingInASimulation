class Birb:
    birb_id= 0
    id = 0

    def __init__(self):
        self.id = Birb.birb_id
        Birb.birb_id += 1

