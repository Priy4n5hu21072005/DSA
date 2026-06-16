class Solution:
    def Merge(nums,left,right,mid):
        n1 = mid -left + 1
        n2 = right - mid
        L = [0]*n1
        R = [0]*n2
        for i in range(n1):
            L[i] = nums[left+i]
        for j in range(n2):
            R[j] = nums[mid+j+1]
        i,j,k = 0,0,left
        while i < n1 and j < n2:
            if L[i] <= R[j]:
                nums[k] = L[i]
                i+=1
            else:
                nums[k] = R[j]
                j+=1
            k+=1
        while i < n1 :
            nums[k] = L[i]
            i+=1
            k+=1
        while j < n2:
            nums[k] = R[j]
            j+=1
            k+=1
    def MergeSort(nums,left,right):
        if left < right :
            mid = (left+right)//2
            
            Solution.MergeSort(nums,left,mid)
            Solution.MergeSort(nums,mid+1,right)
            Solution.Merge(nums,left,right,mid)
nums = [12,11,10,5,6,7]
Solution.MergeSort(nums,0,len(nums)-1)
print(nums)

