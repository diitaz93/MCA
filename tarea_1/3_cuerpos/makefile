##### Crea un pdf con las figuras
Figuras.pdf : dats
	python figuras.py

##### Variable datos 
dats : fig9.dat fig10.dat

##### Datos Figura 9
9.x : fig9.c
	gcc $< -lm -o $@

fig9.dat : 9.x
	./$< > $@ 

##### Datos Figura 10
10.x : fig10.c
	gcc $< -lm -o $@
fig10.dat : 10.x
	./$< > $@ 

##### Datos Figura 11
11.x : fig11.c
	gcc $< -lm -o $@
fig11.dat : 11.x
	./$< > $@

