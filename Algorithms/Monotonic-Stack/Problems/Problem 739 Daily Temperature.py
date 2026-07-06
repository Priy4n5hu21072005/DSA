'''
Humien ek temperature array diya hai aur humein ek aisa array return karana hai jisme har temperature
ke next greater temperature kab mila hai for example 
temperature =[73,74,75,71,69,72,76,73]
ab 73 ka next greater -> 74 hai 1 day 
aur 74 ka 75 hai 1 day 
aur 75 ka 76 hai 4 day 
71 ka 72 hai 2 day 
69 ka 72 hai 1 day 
72 ka hai 76 1 day
76 ka nahi hai 0 
73 ka nahi hai 0 

toh ans [1,1,4,2,1,1,0,0]'''

'''
stack =[]
ans = [0]*len(temperature)
for i in n-1 to 0:
    while stack and temperature[stack[-1]]<temperature[i]:
        stack.pop()
    if stack:
        ans[i]=stack[-1]-i
    stack.append(i)
return ans '''

'''                                         DRY RUN                                                         '''
'''nums =[73,74,75,71,69,72,76,73]
target output [1,1,4,2,1,1,0,0]
stack =[]
ans =[0,0,0,0,0,0,0]
for (7,6,5,4,3,2,1,0):
i=7
    stack(no):
    if(no):
    stack=[7]
    
i = 6
73<76(yes)
if pass
ans[6]'''