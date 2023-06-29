h, w = map(int, input().split())
grid = []

feux = []
bhs = []

NotOut = True

for i in range(h):
    grid.append(list(input()))

    # get @
    if 'J' in grid[i]:
        if i == 0 or i == h - 1 or grid[i].index('J') == 0 or grid[i].index('J') == w - 1:
            print(1)
            NotOut = False
            break
        bhs.append((i, grid[i].index('J')))
    # get *
    if 'F' in grid[i]:
        for j in range(w):
            if grid[i][j] == 'F':
                feux.append((i, j))

i = 0

while NotOut:

    if len(bhs) == 0:
        print("IMPOSSIBLE")
        break

    new_feux = []
    for feu in feux:

        if feu[0] < h - 1:
            if grid[feu[0] + 1][feu[1]] != '#' and grid[feu[0] + 1][feu[1]] != 'F':
                grid[feu[0] + 1][feu[1]] = 'F'
                new_feux.append((feu[0] + 1, feu[1]))
        if feu[0] > 0:
            if grid[feu[0] - 1][feu[1]] != '#' and grid[feu[0] - 1][feu[1]] != 'F':
                grid[feu[0] - 1][feu[1]] = 'F'
                new_feux.append((feu[0] - 1, feu[1]))

        if feu[1] < w - 1:
            if grid[feu[0]][feu[1] + 1] != '#' and grid[feu[0]][feu[1] + 1] != 'F':
                grid[feu[0]][feu[1] + 1] = 'F'
                new_feux.append((feu[0], feu[1] + 1))

        if feu[1] > 0:
            if grid[feu[0]][feu[1] - 1] != '#' and grid[feu[0]][feu[1] - 1] != 'F':
                grid[feu[0]][feu[1] - 1] = 'F'
                new_feux.append((feu[0], feu[1] - 1))

    feux = new_feux  # /!\ new_feux

    new_bhs = []
    for bh in bhs:

        if grid[bh[0] + 1][bh[1]] == '.':
            if bh[0] + 1 == h - 1:
                print(i + 2)
                NotOut = False
                break
            grid[bh[0] + 1][bh[1]] = 'J'
            new_bhs.append((bh[0] + 1, bh[1]))

        if grid[bh[0] - 1][bh[1]] == '.':
            if bh[0] - 1 == 0:
                print(i + 2)
                NotOut = False
                break
            grid[bh[0] - 1][bh[1]] = 'J'
            new_bhs.append((bh[0] - 1, bh[1]))

        if grid[bh[0]][bh[1] + 1] == '.':
            if bh[1] + 1 == w - 1:
                print(i + 2)
                NotOut = False
                break
            grid[bh[0]][bh[1] + 1] = 'J'
            new_bhs.append((bh[0], bh[1] + 1))

        if grid[bh[0]][bh[1] - 1] == '.':
            if bh[1] - 1 == 0:
                print(i + 2)
                NotOut = False
                break
            grid[bh[0]][bh[1] - 1] = 'J'
            new_bhs.append((bh[0], bh[1] - 1))

    bhs = new_bhs

    i += 1
