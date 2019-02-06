import sys

from solver import Solver


def main():
    if len(sys.argv) == 1:
        print(
            """Usage: algernon maze_rows, maze_cols, [gif]"""
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
        s.solve()
        s.save_state()
        
        sys.exit()


if __name__ == '__main__':
    main()
