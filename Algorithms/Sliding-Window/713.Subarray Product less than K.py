class BruteForceSolution:
    def SubarrayProductLessThanK(self,nums:list[int],k:int)->int:
        count = 0 
        
        for start in range(len(nums)):
            product=1
            for end in range(start,len(nums)):
                product*=nums[end]
                if product<k:
                    count+=1
        return count

class OptimalSolution:
    def SubarrayProductLessThanK(self,nums:list[int],k:int)->int:
        if k <= 1:
            return 0
        left = 0 
        product = 1
        count = 0 
        for right in range(len(nums)):
            product=product*nums[right]
            while product>=k:
                product//=nums[left]
                left+=1
            count+=(right-left+1)
        return count
nums=[10,5,2,6]
k=100
object1=BruteForceSolution()
object2=OptimalSolution()
print(object1.SubarrayProductLessThanK(nums,k))

print(object2.SubarrayProductLessThanK(nums,k))