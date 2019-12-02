# TwitterFakeAccount
using 10 minute email to create fake account :) and perform certain action such as retweet/like/reply





Assignment-1
1. Basic Idea of Python Programming.
Ans. Python is a powerful multi-purpose programming language created by Guido van
Rossum. It has simple easy-to-use syntax, making it the perfect language for someone
trying to learn computer programming for the first time.
2. Write a program to implement factorial of a given number.
Ans.
num = int(input("Enter a number: "))
factorial = 1
if num < 0:
print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
print("The factorial of 0 is 1")
else:
for i in range(1,num + 1):
factorial = factorial*i
print("The factorial of",num,"is",factorial)

3. Write a program to implement Fibonacci of a given number.
Ans.
def Fibonacci(n):
if n<0:
print("Incorrect input")
# First Fibonacci number is 0
elif n==1:
return 0
# Second Fibonacci number is 1
elif n==2:
return 1
else:
return Fibonacci(n-1)+Fibonacci(n-2)
# Driver Program
num = int(input("Enter a number: ")
print(Fibonacci(num))

4. Write a program to implement Prime of a given number.
Ans.
num = int(input("Enter a number: "))
if num > 1:
for i in range(2,num):
if (num % i) == 0:
print(num,"is not a prime number")
print(i,"times",num//i,"is",num)

break
else:
print(num,"is a prime number")
else:
print(num,"is not a prime number")

5. Write a program to print the below patterns of a given number.
*
**
***
****
*****
Ans.
def pypart(n):
# outer loop to handle number of rows
# n in this case
for i in range(0, n):
# inner loop to handle number of columns
# values changing acc. to outer loop
for j in range(0, i+1):
# printing stars
print("* ",end="")
# ending line after each row
print("\r")
# Driver Code
n=5
pypart(n)

6.

1
12
123
1234
12345

Ans.
def pypart(n):
# outer loop to handle number of rows
# n in this case
for i in range(1, n+1):
# inner loop to handle number of columns
# values changing acc. to outer loop
for j in range(1, i+1):
print(j ,end="")
# ending line after each row
print("\r")
# Driver Code
n=5
pypart(n)

7. 1
22
333
4444
55555
Ans.
def pypart(n):
# outer loop to handle number of rows
# n in this case
for i in range(1, n+1):
# inner loop to handle number of columns
# values changing acc. to outer loop
for j in range(1, i+1):
print(i ,end="")
# ending line after each row
print("\r")
# Driver Code
n=5
pypart(n)

8.

1
212
32123
4321234

Ans.
def triangle(n):
k = 2*n - 2
for i in range(1, n+1):
for j in range(1, k+1):
print(end=" ")
k=k-1
for j in range(i,1,-1):
print (j, end="")
for j in range(1, i+1):
print(j , end="")
print("\r")
# Driver Code
n=4
triangle(n)

Assignment-2
1. Write a program to implement Factorial, Fibonacci of a given number.
Ans.
def Fibonacci(n):
if n<0:
print("Incorrect input")
# First Fibonacci number is 0
elif n==1:
return 0
# Second Fibonacci number is 1
elif n==2:
return 1
else:
return Fibonacci(n-1)+Fibonacci(n-2)
def Factorial(n):
fact = 1
for i in range(1,n+1):
fact = fact * i
return(fact)
# Driver Program
print(Fibonacci(5))
print(Factorial(5))
2. Write a program to solve 4-Queen problem.
Ans.
global N
N=4
def printSolution(board):
for i in range(N):
for j in range(N):
print (board[i][j], end = " ")
print()
def isSafe(board, row, col):
for i in range(col):
if board[row][i] == 1:
return False
for i, j in zip(range(row, -1, -1),
range(col, -1, -1)):
if board[i][j] == 1:
return False

for i, j in zip(range(row, N, 1), range(col, -1, -1)):
if board[i][j] == 1:
return False
return True
def solveNQUtil(board, col):
if col >= N:
return True
for i in range(N):
if isSafe(board, i, col):
board[i][col] = 1
if solveNQUtil(board, col + 1) == True:
return True
board[i][col] = 0
return False
def solveNQ():
board = [ [0, 0, 0, 0],
[0, 0, 0, 0],
[0, 0, 0, 0],
[0, 0, 0, 0] ]
if solveNQUtil(board, 0) == False:
print ("Solution does not exist")
return False
printSolution(board)
return True
# Driver Code
solveNQ()
3. Write a program to solve traveling salesman problem.
Ans.
from sys import maxsize
V=4

# implementation of traveling Salesman Problem
def travellingSalesmanProblem(graph, s):
# store all vertex apart from source vertex
vertex = []
for i in range(V):
if i != s:
vertex.append(i)
# store minimum weight Hamiltonian Cycle
min_path = maxsize
while True:
# store current Path weight(cost)
current_pathweight = 0
# compute current path weight
k=s
for i in range(len(vertex)):
current_pathweight += graph[k][vertex[i]]
k = vertex[i]
current_pathweight += graph[k][s]
# update minimum
min_path = min(min_path, current_pathweight)
if not next_permutation(vertex):
break
return min_path
# next_permutation implementation
def next_permutation(L):
n = len(L)
i=n-2
while i >= 0 and L[i] >= L[i + 1]:
i -= 1
if i == -1:
return False
j=i+1
while j < n and L[j] > L[i]:
j += 1

j -= 1
L[i], L[j] = L[j], L[i]
left = i + 1
right = n - 1
while left < right:
L[left], L[right] = L[right], L[left]
left += 1
right -= 1
return True
# Driver Code
if __name__ == "__main__":
# matrix representation of graph
graph = [[0, 10, 15, 20], [10, 0, 35, 25],
[15, 35, 0, 30], [20, 25, 30, 0]]
s=0
print(travellingSalesmanProblem(graph, s))
4. Write a program to solve water jug problem.
Ans.
from collections import defaultdict
jug1, jug2, aim = 4, 3, 2
visited = defaultdict(lambda: False)
def waterJugSolver(amt1, amt2):
if (amt1 == aim and amt2 == 0) or (amt2 == aim and amt1 == 0):
print(amt1, amt2)
return True
if visited[(amt1, amt2)] == False:
print(amt1, amt2)
visited[(amt1, amt2)] = True
return (waterJugSolver(0, amt2) or
waterJugSolver(amt1, 0) or
waterJugSolver(jug1, amt2) or
waterJugSolver(amt1, jug2) or
waterJugSolver(amt1 + min(amt2, (jug1-amt1)),
amt2 - min(amt2, (jug1-amt1))) or
waterJugSolver(amt1 - min(amt1, (jug2-amt2)),
amt2 + min(amt1, (jug2-amt2))))
else:
return False
print("Steps: ")
waterJugSolver(0, 0)

5. Implementation of Breath first Search and Depth first search.
Ans.
from collections import defaultdict
class Graph:
def __init__(self):
self.graph = defaultdict(list)
def addEdge(self,u,v):
self.graph[u].append(v)
def BFS(self, s):
visited = [False] * (len(self.graph))
queue = []
queue.append(s)
visited[s] = True
while queue:
s = queue.pop(0)
print (s, end = " ")
for i in self.graph[s]:
if visited[i] == False:
queue.append(i)
visited[i] = True
g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)
print ("Following is Breadth First Traversal" "(starting from vertex 2)")
g.BFS(2)
6. Implementation of Breath first Search and Depth first search.
Ans.
from collections import defaultdict
class Graph:
def __init__(self):
self.graph = defaultdict(list)
def addEdge(self, u, v):
self.graph[u].append(v)
def DFSUtil(self, v, visited):
visited[v] = True
print(v, end = ' ')
for i in self.graph[v]:
if visited[i] == False:

self.DFSUtil(i, visited)
def DFS(self, v):
visited = [False] * (len(self.graph))
self.DFSUtil(v, visited)
# Driver code
g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)
print("Following is DFS from (starting from vertex 2)")
g.DFS(2)
7. Implementation of A* and AO*
Ans.
def heuristic(a, b):
(x1, y1) = a
(x2, y2) = b
return abs(x1 - x2) + abs(y1 - y2)
def a_star_search(graph, start, goal):
frontier = PriorityQueue()
frontier.put(start, 0)
came_from = {}
cost_so_far = {}
came_from[start] = None
cost_so_far[start] = 0
while not frontier.empty():
current = frontier.get()
if current == goal:
break
for next in graph.neighbors(current):
new_cost = cost_so_far[current] + graph.cost(current, next)
if next not in cost_so_far or new_cost < cost_so_far[next]:
cost_so_far[next] = new_cost
priority = new_cost + heuristic(goal, next)
frontier.put(next, priority)
came_from[next] = current
return came_from, cost_so_far

8. TIC TAC TOE
Ans.
# Tic-Tac-Toe Program using
# random number in Python
# importing all necessary libraries
import numpy as np
import random
from time import sleep
# Creates an empty board
def create_board():
return(np.array([[0, 0, 0],
[0, 0, 0],
[0, 0, 0]]))
# Check for empty places on board
def possibilities(board):
l = []
for i in range(len(board)):
for j in range(len(board)):
if board[i][j] == 0:
l.append((i, j))
return(l)
# Select a random place for the player
def random_place(board, player):
selection = possibilities(board)
current_loc = random.choice(selection)
board[current_loc] = player
return(board)
# Checks whether the player has three
# of their marks in a horizontal row
def row_win(board, player):
for x in range(len(board)):
win = True
for y in range(len(board)):
if board[x, y] != player:
win = False
continue
if win == True:
return(win)

return(win)
# Checks whether the player has three
# of their marks in a vertical row
def col_win(board, player):
for x in range(len(board)):
win = True
for y in range(len(board)):
if board[y][x] != player:
win = False
continue
if win == True:
return(win)
return(win)
# Checks whether the player has three
# of their marks in a diagonal row
def diag_win(board, player):
win = True
for x in range(len(board)):
if board[x, x] != player:
win = False
return(win)
# Evaluates whether there is
# a winner or a tie
def evaluate(board):
winner = 0
for player in [1, 2]:
if (row_win(board, player) or
col_win(board,player) or
diag_win(board,player)):
winner = player
if np.all(board != 0) and winner == 0:
winner = -1
return winner
# Main function to start the game
def play_game():
board, winner, counter = create_board(), 0, 1
print(board)

sleep(2)
while winner == 0:
for player in [1, 2]:
board = random_place(board, player)
print("Board after " + str(counter) + " move")
print(board)
sleep(2)
counter += 1
winner = evaluate(board)
if winner != 0:
break
return(winner)
# Driver Code
print("Winner is: " + str(play_game()))


