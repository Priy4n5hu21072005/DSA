def maxWater(height):
    i=0
    n=len[height]
    j=n-1
    max_area=0
    while i<j:
        width=j-i
        Curr_height=min(height[i],height[j])
        area=width*Curr_height
        max_area=max(max_area,area)
        if height[i]<height[j]:
            i +=1
        else:
            j -=1
    return max_area