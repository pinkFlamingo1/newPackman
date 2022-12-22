# @ -> Person
# G -> Ghost
# P -> Pills
# . -> Empty Spaces
# | and - -> Walls
from pacman import map


def validate_map(map):
    map_ok = True
    for row in map:
        if len(row) != 10:
            map_ok = False
            print(row)
    return map_ok


print(map)

print(validate_map(map))

# End of file
