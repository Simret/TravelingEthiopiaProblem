class MiniMax:
    def __init__(self):
        # Define the destinations and their values
        self.destinations = {
            'Fincha': 5,
            'Shambu': 4,
            'Gimbi': 8,
            'Limu': 8,
            'Hossana': 6,
            'Durame': 5,
            'BenjMaji': 5,
            'Tepi': 6,
            'Kaffa': 7,
            'Dilla': 9,
            'Chiro': 6,
            'Harar': 10
        }

        # Define the paths from Addis Ababa to each destination
        self.paths = {
            'Fincha': ['Addis Ababa', 'Ambo', 'Gedo', 'Fincha'],
            'Shambu': ['Addis Ababa', 'Ambo', 'Gedo', 'Shambu'],
            'Gimbi': ['Addis Ababa', 'Ambo', 'Nekemte', 'Gimbi'],
            'Limu': ['Addis Ababa', 'Ambo', 'Nekemte', 'Limu'],
            'Hossana': ['Addis Ababa', 'Butajira', 'Worabe', 'Hossana'],
            'Durame': ['Addis Ababa', 'Butajira', 'Worabe', 'Durame'],
            'BenjMaji': ['Addis Ababa', 'Butajira', 'Wolkite', 'BenjMaji'],
            'Tepi': ['Addis Ababa', 'Butajira', 'Wolkite', 'Tepi'],
            'Kaffa': ['Addis Ababa', 'Adama', 'Mojo', 'Kaffa'],
            'Dilla': ['Addis Ababa', 'Adama', 'Mojo', 'Dilla'],
            'Chiro': ['Addis Ababa', 'Adama', 'Diredawa', 'Chiro'],
            'Harar': ['Addis Ababa', 'Adama', 'Diredawa', 'Harar']
        }

    def minimax(self, node, depth, maximizing_player):
        if depth == 0 or node in self.destinations:
            return self.destinations.get(node, 0)

        if maximizing_player:
            max_eval = float('-inf')
            for child in self.get_children(node):
                eval = self.minimax(child, depth - 1, False)
                max_eval = max(max_eval, eval)
            return max_eval
        else:
            min_eval = float('inf')
            for child in self.get_children(node):
                eval = self.minimax(child, depth - 1, True)
                min_eval = min(min_eval, eval)
            return min_eval

    def get_children(self, node):
        children = []
        for path in self.paths.values():
            if node in path:
                index = path.index(node)
                if index + 1 < len(path):
                    children.append(path[index + 1])
        return children

    def find_best_path(self, start_node, depth):
        best_value = float('-inf')
        best_move = None

        for child in self.get_children(start_node):
            value = self.minimax(child, depth - 1, False)
            if value > best_value:
                best_value = value
                best_move = child

        return best_move, best_value

# Example usage
minimax = MiniMax()
start_node = 'Addis Ababa'
depth = 3  # Adjust depth based on the complexity of the tree
best_move, best_value = minimax.find_best_path(start_node, depth)

print(f"Best move from {start_node} is to {best_move} with a value of {best_value}")