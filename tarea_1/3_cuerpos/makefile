##### Crea un pdf con las figuras
Figuras.pdf : dats
	python figuras.py

##### Variable datos 
dats : fig9.dat fig10.dat

##### Datos Figura 9
9.x : fig9.c
	gcc fig9.c -lm -o $@

fig9.dat : 9.x
	./9.x > fig9.dat 

##### Datos Figura 10
10.x : fig10.c
	gcc fig10.c -lm -o $@
fig10.dat : 10.x
	./10.x > fig10.dat 


