## PRACTICAL NO: 02
## Implementation of A Star Algorithm  

from queue import PriorityQueue

class State(object):

    def __init__(self, value, parent,
                 start = 0,
                 goal = 0):

        self.children = []
        self.parent = parent
        self.value = value
        self.dist = 0

        if parent:
            self.start  = parent.start
            self.goal   = parent.goal
            self.path   = parent.path[:]
            self.path.append(value)
        else:
            self.path   = [value]
            self.start  = start
            self.goal   = goal

    def GetDistance(self):
        pass

    def CreateChildren(self):
        pass

class State_String(State):
    def __init__(self,value,parent,
                 start = 0,
                 goal = 0):

        super(State_String, self).__init__(value, parent, start, goal)
        self.dist = self.GetDistance()

    def GetDistance(self):

        if self.value == self.goal:
            return 0
        dist = 0
        for i in range(len(self.goal)):
            letter = self.goal[i]
            try:
                dist += abs(i - self.value.index(letter))
            except:
                dist += abs(i - self.value.find(letter))
        return dist

    def CreateChildren(self):
        if not self.children:
            for i in range(len(self.goal)-1):
                val = self.value
                val = val[:i] + val[i+1] + val[i] + val[i+2:]
                child = State_String(val, self)
                self.children.append(child)

class AStar_Solver:
    def __init__(self, start , goal):
        self.path          = []
        self.visitedQueue  = []
        self.priorityQueue = PriorityQueue()
        self.start         = start
        self.goal          = goal

    def Solve(self):
        startState = State_String(self.start,
                                  0,
                                  self.start,
                                  self.goal)

        count = 0
        self.priorityQueue.put((0,count,startState))

        while(not self.path and self.priorityQueue.qsize()):
            closestChild = self.priorityQueue.get()[2]
            closestChild.CreateChildren()
            self.visitedQueue.append(closestChild.value)

            for child in closestChild.children:
                if child.value not in self.visitedQueue:
                    count +=1
                    if not child.dist:
                        self.path = child.path
                        break
                    self.priorityQueue.put((child.dist,count,child))

        if not self.path:
            print("Goal of %s is not possible!" % (self.goal))

        return self.path


if __name__ == "__main__":
    start1 = "meshpratha"
    goal1  = "prathamesh"
    # start1 = "elloh"
    # goal1  = "hello"
    print("Starting...")

    a = AStar_Solver(start1, goal1)
    a.Solve()

    for i in range(len(a.path)):
        print("{0}) {1}".format(i, a.path[i]))


'''
This code implements the A* algorithm to solve a string transformation problem. Here's a step-by-step explanation:

1. The `State` class represents a state in the search space. It has attributes like `children` (list of child states), `parent`, `value` (the current state), `dist` (distance or cost to reach the goal state), `start` (the initial state), and `goal` (the target state).

2. The `State_String` class is a subclass of `State` and is specialized for string transformations. It overrides the `GetDistance` method to calculate the distance (heuristic value) between the current state and the goal state. It uses the number of letter positions that need to be changed to transform the current state into the goal state.

3. The `CreateChildren` method in `State_String` generates child states by swapping adjacent letters in the current state. Each child state is created by swapping two adjacent letters in the string.

4. The `AStar_Solver` class is responsible for solving the string transformation problem using the A* algorithm. It maintains a priority queue to prioritize states based on their distance and a visited queue to keep track of visited states.

5. The `Solve` method performs the A* search. It starts with the initial state and continues until a solution is found or there are no more states to explore.

6. It creates the initial state and adds it to the priority queue with a priority based on the distance. The count variable is used to break ties when multiple states have the same distance.

7. The main loop continues until a solution is found (`self.path`) or there are no more states in the priority queue.

8. It selects the state with the lowest distance from the priority queue and generates its children.

9. The children that have not been visited are added to the visited queue and inserted into the priority queue based on their distance.

10. If a child state has a distance of 0, it means the goal state is reached. The solution path is set to the child's path, and the loop is broken.

11. If no solution is found, it prints a message indicating that the goal state is not possible.

12. Finally, the `Solve` method returns the solution path.

13. In the `__main__` section, a sample string transformation problem is defined with the `start1` and `goal1` variables.

14. An instance of the `AStar_Solver` class is created with the initial and goal states.

15. The `Solve` method is called to find the solution path.

16. The solution path is printed step by step.

This implementation demonstrates how the A* algorithm can be used to solve a string transformation problem by finding the minimum number of operations (swapping adjacent letters) required to transform the initial state into the goal state.

'''