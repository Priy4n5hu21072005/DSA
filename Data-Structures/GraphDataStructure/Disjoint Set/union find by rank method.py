class Disjoint_By_Rank:
    def __init__(self,n):
        self.rank=[0]*n
        self.parent=list(range(n)) 

    def find(self,i):
        root=self.parent[i]
        if self.parent[root]!=root:
            self.parent[i]=self.find(root)
            return self.parent[i]
        return root

    def union(self,x,y):
        Xroot=self.find(x)
        Yroot=self.find(y) 

        if Xroot==Yroot:
            return

        if self.rank[Xroot]<self.rank[Yroot]:
            self.parent[Xroot]=Yroot
        elif self.rank[Yroot]<self.rank[Xroot]:
            self.parent[Yroot]=Xroot
        else:
            self.parent[Yroot]=Xroot
            self.rank[Xroot]+=1
            