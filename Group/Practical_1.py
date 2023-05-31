## PRACTICAL NO: 01
## Implementation of DFS and BFS Algorithms:

graph = {'A':['B', 'E', 'C'],
         'B':['A', 'D', 'E'],
         'D':['B', 'E'],
         'E':['A', 'D', 'B'],
         'C':['A', 'F', 'G'],
         'F':['C'],
         'G':['C']
         }
visited = []
queue = []

def bfs(visited, graph, start_node, goal_node):
    visited.append(start_node)
    queue.append(start_node)
    while queue:
        m = queue.pop(0)
        print(m)
        if m == goal_node:
            print("Node is Found !!! ")
            break
        else:
            for n in graph[m]:
                if n not in visited:
                    visited.append(n)
                    queue.append(n)

print("The BFS Traversal is : ")
bfs(visited, graph, 'A', 'D')

#DFS
graph = {'A':['B', 'E', 'C'],
         'B':['A', 'D', 'E'],
         'D':['B', 'E'],
         'E':['A', 'D', 'B'],
         'C':['A', 'F', 'G'],      
         'F':['C'],
         'G':['C']
         }

visited = []
stack = []
def dfs(graph, start, goal):
    print("DFS traveral is: ")
    stack.append(start)
    visited.append(start)
    while stack:
        node = stack[-1]
        stack.pop()
        print("Node: ", node)
        if node == goal:
            print("Goal node found!")
            return
        for n in graph[node]:
            if n not in visited:
                visited.append(n)
                stack.append(n)

dfs(graph, 'A', "D")

'''
This code implements Depth-First Search (DFS) and Breadth-First Search (BFS) algorithms for traversing a graph. Let's go through each part of the code and explain how it works:

1. The graph is represented as a dictionary, where the keys represent nodes, and the values are lists of neighboring nodes.

2. For both DFS and BFS, there is a `visited` list to keep track of visited nodes.

3. In the BFS algorithm:
   - The `bfs` function takes the `visited` list, the graph, the starting node, and the goal node as inputs.
   - The starting node is added to the `visited` list and the `queue`.
   - While the `queue` is not empty, the first element (`m`) is removed from the `queue`.
   - If `m` is equal to the goal node, it means the goal node is found, and a message is printed.
   - Otherwise, for each neighbor `n` of `m`, if `n` is not visited, it is added to the `visited` list and the `queue`.
   - The process continues until the goal node is found or the `queue` is empty.

4. In the DFS algorithm:
   - The `dfs` function takes the graph, the starting node, and the goal node as inputs.
   - The `stack` and `visited` lists are initialized.
   - The starting node is added to the `stack` and `visited` list.
   - While the `stack` is not empty, the top element (`node`) is removed from the `stack`.
   - The `node` is printed.
   - If the `node` is equal to the goal node, it means the goal node is found, and a message is printed, and the function returns.
   - For each neighbor `n` of the `node`, if `n` is not visited, it is added to the `visited` list and the `stack`.
   - The process continues until the goal node is found or the `stack` is empty.

5. In the test section, the BFS algorithm is called with the graph, starting node 'A', and the goal node 'D'. The BFS traversal is printed.

6. Then, the DFS algorithm is called with the graph, starting node 'A', and the goal node 'D'. The DFS traversal is printed.

Both algorithms aim to traverse the graph and find the goal node. BFS explores the graph in a breadth-first manner, visiting all nodes at the same level before moving to the next level. DFS explores the graph in a depth-first manner, visiting a node and exploring as far as possible along each branch before backtracking.

Note that in the DFS implementation, the stack is used to keep track of nodes to be explored, while in the BFS implementation, a queue is used to explore nodes in the order they were discovered.

Overall, this code provides a simple implementation of BFS and DFS algorithms for graph traversal.
'''