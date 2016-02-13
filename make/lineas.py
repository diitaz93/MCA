filein=open("numeros.txt", "r")
lineas=filein.readlines()
n_lineas=len(lineas)

fileout=open("lineas_1.txt","w")
fileout.write("{}".format(n_lineas))
fileout.close()

fileout=open("lineas_2.txt","w")
fileout.write("{}".format(n_lineas))
fileout.close()
