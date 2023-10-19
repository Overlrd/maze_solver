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

def manhattan_distance(state, goal):
    return abs(state[0] - goal[0]) + abs(state[1] - goal[1])

def uninformed_search(Maze, Node, Frontier):
    """
    Uninformed search algorithms, also known as blind search, do not utilize any domain-specific knowledge for their search strategy.
    
    This function can implement either a Depth-First Search (DFS) or a Breadth-First Search (BFS) algorithm based on the type of Frontier provided:
    
    - If the Frontier is a StackFrontier (implementing a Last-In First-Out data structure), the function performs a DFS, which explores as deeply as possible along each branch of the search tree before backtracking.
    
    - If the Frontier is a QueueFrontier (representing the frontier as a queue, a First-In Last-Out data structure), the function performs a BFS, which explores all nodes at the current level before moving to the next level in the search tree.
    """
    # initialize a frontier containing the starting node 
    num_explored = 0
    start = Node(state=Maze.start, parent=None, action=None)
    frontier = Frontier()
    frontier.add(start)

    # initialize an empty explored set
    explored = set()

    # loop until the solution is found or there are no more nodes in the frontier
    while not frontier.empty():

        # pick a node from the frontier 
        node = frontier.remove()
        num_explored +=1

        # check if the current node is the goal state
        if node.state == Maze.goal:
            Maze.solution = reconstruct_node_history(node)
            Maze.explored = explored
            Maze.num_explored = num_explored
            return

        # if the current node is not the goal state , add it to the explored set
        explored.add(node.state)

        # explore the neighbors of the current node for valid nodes to explore next
        for action, state in Maze.neighbors(node.state):
            # make sure the state is not already present in the frontier nor in the explored set
            if not frontier.contains_state(state) and state not in explored:
                # generate a child node and push it into the frontier
                child = Node(state=state, parent=node, action=action)
                frontier.add(child)


def informed_search(Maze, Node, Frontier, frontier_sort_key):
    """
    Informed search algorithms use problem-specific knowledge to find the solution more efficiently.

    This function can implement Greedy Best First Search (GBFS) and A* algorithms based on the `frontier_sort_key`. 
    The `frontier_sort_key` can be one of the following:
    
    - For Greedy Best-First Search (GBFS): 
      `frontier_sort_key = lambda x: x.h_cost`
      (where `x.h_cost` is the heuristic cost)

    - For A* Search: 
      `frontier_sort_key = lambda x: x.h_cost + x.g_cost`
      (where `x.h_cost` is the heuristic cost and `x.g_cost` is the actual cost from the start)
    """
    # initialize a frontier containing the starting node 
    num_explored = 0
    start = Node(state=Maze.start, parent=None, action=Node, h_cost= manhattan_distance(Maze.start, Maze.goal), g_cost= 0)
    frontier = Frontier()
    frontier.add(start)

    # initialize an empty explored set
    explored = set()

    # loop until the solution is found or there are no more nodes in the frontier
    while not frontier.empty():

        # pick a node from the frontier based on the 'frontier_sort_key' function
        node = frontier.remove(frontier_sort_key)
        print(f"Picked node {node.g_cost=} {node.h_cost=} : {node.g_cost + node.h_cost} ")
        num_explored +=1

        # check if the current node is the goal state
        if node.state == Maze.goal:
            Maze.solution = reconstruct_node_history(node)
            Maze.explored = explored
            Maze.num_explored = num_explored
            return

        # if the current node is not the goal state , add it to the explored set
        explored.add(node.state)

        # explore the neighbors of the current node for valid nodes to explore next
        for action, state in Maze.neighbors(node.state):
            # make sure the state is not already in the explored set
            if state not in explored:
                # compute the h_cost of the current state using manhattan distance 
                h_cost = manhattan_distance(state, Maze.goal)
                # generate a child node and push it into the frontier
                child = Node(state, parent=node, action=action, h_cost = h_cost,
                             g_cost = node.g_cost + 1)
                frontier.add(child)

    raise Exception("no solution ")
