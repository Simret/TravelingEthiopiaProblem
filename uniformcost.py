import heapq

# Define Node class for UCS
class Node:
    def __init__(self, state, parent=None, action=None, path_cost=0):
        self.state = state
        self.parent = parent
        self.action = action
        self.path_cost = path_cost

    def __lt__(self, other):
        return self.path_cost < other.path_cost  # Priority queue uses this to order nodes by cost

    def __repr__(self):
        return f"Node(state={self.state}, cost={self.path_cost})"

# Uniform Cost Search Algorithm
def uniform_cost_search(problem, start_state, goal_state):
    initial_node = Node(start_state)
    frontier = []
    heapq.heappush(frontier, initial_node)  # Min-heap priority queue
    reached = {start_state: 0}  # Cost of reaching each state

    while frontier:
        node = heapq.heappop(frontier)

        if node.state == goal_state:
            return node  # Found the goal

        # Expand the node (look at neighbors)
        for child in problem.expand(node):
            if child.state not in reached or child.path_cost < reached[child.state]:
                reached[child.state] = child.path_cost
                heapq.heappush(frontier, child)

    return None  # If no solution found

# Define Ethiopia Problem
class EthiopiaProblem:
    def __init__(self, initial_state, goal_states):
        self.initial = initial_state
        self.goal_states = set(goal_states)  # Set of goal states (to visit all of them)
        
        # Define Ethiopia cities and their connections with costs (simplified example)
        self.graph = {
            'Addis Ababa': {'Axum': 39, 'Gondar': 41, 'Lalibela': 30, 'Babile': 25, 'Jimma': 19, 'Bale': 25, 'Sof Oumer': 48, 'Arba Minch': 25},
            'Axum': {'Addis Ababa': 39, 'Gondar': 13},
            'Gondar': {'Addis Ababa': 41, 'Axum': 13, 'Lalibela': 20},
            'Lalibela': {'Addis Ababa': 30, 'Gondar': 20},
            'Babile': {'Addis Ababa': 25},
            'Jimma': {'Addis Ababa': 19},
            'Bale': {'Addis Ababa': 25},
            'Sof Oumer': {'Addis Ababa': 48},
            'Arba Minch': {'Addis Ababa': 25}
        }

    def expand(self, node):
        # Returns the list of child nodes from the current node's state
        children = []
        for neighbor, cost in self.graph.get(node.state, {}).items():
            children.append(Node(neighbor, parent=node, action=f"Move to {neighbor}", path_cost=node.path_cost + cost))
        return children

# Main function to solve the problem
def visit_all_goals(problem):
    current_state = problem.initial
    path = []

    # Continue visiting goal states until all are visited
    while problem.goal_states:
        # Find the closest goal state to the current state
        closest_goal = min(problem.goal_states, key=lambda goal: uniform_cost_search(problem, current_state, goal).path_cost)
        
        # Apply UCS to find the path to the closest goal
        solution_node = uniform_cost_search(problem, current_state, closest_goal)

        # If a solution is found, backtrack to get the path
        if solution_node:
            path_segment = []
            node = solution_node
            while node:
                path_segment.append(node.state)
                node = node.parent
            # Convert the reversed iterator to a list before slicing
            path += list(reversed(path_segment))[1:]  # Add the path excluding the current state (because it's already in the path)
            
            current_state = closest_goal
            problem.goal_states.remove(closest_goal)
        else:
            print("No solution found.")
            break

    return path

# Testing the solution
if __name__ == '__main__':
    initial_state = 'Addis Ababa'
    goal_states = ['Axum', 'Gondar', 'Lalibela', 'Babile', 'Jimma', 'Bale', 'Sof Oumer', 'Arba Minch']
    
    problem = EthiopiaProblem(initial_state, goal_states)
    
    solution_path = visit_all_goals(problem)
    
    print("Solution Path:", ' -> '.join(solution_path))


