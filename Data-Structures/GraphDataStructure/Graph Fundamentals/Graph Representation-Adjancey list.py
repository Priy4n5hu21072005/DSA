class Solution:
    def create_adjacency_list(Vertex,Edges):
        adjancency_list=[[]for _ in range(Vertex)]
        for edge in Edges:
            u=edge[0]
            v=edge[1]
            adjancency_list[u].append(v)
            adjancency_list[v].append(u)  
        return adjancency_list
    if __name__ == "__main__":
        vertex=3
        edges=[(0,1),(0,2),(1,2)]
        adjacency_list=create_adjacency_list(vertex,edges)
        for i in range(vertex):
            print(f"{i}->",end=" ")
            for j in adjacency_list[i]:
                print(j,end=" ")
            print()  

