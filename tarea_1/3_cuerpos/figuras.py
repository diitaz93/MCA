import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_pdf import PdfPages

# FIGURA 9
data=np.genfromtxt('fig9.dat')
fig9=plt.figure(figsize=(12,20))
plt.subplot(2,1,1)
plt.scatter(data[:,0],data[:,1],s=1,c='k')
plt.ylabel(r'$p_3$')
plt.xlabel(r'$q_3$')
plt.title(r'Figura 9 SIA')
plt.subplot(2,1,2)
plt.scatter(data[:,2],data[:,3],s=1,c='k')
plt.ylabel(r'$p_3$')
plt.xlabel(r'$q_3$')
plt.title(r'Figura 9 RK4')


#FIGURA 10
data=np.genfromtxt('fig10.dat')
fig10=plt.figure(figsize=(12,20))
plt.subplot(2,1,1)
plt.scatter(data[:,0],data[:,1],s=1,c='k')
plt.ylabel(r'$p_3$')
plt.xlabel(r'$q_3$')
plt.title(r'Figura 10 SIA')
plt.subplot(2,1,2)
plt.scatter(data[:,2],data[:,3],s=1,c='k')
plt.ylabel(r'$p_3$')
plt.xlabel(r'$q_3$')
plt.title(r'Figura 10 RK4')


#FIGURA 11
data=np.genfromtxt('fig11.dat')
fig11=plt.figure(figsize=(12,20))
plt.subplot(2,1,1)
plt.scatter(data[:,0],data[:,1],s=1,c='k')
plt.ylabel(r'$p_3$')
plt.xlabel(r'$q_3$')
plt.title(r'Figura 11 SIA')
plt.subplot(2,1,2)
plt.scatter(data[:,2],data[:,3],s=1,c='k')
plt.ylabel(r'$p_3$')
plt.xlabel(r'$q_3$')
plt.title(r'Figura 11 RK4')


#FIGURA 12
data=np.genfromtxt('fig12.dat')
fig12=plt.figure(figsize=(10,10))
plt.scatter(data[:,0],data[:,1],s=1,c='k')
plt.ylabel(r'$p_3$')
plt.xlabel(r'$q_3$')
plt.title(r'Figura 12')

#FIGURA 13
data=np.genfromtxt('fig13.dat')
fig13=plt.figure(figsize=(10,10))
plt.scatter(data[:,0],data[:,1],s=1,c='k')
plt.ylabel(r'$p_3$')
plt.xlabel(r'$q_3$')
plt.title(r'Figura 13')

#FIGURA 14
data=np.genfromtxt('fig14.dat')

fig14=plt.figure(figsize=(10,10))
plt.scatter(data[:,0],data[:,1],s=1,c='k')
plt.ylabel(r'$p_3$')
plt.xlabel(r'$q_3$')
plt.title(r'Figura 14')

#FIGURA 15
data=np.genfromtxt('fig15.dat')
fig15=plt.figure(figsize=(10,10))
plt.scatter(data[:,0],data[:,1],s=1,c='k')
plt.ylabel(r'$p_3$')
plt.xlabel(r'$q_3$')
plt.title(r'Figura 15')

#FIGURA 16
data=np.genfromtxt('fig16.dat')
fig16=plt.figure(figsize=(10,10))
plt.scatter(data[:,0],data[:,1],s=1,c='k')
plt.ylabel(r'$p_3$')
plt.xlabel(r'$q_3$')
plt.title(r'Figura 16')

#FIGURA 17
data=np.genfromtxt('fig17.dat')
fig17=plt.figure(figsize=(15,15))
plt.subplot(2,2,1)
plt.plot(data[:,0],data[:,2],c='k')
plt.ylabel(r'E')
plt.xlabel(r'$t$')
plt.title(r'Symplectic Integrator, $\Delta E/E=$3.8547e-012')
plt.subplot(2,2,2)
plt.plot(data[:,1],data[:,3],c='k')
plt.ylabel(r'E')
plt.xlabel(r'$t$')
plt.title(r'Symplectic Integrator, $\Delta E/E=$1.3195e-07')
plt.subplot(2,2,3)
plt.plot(data[:,0],data[:,4],c='k')
plt.ylabel(r'E')
plt.xlabel(r'$t$')
plt.title(r'Traditional Integrator, $\Delta E/E=$5.7048e-005')
plt.subplot(2,2,4)
plt.plot(data[:,1],data[:,5],c='k')
plt.ylabel(r'E')
plt.xlabel(r'$t$')
plt.title(r'Traditional Integrator, $\Delta E/E=$0.079921')

#Guarda imagenes en un pdf
pdf=PdfPages('Figuras.pdf')
pdf.savefig(fig9)
pdf.savefig(fig10)
pdf.savefig(fig11)
pdf.savefig(fig12)
pdf.savefig(fig13)
pdf.savefig(fig14)
pdf.savefig(fig15)
pdf.savefig(fig16)
pdf.savefig(fig17)
pdf.close()
