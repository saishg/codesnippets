from collections import deque
 
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
     
    def __str__(self):
        return "X=%d,Y=%d" % (self.x, self.y)
 
def getPointsFromPoint(N, arr, point):
    x = point.x
    y = point.y
    points = []
     
    while x > 0:
        x -= 1
        if arr[x][y] == 'X':
            break
        points.append(Point(x,y))
     
    x = point.x
    while x < N-1: 
        x += 1
        if arr[x][y] == 'X': 
            break
        points.append(Point(x,y)) 
     
    x = point.x 
    while y > 0:
        y -= 1
        if arr[x][y] == 'X':
            break
        points.append(Point(x,y))
     
    y = point.y
    while y < N-1:
        y += 1
        if arr[x][y] == 'X':
            break
        points.append(Point(x,y))
         
    return points
     
def solveCastleGrid(N, arr, start, end):
    q = deque([start])
    arr[start.x][start.y] = 0
     
    while q:
        current_point = q.pop()
        current_distance = arr[current_point.x][current_point.y]
         
        points = getPointsFromPoint(N, arr, current_point)
        for p in points:
            if arr[p.x][p.y] == '.':
                arr[p.x][p.y] = current_distance + 1
                q.appendleft(p)
                if p.x == end.x and p.y == end.y:
                    return current_distance + 1
    return -1
     
if __name__ == '__main__':
    N = input()
    arr = [0] * N
     
    for i in xrange(N):
        arr[i] = list(raw_input())
         
    start_x, start_y, end_x, end_y = map(int, raw_input().split())
     
    print solveCastleGrid(N, arr, Point(start_x, start_y), Point(end_x, end_y))
