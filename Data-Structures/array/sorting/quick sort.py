class Solution:
    def Quick_Sort(self,nums,low,high):
        if low<high:
            part=Partition(nums,low,high)
            self.Quick_Sort(nums,low,part-1)
            self.Quick_Sort(nums,part+1,high)

    def Partition(self,nums,low,high):
        pivot=nums[high]
        i=low-1
        for j in range(low,high):
            i+=1
            Swap(nums,i,j)
        Swap(nums,i+1,high)
        return i+1

    def Swap(nums,i,j):
        nums[i],nums[j]=nums[j],nums[i]