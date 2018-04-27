# https://www.careercup.com/question?id=4593205218639872

def is_land(island_map, row, col):
    return (0 <= row < len(island_map)
            and 0 <= col < len(island_map[0])
            and island_map[row][col] == '1')

def find_connected_land(island_map, row, col):
    queue = [(row, col)]
    while queue:
        row, col = queue.pop(0)
        island_map[row][col] = '0'
        for nextrow in (row-1, row, row+1):
            for nextcol in (col-1, col, col+1):
                if is_land(island_map, nextrow, nextcol):
                    queue.append((nextrow, nextcol))

def count_islands(island_map):
    ISLAND_COUNT = 0
    island_map = map(lambda x:list(x), island_map)

    for row in range(len(island_map)):
       for col in range(len(island_map[0])):
           if is_land(island_map, row, col):
               find_connected_land(island_map, row, col)
               ISLAND_COUNT += 1

    return ISLAND_COUNT
           

if __name__ == '__main__':
    MAP = [
           '01010',
           '01001',
           '01101',
          ]

    print count_islands(MAP)
