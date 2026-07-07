'''Iss Question mein humeine next smaller nikalna hai '''
'''Jo meine algo bnai hai vo pahle dekhte hai 
ek stack bnate hai 
for loop n-1 to 0:
while stack and stack[-1]>prices[i]:
stack.pop()
if stack :
ans[i]=prices[i]-stack[-1]
else:
ans[i]=price[i]
stack.append(prices[i])
return ans '''

class sol:
    def FinalPriceWithSpecialDiscount(self,prices):
        stack =[]
        ans =[0]*len(prices)
        for i in range(len(prices)-1,-1,-1):
            while stack and stack[-1]>prices[i]:
                stack.pop()
            if stack:
                ans[i]=prices[i]-stack[-1]
            else:
                ans[i]=prices[i]
            stack.append(prices[i])
        return ans   

prices = [8,4,6,2,3]
object = sol()
print(object.FinalPriceWithSpecialDiscount(prices))