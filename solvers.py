import math


def reconstruct_node_history(node):
    actions = []
    cells = []
    while node.parent is not None:
        actions.append(node.action)
        cells.append(node.state)
        node = node.parent
    actions.reverse()
    cells.reverse()
    return (actions, cells)

def manhattan_distance(node, goal):
    return abs(node.state[0] - goal[0]) + abs(node.state[1] - goal[1])

def uninformed_solver(Maze, Node, Frontier):
    "includes dfs and bfs, specified by the frontier"
    num_explored = 0
    start = Node(state=Maze.start, parent=None, action=None)
    frontier = Frontier()
    frontier.add(start)

    # initialize an empty explored set
    explored = set()

    # loop until the solution is found
    while not frontier.empty():

        # pick a node from the frontier 
        node = frontier.remove()
        num_explored +=1

        if node.state == Maze.goal:
            Maze.solution = reconstruct_node_history(node)
            Maze.explored = explored
            Maze.num_explored = num_explored
            return

        explored.add(node.state)

        for action, state in Maze.neighbors(node.state):
            if not frontier.contains_state(state) and state not in explored:
                child = Node(state=state, parent=node, action=action)
                frontier.add(child)


def greedy_bfs(Maze, Node, Frontier):
    num_explored = 0
    start = Node(state=Maze.start, parent=None, action=Node, priority=-math.inf)
    frontier = Frontier()
    frontier.add(start)

    explored = set()
    while not frontier.empty():
        # pick a node from the frontier 
        node = frontier.remove()
        num_explored +=1

        if node.state == Maze.goal:
            Maze.solution = reconstruct_node_history(node)
            Maze.explored = explored
            Maze.num_explored = num_explored
            return

        explored.add(node.state)

        for action, state in Maze.neighbors(node.state):
            if state not in explored:
                child = Node(state, parent=node, action=action)
                priority = manhattan_distance(child, Maze.goal)
                child.priority = priority
                frontier.add(child)

    raise Exception("no solution ")
