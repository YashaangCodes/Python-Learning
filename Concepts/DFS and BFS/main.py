from collections import deque

def BFS(graph,start,visited,n):
    '''This function implements the BFS algorithm to traverse a graph represented as an adjacency matrix'''
    visited[start] = True
    queue = deque()    
    queue.append(start)
    while queue:
        vertex = queue.popleft()
        print(vertex, end = " ")
        for i in range(n):
            if graph[vertex][i] == 1 and not visited[i] :
                queue.append(i)
                visited[i] = True
    
def DFS(graph,vertex,visited,n):
    '''This function implements the DFS algorithm to traverse a graph represented as an adjacency matrix'''
    visited[vertex] = True
    print(vertex, end = " ")
    for i in range(n):
        if graph[vertex][i] == 1 and not visited[i] :
            DFS(graph,i,visited,n)

n = int(input("Enter the number of vertices : "))

graph = []

print("Enter the Adjacency matrix : ")
for i in range(n):
    row = list(map(int, input().split()))
    graph.append(row)

start = int(input("Enter the starting vertice : "))

visited = [False] * n
print("BFS Traversl : ", end="")
BFS(graph,start,visited,n)

visited = [False] * n
print("\nDFS Trversal : ", end="")
DFS(graph,start,visited,n)
