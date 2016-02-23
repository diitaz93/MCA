from numpy import *

data=genfromtxt("salida.txt",delimiter=" ")
T=genfromtxt("temp.txt")
side=7
M=zeros(len(T))
mag=abs(data[-1000:-1,2])
for i in range(len(T)):
    M[i]=sum(mag)/(side*side)
figure()
plot(
    




