def maximalRectangle(matrix):
    if not matrix or not matrix[0]:
        return 0
    cols=len(matrix[0])
    height=[0]*cols
    maxArea=0
    for row in matrix:
        for j in range(cols):
            if row[j]=='1':
                height[j]+=1
            else:
                height[j]=0
        stack=[]
        for i in range(cols+1):
            current_height=height[i] if i<cols else 0
            while stack and current_height<height[stack[-1]]:
                h=height[stack.pop()]
                if not stack:
                    w=i
                else:
                    w=i-stack[-1]-1
                maxArea=max(maxArea,w*h)
            stack.append(i)
    return maxArea

