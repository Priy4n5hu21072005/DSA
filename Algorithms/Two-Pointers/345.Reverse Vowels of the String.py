class Solution:
    def ReverseVowels(self,s:str)->str:

        vowels ={'a','e','i','o','u','A','E','I','O','U'}
        nums=list(s)
        n = len(nums)
        left = 0 
        right = n-1

        while left<right:

            while left<right and nums[left] not in vowels:
                left+=1

            while left < right and nums[right] not in vowels:
                right-=1

            nums[left],nums[right]=nums[right],nums[left]

            left+=1
            right-=1

        return "".join(nums)
