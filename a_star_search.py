import queue
import numpy as np
from search_problems import Node, GridSearchProblem, get_random_grid_problem


def a_star_search(problem):

    #Creating the Priority Queue, Bin, path
    Q = queue.PriorityQueue()
    bin_ = set()
    path = {}
    path[problem.init_state] = [problem.init_state]
    num_nodes_expanded = 0
    max_frontier_size = 0

    #Putting the item into the Queue
    Q.put([0,problem.init_state])

    #Loop that runs until Q is empty
    while Q:
        temp = []
        
        #Getting each node from queue
        node = Q.get(0)[1]
        children = []

        #Getting the children nodes from the node
        for i in problem.get_actions(node):
            children.append(i[1])

        #Analysing each child in all the children
        for child in children:

            #Checking if this child has already been explored
            if child not in bin_:
                bin_.add(child)

                #Adding the node into the existing paths
                if node in path:
                    temp = path[node].copy()
                    temp.append(child)
                path[temp[len(temp)-1]] = temp

                #Adding the child into the Priority Queue
                Q.put([len(temp) + problem.heuristic(child),child])

                #If the child arrives at a goal state, return the path of the child
                if child == problem.goal_states[0]:
                    return path[child],len(bin_),max_frontier_size

        max_frontier_size = max(max_frontier_size,Q.qsize())

    #Returning an empty path if no answer exists
    return [],len(bin_),max_frontier_size

def search_phase_transition():
    transition_start_probability = 0.3
    transition_end_probability = 0.5
    peak_nodes_expanded_probability = 0.4
    return transition_start_probability, transition_end_probability, peak_nodes_expanded_probability


if __name__ == '__main__':
    # Test your code here!
    # Create a random instance of GridSearchProblem
    p_occ = 0.25
    M = 100
    N = 100
    problem = get_random_grid_problem(p_occ, M, N)
    path, num_nodes_expanded, max_frontier_size = a_star_search(problem)
    correct = problem.check_solution(path)
    print("Solution is correct: {:}".format(correct))
    #print("path:  "  + str(path))
    print("num_nodes_expanded: " + str(num_nodes_expanded))
    print("max_frontier_size: " + str(max_frontier_size))
    # Plot the result
    problem.plot_solution(path)

    # Experiment and compare with BFS