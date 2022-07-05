from Birb import Birb

birb_list = []

for x in range(5):
    birb = Birb()
    birb_list.append(birb)

for x in birb_list:
    print(x.id)
