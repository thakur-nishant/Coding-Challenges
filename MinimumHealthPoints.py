# Dungeons and Dragon


def minHealth(dungeon):
    # Write your code here
    min_hp = curr_hp = 0
    anchor = 0
    while anchor < len(dungeon):
        if dungeon[anchor] + curr_hp < 0:
            min_hp += 1 - (dungeon[anchor] + curr_hp)
            curr_hp = 1
        else:
            curr_hp += dungeon[anchor]
        anchor += 1

    return min_hp
