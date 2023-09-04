from collections import deque
import numpy as np
from search_problems import Node, GraphSearchProblem, GridSearchProblem, get_random_grid_problem

def breadth_first_search(problem):

    # Creating the path, explored bin
    max_frontier_size = 0
    num_nodes_expanded = 0
    path = {}
    bin_ = set()

    #Adding the initial state into the queue, the bin and path
    Q = [problem.init_state]
    bin_.add(Q[0])
    path[problem.init_state] = [problem.init_state]

    #Creating a loop that lasts until Q is empty
    while Q:

        #Getting the node from the Q
        node = Q.pop(0)
        temp1 = []

        #Getting all the children in each node
        for child in problem.get_actions(node):
            child = child[1]

            #Checking if the child has already been explored
            if child not in bin_:

                #Adding the child into the explored bin and the Queue
                bin_.add(child)
                Q.append(child)

                #Adding the node into the path
                path[child] = path[node] + [child]

                #Checking if the child has reached a goal node
                if child == problem.goal_states[0]:
                    return path[child], len(bin_), max_frontier_size
            max_frontier_size = max(len(Q), max_frontier_size)
    #Return an empty path if no solution exists
    return [],0,0
 

if __name__ == '__main__':
    # Simple example
    goal_states = [0]
    init_state = 9
    V = np.arange(0, 10)
    E = np.array([[0, 1],
                  [1, 2],
                  [2, 3],
                  [3, 4],
                  [4, 5],
                  [5, 6],
                  [6, 7],
                  [7, 8],
                  [8, 9],
                  [0, 6],
                  [1, 7],
                  [2, 5],
                  [9, 4]])
    problem = GraphSearchProblem(goal_states, init_state, V, E)
    path, num_nodes_expanded, max_frontier_size = breadth_first_search(problem)
    correct = problem.check_graph_solution(path)
    print("Solution is correct: {:}".format(correct))
    print("path:  "  + str(path))
    print("num_nodes_expanded: " + str(num_nodes_expanded))
    print("max_frontier_size: " + str(max_frontier_size))

    # Use stanford_large_network_facebook_combined.txt to make your own test instances
    E = np.loadtxt('stanford_large_network_facebook_combined.txt', dtype=int)
    V = np.unique(E)
    goal_states = [349]
    init_state = 0
    problem = GraphSearchProblem(goal_states, init_state, V, E)
    path, num_nodes_expanded, max_frontier_size = breadth_first_search(problem)
    correct = problem.check_graph_solution(path)
    print("Solution is correct: {:}".format(correct))
    print("path:  "  + str(path))
    print("num_nodes_expanded: " + str(num_nodes_expanded))
    print("max_frontier_size: " + str(max_frontier_size))

    # Create a random instance of GridSearchProblem
    p_occ = 0.25
    M = 100
    N = 100
    problem = get_random_grid_problem(p_occ, M, N)
    # Simple example
    goal_states = [0]
    init_state = 9
    problem = GridSearchProblem(problem.goal_states, problem.init_state, M, N, problem.grid_map)

    print("\n\n------ USING BIDIRECTIONAL SEARCH ------\n")
    # Solve it
    path, num_nodes_expanded, max_frontier_size = breadth_first_search(problem)
    # Check the result
    correct = problem.check_solution(path)
    print("Solution is correct: {:}".format(correct))
    # Plot the result
    problem.plot_solution(path)
    print(path)
    bi_path = path