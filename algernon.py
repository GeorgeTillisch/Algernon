#!/usr/bin/env python3
import sys

from solver import Solver


def main():
    if len(sys.argv) == 1:
        print(
            """Usage: algernon width height [bmp]"""
        )
        sys.exit()
    elif len(sys.argv) < 3:
        print(
            'Insufficient arguments.'
        )
        sys.exit()
    else:
        maze_rows = int(sys.argv[1])
        maze_cols = int(sys.argv[2])

        s = Solver(maze_rows, maze_cols)
        s.save_state()
        s.save_state(output='svg')
        s.solve()
        s.save_state()
        s.save_state(output='svg')
        
        sys.exit()


if __name__ == '__main__':
    main()
