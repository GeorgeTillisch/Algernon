#!/usr/bin/env python3
import sys
import re

from solver import Solver, SOLVE_TYPES, MAZE_TYPES


def main():
    if len(sys.argv) == 1:
        print("Usage: algernon width height mazetype solvetypes [bmp/svg/gif]")
        print("Defaults to PNG output")
        print("Mazetypes: perfect, braid, diagonal, prim, sidewinder, spiral")
        print("Solvetypes: bfs (breadth first search), gbfs (greedy bfs), astar. Combine with + to compare.")
        sys.exit()
    elif len(sys.argv) < 5:
        print(
            'Insufficient arguments.'
        )
        sys.exit(1)
    else:
        # Get width and height
        try:
            maze_rows = int(sys.argv[1])
            maze_cols = int(sys.argv[2])
        except ValueError:
            print('Invalid argument, width/height must be ints')
            sys.exit(1)

        # Get mazetype and check it's valid
        mazetype = sys.argv[3]
        if mazetype.lower() not in MAZE_TYPES.keys():
            print('Invalid argument:' + mazetype)
            sys.exit(1)

        # Get solvetypes and check that they're valid
        solvetypes_arg = sys.argv[4]
        if '+' in solvetypes_arg:
            solvetypes = solvetypes_arg.split('+')
        else:
            solvetypes = [solvetypes_arg]
        for s in solvetypes:
            if s.lower() not in SOLVE_TYPES.keys():
                print('Invalid argument:' + s)
                sys.exit(1)
        
        # Get output
        output='png'
        if 'bmp' in sys.argv:
            output = 'png'
        elif 'svg' in sys.argv:
            output = 'svg'
        elif 'gif' in sys.argv:
            output = 'gif'

        s = Solver(maze_rows, maze_cols, mazetype, output, solvetypes)
        s.solve()
             
        sys.exit()


if __name__ == '__main__':
    main()
