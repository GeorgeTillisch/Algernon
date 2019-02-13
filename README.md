<img src="imgs\logo\algernon_l_t.svg">

## A program for visualising graph search algorithms (and solving mazes).

![](imgs/_unsolved.png)  |  ![](imgs/_solved.png)
:-------------------------:|:-------------------------:

# Search comparison:

BFS | Greedy BFS | A*
:-------------------------:|:-------------------------:|:-------------------------:
![](imgs/_bfs.gif) | ![](imgs/_gbfs.gif) | ![](imgs/_astar.gif)

Since A* is not highly optimized, greedy bfs often performs as well as A* on small mazes.

# Usage

```bash
algernon width height mazetype solvetypes [bmp/svg/gif]
Defaults to PNG output.
Mazetypes: perfect, braid, diagonal, prim, sidewinder, spiral.
Solvetypes: bfs (breadth first search), gbfs (greedy bfs), astar. Combine with + to compare.

$ algernon 201 201 diagonal astar
$ algernon 501 1001 perfect bfs+gbfs+astar gif
```

![](imgs/_maze_diagonal_astar_s.png) | ![](imgs/_maze_perfect_astar_s.png) | ![](imgs/_maze_braid_astar_s.png)
:-------------------------:|:-------------------------:|:-------------------------:
![](imgs/_maze_sidewinder_astar_s.png) | ![](imgs/_maze_spiral_astar_s.png) | ![](imgs/_maze_prim_astar_s.png)
