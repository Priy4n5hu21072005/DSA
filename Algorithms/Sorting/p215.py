# Problem 215 : Kth Largest Element in an Array
# input nums :[2,3,4,2,1] , k = 2 
# output : 3
class Solution(object):
    def LargestElement(self,nums,k):
        nums.sort(reverse=True)
        return nums[k-1]
    

if __name__ == "__main__":
    nums = [2,3,4,2,1]
    k = 2
    print(Solution().LargestElement(nums,k))