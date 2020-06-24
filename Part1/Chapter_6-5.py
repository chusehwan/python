rivers = {
    'nation_A':'river_A',
    'nation_B': 'river_B',
    'nation_C': 'river_C',
    'nation_D': 'river_D',
    'nation_E': 'river_E',
    }

for nation, river in rivers.items():
    print(river + ' runs through '+ nation +'.')

for nation in rivers.keys():
    print(' runs through '+ nation +'.')

for nation in rivers.values():
    print(' runs through '+ nation +'.')