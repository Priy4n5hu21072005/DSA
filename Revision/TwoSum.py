'''
array = [2,7,22,11]
target=13
humein ye batana hai ki kin do numbers ka sum target ke equal hai jo exist karte hai
nums mein

nums =[2,7,22,13]
       | |
       i  j


maan le same array tha 
ab pahla element 2 thek hai 
vo target kitna =15
13 piche hai theek hai 
ab gar hum array mein traverse karte hai aur pta chalta hai ki 13 toh hai toh mil gaya na indexes
{
2:13
7:8
13:2
} 

'''
def two_sum(array,target):
    for i in range(len(array)):
        for j in range(i+1,len(array)):
            if array[i]+array[j]==target:
                return i,j
