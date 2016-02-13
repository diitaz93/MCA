import math
from numpy import *
halfL=15.0
x=[]
y=[]
angle=linspace(math.pi/2,0)
#print angle
#print "x\ty"
for a in angle:
    print halfL*math.cos(a),"\t",halfL*math.sin(a)
