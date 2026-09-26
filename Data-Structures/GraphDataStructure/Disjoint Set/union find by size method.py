class DSU:
    def __init__(self,size):
        self.parent=list(range(size))
    def find(self,i):
        if self.parent[i]==i:
            return i
        return self.find(self.parent[i])

    def union(self,i,j):
        irep=self.find(i)
        jrep=self.find(j) 
        self.parent[jrep]=irep
        