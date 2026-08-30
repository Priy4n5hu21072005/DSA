class Solution:
    def dailyTemp(self,temp:list[int])->list[int]:
        ans=[0]*len(temp)
        stack=[]
        for i in range(len(temp)-1,-1,-1):
            while stack and temp[stack[-1]]<=temp[i]:
                stack.pop()
            if stack:
                ans[i]=stack[-1]-i
            stack.append(i)  
        return ans



        '''
        temp=[73,74,75,71,69,72,76,73]
        ans=[0,0,0,0,0,0,0,0]
        stack=[]
        for i (7->0)
            i=7
            while fail
            if fail
            stack=[7]

            i=6
            while stack and temp[stack[-1]]<=temp[i]
                    pass and temp[7]=73 <= temp[6]=76              73 <= 76     pass
                        stack =[]
            if stack fail

            stack=[6]

            i=5
            while stack and temp[6]=76<=temp[5]=72                        76 <= 72 fail
            if stack pass
             ans[5]= 6-5 = 1
             ans = [0,0,0,0,0,1,0,0]
            stack=[5,6]

            i=4
            while stack and temp[5]= 72 < temp[4] = 69                         72 <= 69 fail
            if stack pass
                ans[4]=5-4=1
                ans=[0,0,0,0,1,1,0,0]
            stack[4,5,6]

            i=3
            while stack and temp[4]=69 <= temp[3]=71                       69<=71 fail
            if stack pass
                ans[3]=4-3=1
                ans=[0,0,0,1,1,1,0,0]
            stack=3,4,5,6

            i=2
            while stack and temp[3] = 71 <= temp[2]=75                            71<=75
                stack=[4,5,6]
            while stack and temp[4] = 69 <= temp[2] =75
                stack=5,6
            while stack and temp[5]=72 <= temp[2]=75
                stack=6 
            while stack and temp[6]=76 <= temp[2]=75 
            if stack 
                ans[2]=6-2=4


        '''