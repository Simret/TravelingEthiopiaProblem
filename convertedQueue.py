from collections import deque

# Define Node class
class Node:
    def __init__(self, state, parent=None, action=None, path_cost=0):
        self.state = state
        self.parent = parent
        self.action = action
        self.path_cost = path_cost

    def __repr__(self):
        return f"Node(state={self.state}, action={self.action}, cost={self.path_cost})"

# Breadth-First Search Algorithm
def breadth_first_search(problem):
    node = Node(problem.initial)
    if problem.is_goal(node.state):
        return node

    frontier = deque([node])  # FIFO Queue for frontier
    reached = {node.state}    # Set to store reached states

    while frontier:
        node = frontier.popleft()  # Pop from front of the queue

        for child in problem.expand(node):
            s = child.state
            if problem.is_goal(s):
                return child
            if s not in reached:
                reached.add(s)
                frontier.append(child)

    return None  # Failure


# Depth-First Search Algorithm
def depth_first_search(problem):
    node = Node(problem.initial)
    if problem.is_goal(node.state):
        return node

    frontier = [node]  # Stack for frontier
    reached = {node.state}  # Set to store reached states

    while frontier:
        node = frontier.pop()  # Pop from the stack

        for child in problem.expand(node):
            s = child.state
            if problem.is_goal(s):
                return child
            if s not in reached:
                reached.add(s)
                frontier.append(child)

    return None  # Failure


# Define Problem
class TravelingEtProblem:
    def __init__(self, initial_state):
        self.initial = initial_state
        self.goal = 'Gondar'  # Example goal city

        # Define Ethiopia map (cities and their neighbors)
        self.graph = {
            'Metema': ['Gondar', 'Azezo'],
            'Gondar': ['Azezo', 'Metema', 'Debarke'],
            'BahirDar': ['Azezo','DebreTabor', 'Metekel','Injibara','FinoteSelam'],
            'Lalibela': ['Woldia', 'Sekota', 'DebreTabor']
        }

    def is_goal(self, state):
        return state == self.goal

    def expand(self, node):
        # Expands the node and returns a list of child nodes
        children = []
        for neighbor in self.graph.get(node.state, []):
            children.append(Node(neighbor, parent=node, action=f"Move to {neighbor}", path_cost=node.path_cost + 1))
        return children


# Testing the search algorithms
if __name__ == '__main__':
    initial_state = 'Metema'
    problem = TravelingEtProblem(initial_state)

    print("Testing Breadth-First Search:")
    solution_bfs = breadth_first_search(problem)
    if solution_bfs:
        path = []
        node = solution_bfs
        while node:
            path.append(node.state)
            node = node.parent
        print("BFS Solution Path:", ' -> '.join(reversed(path)))
    else:
        print("BFS failed to find a solution.")

    print("\nTesting Depth-First Search:")
    solution_dfs = depth_first_search(problem)
    if solution_dfs:
        path = []
        node = solution_dfs
        while node:
            path.append(node.state)
            node = node.parent
        print("DFS Solution Path:", ' -> '.join(reversed(path)))
    else:
        print("DFS failed to find a solution.")



