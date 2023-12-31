import argparse

from maze import Maze, Node, StackFrontier, QueueFrontier, CostFrontier
from solvers import informed_search, uninformed_search

ALGORITHMS = {
    "dfs": (uninformed_search, StackFrontier),
    "bfs": (uninformed_search, QueueFrontier),
    "gbfs": (informed_search, CostFrontier, lambda x: x.h_cost),
    "a_star": (informed_search, CostFrontier, lambda x: x.h_cost + x.g_cost),
}

def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("algorithm", help="[dfs, bfs, gbfs, a_star ]")
    parser.add_argument("maze_file", help="txt file of the maze including a start point A and target B",
                        default="maze.txt")
    parser.add_argument("--output_file", "-o", help="output image of the solved maze", default="maze.png")
    args = parser.parse_args()
    return args.algorithm, args.maze_file, args.output_file

def main():
    algorithm, maze_file, output_file = parse_arguments()

    if algorithm not in ALGORITHMS:
        print("Invalid algorithm. Please choose from: dfs, bfs, gbfs, a_star")
        return

    solver, *algorithm_args = ALGORITHMS[algorithm]

    m = Maze(maze_file)
    print("Maze:")
    m.print()

    print("Solving...")
    m.solve(solver, Node, *algorithm_args)

    print("States Explored:", m.num_explored)
    print("Solution:")
    m.print()
    m.output_image(output_file, show_explored=True)

if __name__ == "__main__":
    main()
