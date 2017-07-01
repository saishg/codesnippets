points= []
points_dict = {}

def addPoint(x,y):
    if (x, y) in points_dict:
        return
    xs=str(abs(x))
    ys=str(abs(y))
    xsum=0
    ysum=0
    for c in xs:
        xsum=xsum+int(c)
    for c in ys:
        ysum=ysum+int(c)
    if xsum+ysum >=19:
        return

    points.append((x,y))
    points_dict[(x,y)] = True


def addGoodNeighbors(x,y):
    addPoint(x+1,y)
    addPoint(x-1,y)
    addPoint(x,y+1)
    addPoint(x,y-1)

addPoint(0,0)

i=0
while True:
    print i
    addGoodNeighbors(points[i][0],points[i][1])
    i=i+1
    #print len(points)
    if i>=len(points): break

print len(points)
