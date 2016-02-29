import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_pdf import PdfPages

# FIGURA 9
data=np.genfromtxt('fig9.dat')
fig9=plt.figure(figsize=(12,20))
plt.subplot(2,1,1)
plt.scatter(data[:,0],data[:,1],s=1,c='k')
plt.ylim((-2.5,2.5))
plt.xlim((-3,3))
plt.ylabel(r'$p_3$')
plt.xlabel(r'$q_3$')
plt.title(r'Figura 9 SIA')
plt.subplot(2,1,2)
plt.scatter(data[:,2],data[:,3],s=1,c='k')
plt.ylim((-2.5,2.5))
plt.xlim((-3,3))
plt.ylabel(r'$p_3$')
plt.xlabel(r'$q_3$')
plt.title(r'Figura 9 RK4')


#FIGURA 10
fig10=plt.figure(figsize=(12,20))
plt.subplot(2,1,1)
plt.scatter(data[:,0],data[:,1],s=1,c='k')
plt.ylim((-0.6,0.6))
plt.xlim((-2.4,-0.9))
plt.ylabel(r'$p_3$')
plt.xlabel(r'$q_3$')
plt.title(r'Figura 10 SIA')
plt.subplot(2,1,2)
plt.scatter(data[:,2],data[:,3],s=1,c='k')
plt.ylim((-0.35,0.35))
plt.xlim((-0.2,0.8))
plt.ylim((-1,1.5))
plt.xlim((-2.8,-0.8))
plt.ylabel(r'$p_3$')
plt.xlabel(r'$q_3$')
plt.title(r'Figura 10 RK4')


#FIGURA 11
fig11=plt.figure(figsize=(12,20))
plt.subplot(2,1,1)
plt.scatter(data[:,0],data[:,1],s=1,c='k')
plt.ylim((-0.35,0.35))
plt.xlim((-0.2,0.8))
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
plt.ylim((-2.5,2.5))
plt.xlim((-2,2))
plt.ylabel(r'$p_3$')
plt.xlabel(r'$q_3$')
plt.title(r'Figura 12')

#FIGURA 13
fig13=plt.figure(figsize=(10,10))
plt.scatter(data[:,0],data[:,1],s=1,c='k')
plt.ylim((-0.65,0.65))
plt.xlim((0.2,0.7))
plt.ylabel(r'$p_3$')
plt.xlabel(r'$q_3$')
plt.title(r'Figura 13')

#FIGURA 14
fig14=plt.figure(figsize=(10,10))
plt.scatter(data[:,0],data[:,1],s=1,c='k')
plt.ylim((-0.1,0.1))
plt.xlim((-0.08,0.08))
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
plt.subplot(2,1,1)
plt.plot(data[:,2],data[:,0],c='k')
plt.ylabel(r'E')
plt.xlabel(r'$t$')
plt.title(r'Traditional Integrator')
plt.subplot(2,1,2)
plt.plot(data[:,2],data[:,1],c='k')
plt.ylabel(r'E')
plt.xlabel(r'$t$')
plt.title(r'Symplectic Integrator')

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
