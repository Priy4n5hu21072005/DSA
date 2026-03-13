# Problem Name: Random Point in Non-overlapping Rectangles
# Problem Description: Randomly and uniformly pick an integer point in the space covered by non-overlapping rectangles.
import random
import bisect
class solution(object):
    def __init__(self,rectangles):
        self.rectangles = rectangles
        self.prefix=[]
        total=0
        for x1,y1,x2,y2 in rectangles:
            points=(x2-x1+1)*(y2-y1+1)
            total += points
            self.prefix.append(total)
    def pick(self):
        rand_points=random.randint(1,self.prefix[-1])
        index=bisect.bisect_left(self.prefix,rand_points)
        x1,y1,x2,y2=self.rectangles[index]
        x= random.randint(x1,x2)
        y= random.randint(y1,y2)
        return [x,y]
rectangles=[
    [1,1,2,2],
    [3,3,4,4],
    [10,10,10,10]
]
obj=solution(rectangles)
for i in range (5):
    print(obj.pick())
