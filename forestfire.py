import numpy as np
import random
import matplotlib.pyplot as plt
from matplotlib import animation
from matplotlib import colors

# Initial fraction of the forest occupied by trees

forest_fraction = 0.55

# Probability of new tree growth per empty cell, and of lightning strike.

(p, f) = (0.01, 0.001)

# Forest size (number of cells in x and y directions).

(nx, ny) = (100, 100)

# Displacements from a cell to its eight nearest neighbours

neighbourhood = (
    (-1, -1),
    (-1, 0),
    (-1, 1),
    (0, -1),
    (0, 1),
    (1, -1),
    (1, 0),
    (1, 1),
)
(space, tree, fire) = (0, 1, 2)

# Colours for visualization: brown for space, dark green for tree and orange
# for fire.
#colors_list = [(0.2, 0, 0), (0, 0.5, 0), (1, 0, 0)]
colors_list = ['k', '#26A910', 'r']


c_map = colors.ListedColormap(colors_list)


# Iterating the forest according to the forest-fire model rules

def make_new_grid(old_grid):

    # The boundary of the forest is always empty, so consider cells
    # indexed from 1 to nx-2, 1 to ny-2

    newgrid = np.zeros((nx, ny))  # creates the new grid
    for x in range(1, nx - 1):
        for y in range(1, ny - 1):                       # condition 1
            if old_grid[x, y] == fire:
                newgrid[x, y] = space
            elif old_grid[x, y] == space:                # condition 4
                if random.random() <= p:
                    newgrid[x, y] = tree
                else:
                    newgrid[x, y] = space
            elif old_grid[x, y] == tree:
                newgrid[x, y] = tree
                if random.random() <= f:                 # condition 3
                    newgrid[x, y] = fire
                for (dx, dy) in neighbourhood:           # condition 2
                    if old_grid[x + dx, y + dy] == fire:
                        newgrid[x, y] = fire
    return newgrid


# Initialize the first forest grid. Begin with a grid of zeros
initial_grid = np.zeros((nx, ny))

# fill the grid with random integers between 0 and 1 such that
# it is populated with trees with a probability of 0.55 per cell.
for x in range(1, nx - 1):
    for y in range(1, ny - 1):
        if (random.random() <= forest_fraction):
            initial_grid[x, y] = tree
        else:
            initial_grid[x, y] = space

# generate a empty canvas
fig = plt.figure(figsize=(5.0, 5.0))
ax = fig.add_subplot(111)

# iterate the function 300 times and create an image for each iteration
grids = [initial_grid]
ims = []
for i in range(300):
    grids.append(make_new_grid(grids[-1]))
for g in grids:
    ims.append((ax.pcolormesh(g, cmap=c_map, vmin=0, vmax=c_map.N, edgecolors = 'w'), ))
# edgecolors = 'b', alpha = 1.0


# Interval between frames (ms).
interval = 190

# Animate the list of images over an interval of 40ms
anim = animation.ArtistAnimation(fig, ims, interval, repeat=False)
plt.show()

# The writer will write the video to a file
# This is where properties of the video should be (fps, bitrate, codec ...etc)
writervideo = animation.FFMpegWriter(fps=5, bitrate=-1)

# You have to include this to tell python where the ffmpeg path is:
plt.rcParams['animation.ffmpeg_path'] = r'C:\\Users\\unive\\Downloads\\Programs\\ffmpeg-4.3.1-win64-static\\bin\\ffmpeg.exe'

anim.save('forestfire2.mp4', writer=writervideo)
