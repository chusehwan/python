#Great Magicians
def make_great(magicians):
    great_magicians=[]
    for magician in magicians:
        great_magician ='Great ' + magician
        great_magicians.append(great_magician)
    return great_magicians

def show_magicians(magicians):
    for magician in magicians:
        print(magician)

magicians=['magician_A','magician_B','magician_C','magician_D']

magicians = make_great(magicians)
show_magicians(magicians)