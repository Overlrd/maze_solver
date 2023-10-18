import sys
import argparse

from maze import Maze, Node, StackFrontier, QueueFrontier, PriorityFrontier
from solvers import uninformed_solver, greedy_bfs


parser = argparse.ArgumentParser()
parser.add_argument("algorithm", help="[dfs, bfs, qbfs]")
parser.add_argument("maze_file", help="txt file of the maze including a start point A and target B",
                    default="maze.txt")
args = parser.parse_args()

algorithm = args.algorithm
maze_file = args.maze_file

algorithm_args = []
algorithm_args.append(Node)
solver = None
if algorithm == "dfs":
    solver = uninformed_solver
    algorithm_args.append(StackFrontier)
elif algorithm == "bfs":
    solver = uninformed_solver
    algorithm_args.append(QueueFrontier)
elif algorithm == "gbfs":
    solver = greedy_bfs
    algorithm_args.append(PriorityFrontier)


m = Maze(maze_file)
print("Maze:")
m.print()

print("Solving...")
m.solve(solver, *algorithm_args)

print("States Explored:", m.num_explored)
print("Solution:")
m.print()
m.output_image("maze.png", show_explored=True)
