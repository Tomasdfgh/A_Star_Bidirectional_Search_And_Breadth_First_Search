from collections import deque
import numpy as np
from search_problems import Node, GraphSearchProblem, GridSearchProblem, get_random_grid_problem

def bidirectional_search(problem):
    # Creating forward path, backward path, Forward Queue, Backward Queue
    max_frontier_size = 0
    num_nodes_expanded = 0
    path_forward = {}
    path_backward = {}
    path_forward[problem.init_state] = [problem.init_state]
    path_backward[problem.goal_states[0]] = problem.goal_states
    Q_forward = [[problem.init_state,[problem.init_state]]]
    Q_backward = [[problem.goal_states[0],[problem.goal_states[0]]]]

    # Running a while loop until the forward Queue and backward Queue are empty
    while Q_forward and Q_backward:

        #Running a for loop for everysingle node in Q forward
        for _ in Q_forward:

            #getting the node from the queue and path of that node
            node_f,path_f = Q_forward.pop(0)
            
            #getting the children of each node
            for z_1 in problem.get_actions(node_f):
                z_1 = z_1[1]

                #Checking if there are any intersection
                if z_1 in path_backward:
                    return path_f + path_backward[z_1][::-1] ,len(path_forward) + len(path_backward),max_frontier_size

                #Checking if the node is not in path forward in order to make a new path
                if z_1 not in path_forward:
                    temp_path = path_f.copy()
                    temp_path.append(z_1)
                    Q_forward.append([z_1,temp_path])
                    max_frontier_size = max(max_frontier_size,len(Q_forward) + len(Q_backward))
                    path_forward[z_1] = path_forward[node_f] + [z_1]

        #Running a for loop for everysingle node in Q backward
        for _ in Q_backward:

            #Getting the node from the queue and path of that node
            node_b,path_b = Q_backward.pop(0)

            #getting the children of each node
            for z in problem.get_actions(node_b):
                z = z[1]

                #Checking if there are any intersection
                if z in path_forward:
                    return path_forward[z] + path_b[::-1] ,len(path_forward) + len(path_backward),max_frontier_size

                #Checking if the node is not in path backward in order to make a new path
                if z not in path_backward:
                    temp_path = path_b.copy()
                    temp_path.append(z)
                    Q_backward.append([z,temp_path])
                    max_frontier_size = max(max_frontier_size,len(Q_forward) + len(Q_backward))
                    path_backward[z] = path_backward[node_b] + [z]

    #Returning an empty path if no solution exists
    return [],0,0


def test():
    
    q1 = [1,2,3,4,5,6]
    q2 = q1.copy()

    while q1 and q2:
        if q2:
            print(q2.pop())
        else:
            print(q1.pop())


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
    #path, num_nodes_expanded, max_frontier_size = bidirectional_search(problem)
    path, num_nodes_expanded, max_frontier_size = bidirectional_search(problem)
    correct = problem.check_graph_solution(path)
    print("---Simple Example---")
    print("path:  "  + str(path))
    print("num_nodes_expanded: " + str(num_nodes_expanded))
    print("max_frontier_size: " + str(max_frontier_size))
    print("Solution is correct: {:}".format(correct))
    print(" ")

    # Use stanford_large_network_facebook_combined.txt to make your own test instances
    E = np.loadtxt('stanford_large_network_facebook_combined.txt', dtype=int)
    V = np.unique(E)
    goal_states = [349]
    init_state = 0
    problem = GraphSearchProblem(goal_states, init_state, V, E)
    path, num_nodes_expanded, max_frontier_size = bidirectional_search(problem)
    correct = problem.check_graph_solution(path)
    print("---Actual Example---")
    print("path:  "  + str(path))
    print("num_nodes_expanded: " + str(num_nodes_expanded))
    print("max_frontier_size: " + str(max_frontier_size))
    print("Solution is correct: {:}".format(correct))
    # Be sure to compare with breadth_first_search!

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
    path, num_nodes_expanded, max_frontier_size = bidirectional_search(problem)
    # Check the result
    correct = problem.check_solution(path)
    print("Solution is correct: {:}".format(correct))
    # Plot the result
    problem.plot_solution(path)
    print(path)
    bi_path = path
    