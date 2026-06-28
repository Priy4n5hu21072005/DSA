'''
Humein ek Array given hai nums karke problem mein humein 2 operations allowed hai rearrangment and decrease for example
maan lo ek array hai [2,2,1,2] something like that theek hai ab pahla operation
operation 1 : Rearrangement
hum array ko [2,1,2,2],[1,2,2,2] kaise bhi re-arrange kar skte hai hai
aur ab Operation 2 : Decrease means like ek array hai [3,4,1,5] kuch aisa hai toh hum
har element ko decrease kar skte hai like 4 -> 3 kar skate hai , similarly 2 kar skate hai aise he theek hai


Ab Problem mein humein 2 condition ko satisfy karana hai
condition 1 : first element always 1
theek hai like koi array hai [21,2,1,3] -> toh vo aisa uska pahla element ye he hona chayie -> [1,21,2,3] ab order kuch
bhi ho skta hai
condition 2 : Ab har consecutive or adjucent elements ka difference 2 se jyada nahi hona chayie like this
[1,2,3,4] etc

toh ab main problem ye hai ki ab hum jo final element nikalenge uska maximum number kya hoga for example
ek array hai [5,2,3,4,1] -> final array [1,2,3,4,5] theek hai toh maximum number 5 hua
ab similarly agar array ka consecutive difference 2 se jyada hai tab kya kare toh cheez simple hai decrease karna hai
for example ek array aisa given hai [1,2,1000] toh isse aisa bnyenge [1,2,3] jaha 1000-> 3 mein bna diya hai decrease kar ke
'''


'''
ab solution derive karte hai sab se pahli cheez kya hogi agar ek array given hai like 
nums = [1,2,2,10]
theek hai tu normally traverse karta hai 
1 pe aya hai condition 1 satisfy 
2 pe gaya dekha difference 1 se jyada nahi hai 
phir 2nd waale 2 pe gaya dekha difference phir 1 se jayada nahi hai 
ab 10 pe aya difference 1 se jayada hai toh ab kya karega ek simple sa logic 10 -> 3 mein decrease aur logic min(current , previous +1)
'''

class Solution :
    def MaximumNumberFromFinalElement(self,nums):
        # Array ko sort kar diya taaki increasing order mein value mil jaaye
        nums.sort()
        # Condition 1 : first element always one
        nums[0] =1
        # Traverse whole array
        for i in range(1,len(nums)):
            # Condition 2 : difference 1 se jayada nahi
            nums[i]=min(nums[i],nums[i-1]+1)
        # Maximum number array ke last mein hoga because it is sorted
        return nums[-1]

