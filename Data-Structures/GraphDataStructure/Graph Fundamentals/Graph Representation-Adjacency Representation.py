# Adjacency Representation
class Solution:
    def create_matrix(Vertices,Edges):
        mat=[[0 for _ in range(Vertices)]for _ in range(Vertices)]
        for value in Edges:
            u=value[0]
            v=value[1]
            mat[u][v]=1
            mat[v][u]=1
        return mat

    if __name__=="__main__":
        vertices=3
        edges=[(0,1),(0,2),(1,2)]
        mat=create_matrix(vertices,edges)
        for i in range(vertices):
            for j in range(vertices):
                print(mat[i][j],end=" ")
            print()