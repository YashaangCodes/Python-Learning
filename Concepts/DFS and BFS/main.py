
def DFS(graph,vertex,visited,n):
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
print("DFS Trversal : ", end="")
DFS(graph,start,visited,n)
