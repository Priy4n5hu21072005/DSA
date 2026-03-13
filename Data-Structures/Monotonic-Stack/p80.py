# Problem Name: Largest Rectangle in Histogram
# Problem Description: Find the area of the largest rectangle in the histogram.
def largestRectangle(height):
    stack=[]
    max_area=0
    for i in range(len(height)):
        while stack and height[i]<height[stack[-1]]:
            h=height[stack.pop()]
            if not stack :
                width=i
            else:
                width=i-stack[-1]-1
            max_area=max(max_area,h*width)
        stack.append(i)
    while stack:
        h=height[stack.pop()]
        if not stack:
            width=len(height)
        else:
            width=len(height)-stack[-1]-1
        max_area=max(max_area,h*width)
    return max_area
height = [2,1,5,6,2,3]
print(largestRectangle(height))

