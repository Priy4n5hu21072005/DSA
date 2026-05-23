# Problem name : 66 . Plus one
class solution:
    def plusone(self,digits):
        for i in range(len(digits)-1,-1,-1):
            if digits[i]!=9:
                digits[i]+=1
                return digits
            digits[i]=0
        return [1]+digits
    
# for example
digits =[1,2,3]
print(solution().plusone(digits))
