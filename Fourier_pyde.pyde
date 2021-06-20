from math import pi
time,n = 0,1
yList = []

def setup():
    size(800,600)

def draw():
    global time,n
    x,y=0,0
    background(0)
    translate(200,200)
    for i in range(500):
        prevx = x
        prevy = y
        n = i*2+1
        radius = 75*(4/(n*pi))
        stroke(255)
        noFill()
        ellipse(prevx,prevy,2*radius,2*radius)
        x += radius*cos(radians(n*time))
        y += radius*sin(radians(n*time))
        stroke(255)
        line(prevx,prevy,x,y)
        fill(255,0,0)
        ellipse(x,y,5,5)
    
    
    yList.insert(0,y)
    # This is for drawing the curve
    beginShape()
    translate(200,0)
    noFill()
    line(x-200,y,0,yList[0])
    for i in range(len(yList)):
        vertex(i,yList[i])
    endShape()
    time+=1
