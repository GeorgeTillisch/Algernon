#!/usr/bin/env python3
import sys

from solver import Solver, SOLVE_TYPES


def main():
    if len(sys.argv) == 1:
        print(
            """Usage: algernon width height solvetype [svg/gif] \nDefaults to BMP output. \nSolvetype Options: bfs, astar"""
        )
        sys.exit()
    elif len(sys.argv) < 4:
        print(
            'Insufficient arguments.'
        )
        sys.exit(1)
    else:
        try:
            maze_rows = int(sys.argv[1])
            maze_cols = int(sys.argv[2])
        except ValueError:
            print('Invalid argument, width/height must be ints')
            sys.exit(1)

        solvetype = sys.argv[3]
        if solvetype.lower() not in SOLVE_TYPES.keys():
            print('Invalid argument:' + solvetype)
            sys.exit(1)
        
        output = 'bmp'
        if 'svg' in sys.argv:
            output = 'svg'
        elif 'gif' in sys.argv:
            output = 'gif'

        s = Solver(maze_rows, maze_cols, output, solvetype)
        
        if output != 'gif': # Gif doesn't require a 'before' image
            s.save_state()
        s.solve()
        s.save_state()        
        
        sys.exit()


if __name__ == '__main__':
    main()
