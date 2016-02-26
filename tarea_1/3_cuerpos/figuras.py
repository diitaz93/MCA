import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_pdf import PdfPages

# FIGURA 9
data=np.genfromtxt('fig9.dat')
fig9=plt.figure(figsize=(10,10))
plt.scatter(data[:,0],data[:,1],s=1,c='k')
plt.ylabel(r'$p_3$')
plt.xlabel(r'$q_3$')
plt.title(r'Figura 9')

#FIGURA 10
data=np.genfromtxt('fig10.dat')
fig10=plt.figure(figsize=(10,10))
plt.scatter(data[:,0],data[:,1],s=1,c='k')
plt.ylabel(r'$p_3$')
plt.xlabel(r'$q_3$')
plt.title(r'Figura 10')

#FIGURA 11

#FIGURA 12

#FIGURA 13

#FIGURA 14

#FIGURA 15

#FIGURA 16

#FIGURA 17

#Guarda imagenes en un pdf
pdf=PdfPages('Figuras.pdf')
pdf.savefig(fig9)
pdf.savefig(fig10)
pdf.close()
