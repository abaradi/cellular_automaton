# Forest Fire Model

A python script that simulates the behaviour of a cellular automaton. A cellular automaton is an autonomous system consisting of a group of cells occupying a grid lattice with finite dimensions. Each cell has a state and a neighborhoud of cells that surround it. The number of state possibilities is typically finite and the state evolves according to a set of rules. The rules are microscopic in nature but the system often develops macroscopic behaviors and patterns which makes it resemble realistic behavior in realistic systems. For this project, we aim to model the destruction by fire, and the regeneration of a forest. The cells which represent the forest cycle between three possible states. A cell could be a tree, a burning tree, or an empty space. 

# Rules
The forest cellular automaton evolves according to the following set of rules which are executed simultaneously for every cell at a given iteration: 

### Rule 1
A burning cell turns into an empty cell:
![Condition 1](/images/Condition%201.png)

### Rule 2
A tree will burn if at least one neighbor is burning:
![Condition 2](/images/Condition%202.png)

### Rule 3
A tree ignites with probability f even if no neighbor is burning:
![Condition 3](/images/Condition%203.png)

### Rule 4
An empty space fills with a tree with probability p:
![Condition 4](/images/Condition%204.png)

# Animation
The probability values are adjustable on line 13 of the python script. The evolution of 40,000 cells on a 200 x 200 grid is shown in the following gif:
![HQ](/gifs/ForestFire40kCells.gif)

The behaviour is also displayed on a 20 x 20 grid where it's easier to track the evolution of individual cells: 
![LQ](/gifs/ForestFire400Cells.gif)