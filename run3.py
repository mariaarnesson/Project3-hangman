from itertools import zip_longest

ships = ['Carrier','Battleship','Destroyer']
sizes = ['5','4','2']

for ships, sizes in zip_longest(ships,sizes):
    print(ships, sizes)


