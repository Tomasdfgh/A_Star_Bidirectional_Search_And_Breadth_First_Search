# README for ROB311 Artificial Intelligence

## Introduction

Welcome to the README for the Artificial Intelligence (ROB311) class project. In this project, we explore various search algorithms, namely A* search, Breadth-First Search (BFS), and Bidirectional Search, to solve different types of search problems. The code presented here is the result of our efforts in understanding and implementing these algorithms as part of our coursework.

## Code Structure

This project comprises several Python code files, each serving a specific purpose. Before we proceed further, let's briefly discuss the structure of these files.

### `search_problems.py`

`search_problems.py` is a foundational module provided by the teaching team for the ROB311 class. It defines the essential components of a search problem, including nodes, search problem abstractions, and specific problem classes like `SimpleSearchProblem`, `GraphSearchProblem`, and `GridSearchProblem`. This module sets the groundwork for our search algorithms to operate on.

### `a_star_search.py`

`a_star_search.py` implements the A* search algorithm. A* is a popular heuristic search algorithm used for finding the shortest path in a graph or grid. It uses a combination of the cost to reach a node and a heuristic estimate of the cost to the goal node. A* maintains a priority queue to efficiently explore the most promising paths.

### `breadth_first_search.py`

`breadth_first_search.py` focuses on implementing Breadth-First Search (BFS). BFS explores all the neighbors of a node before moving on to their children, making it suitable for finding the shortest path in unweighted graphs. It employs a queue to systematically traverse the graph or grid.

### `bidirectional_search.py`

`bidirectional_search.py` introduces Bidirectional Search, a strategy that explores the search space from both the initial and goal states simultaneously. It aims to find a meeting point in the search space to reduce the overall exploration. This can be particularly effective when the search space is large.

## How the Algorithms Work

Let's delve into how each of these algorithms works, based on the code provided:

### A* Search

A* search is an informed search algorithm. It uses a priority queue to explore nodes, with the priority determined by a combination of the path cost to reach a node and a heuristic estimate of the remaining cost to the goal. The algorithm operates as follows:

1. Initialize a priority queue with the initial state.
2. While the priority queue is not empty:
   a. Pop the node with the lowest priority (lowest total cost).
   b. Expand this node by considering its child nodes.
   c. Calculate the cost of each child node, add it to the path, and push it into the priority queue.
   d. Repeat until the goal state is reached or the priority queue becomes empty.

### Breadth-First Search

Breadth-First Search (BFS) is an uninformed search algorithm that explores the search space systematically. It uses a queue to maintain the order of exploration. The algorithm operates as follows:

1. Initialize a queue with the initial state.
2. While the queue is not empty:
   a. Pop the node at the front of the queue.
   b. Expand this node by considering its child nodes.
   c. Add the child nodes to the back of the queue.
   d. Repeat until the goal state is reached or the queue becomes empty.

### Bidirectional Search

Bidirectional Search is a strategy that simultaneously explores the search space from both the initial and goal states. It aims to find a meeting point in the search space, effectively reducing the overall exploration. The algorithm operates as follows:

1. Initialize two queues, one from the initial state and one from the goal state.
2. While both queues are not empty:
   a. Pop a node from each queue.
   b. Expand these nodes by considering their child nodes.
   c. Check if there is a meeting point (a node common to both frontiers).
   d. If a meeting point is found, combine the paths from the initial and goal states to this node to form the final path.
   e. Repeat until a meeting point is found or one of the queues becomes empty.

## Performance Comparison

Now, let's discuss how these algorithms perform in different scenarios and why you might choose one over the others:

### A* Search

A* search is a highly efficient algorithm when you have access to a good heuristic function. It guarantees an optimal solution when the heuristic is admissible (never overestimates the true cost). A* is particularly suitable for graph and grid problems where edge costs are non-uniform. It excels at finding the shortest path efficiently.

![image](https://github.com/Tomasdfgh/A_Star_Bidirectional_Search_And_Breadth_First_Search/assets/86145397/376941b6-61d6-45c0-bbcb-9d4279057249)

Result of an A* search trial

### Breadth-First Search

BFS is a simple and reliable algorithm for finding the shortest path in unweighted graphs or grids. It explores all neighbors of a node before moving on to their children, ensuring that it finds the shortest path first. However, BFS can be slow in large search spaces, as it expands nodes uniformly.

![image](https://github.com/Tomasdfgh/A_Star_Bidirectional_Search_And_Breadth_First_Search/assets/86145397/4a50beb0-ccf2-4c68-920f-828d49074965)

Result of a BFS search trial

### Bidirectional Search

Bidirectional Search is an excellent choice when you have both the initial and goal states and you want to find the shortest path efficiently. It reduces the search space by exploring from both ends simultaneously, often resulting in faster convergence to a solution. Bidirectional Search is highly effective when the search space is large.

![image](https://github.com/Tomasdfgh/A_Star_Bidirectional_Search_And_Breadth_First_Search/assets/86145397/12595f71-e06f-4a52-a1bf-79f6b64f3818)

Result of a Bidirectional search trial

## Conclusion

In conclusion, this project provides implementations of three essential search algorithms: A* search, Breadth-First Search, and Bidirectional Search. These algorithms are crucial tools in the field of Artificial Intelligence, allowing machines to find optimal solutions to various problems.

This project was completed as part of the ROB311 (Artificial Intelligence) class. While the code file `search_problems.py` was provided by the teaching team, the implementations of A* search, Breadth-First Search, and Bidirectional Search were carried out independently.

We hope this project and the accompanying README provide valuable insights into these search algorithms and their practical applications. Feel free to explore the code, experiment with different scenarios, and use these algorithms in your own projects.

Thank you for reading, and happy searching!

---
*This project was completed as part of the ROB311 (Artificial Intelligence) class. The `search_problems.py` code file was provided by the teaching team, while the implementations of A* search, Breadth-First Search, and Bidirectional Search were carried out independently by the author.*
