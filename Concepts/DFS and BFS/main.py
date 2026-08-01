from collections import deque

def BFS(graph,start,visited,n,reach,target):
    '''This function implements the BFS algorithm to traverse a graph represented as an adjacency matrix'''
    visited[start] = True
    queue = deque()    
    queue.append(start)
    while queue:
        vertex = queue.popleft()
        print(vertex, end = " ")

        if vertex == target :
            reach = True
            print("\nTarget Found!")
            return

        for i in range(n):
            if graph[vertex][i] == 1 and not visited[i] and not reach:
                queue.append(i)
                visited[i] = True

                if i == target : reach = True
    else :
        print("\nTarget wasn't found!")
    
def DFS(graph,vertex,visited,n,target):
    '''This function implements the DFS algorithm to traverse a graph represented as an adjacency matrix'''
    visited[vertex] = True
    print(vertex, end = " ")

    if vertex == target:
        print("\nTarget Found!")
        return True

    for i in range(n):
        if graph[vertex][i] == 1 and not visited[i] :
            if DFS(graph,i,visited,n,target):
                return True
    return False

n = int(input("Enter the number of vertices : "))

graph = []

print("Enter the Adjacency matrix : ")
for i in range(n):
    row = list(map(int, input().split()))
    graph.append(row)

start = int(input("Enter the starting vertice : "))
goal = int(input("Enter the goal vertice : "))

status = False
visited = [False] * n
print("\nBFS Traversl : ", end="")
BFS(graph,start,visited,n,status,goal)

visited = [False] * n
print("\nDFS Trversal : ", end="")
if not DFS(graph,start,visited,n,goal):
    print("\nTarget wasn't Found!")
