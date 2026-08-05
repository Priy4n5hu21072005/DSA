import heapq
class Solution:
    def Kth_Smallest_Element_In_Matrix(self,matrix:list[list[int]],k:int)->int:
        n=len(matrix)
        heap=[]

        for r in range(n):
            heapq.heappush(heap,(matrix[r][0],r,0))

        for _ in range(k-1):
            val,row,col=heapq.heappop(heap)

            if col+1<n:
                heapq.heappush(heap,(matrix[row][col+1],row,col+1))

        return heapq.heappop(heap)[0]

matrix = [[1,5,9],[11,13,15],[12,13,21]]
k=4  
object=Solution()
print(object.Kth_Smallest_Element_In_Matrix(matrix,k))