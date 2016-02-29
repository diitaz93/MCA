##### Crea un pdf con las figuras
Figuras.pdf : dats
	python figuras.py
##### Borra archivos creados
.PHONY : clean
clean :
	rm *.x *.dat

##### Variable datos 
dats : fig9.dat fig12.dat fig15.dat fig16.dat fig17.dat

##### Datos Figura 9
9.x : fig9.c
	gcc $< -lm -o $@

fig9.dat : 9.x
	./$< > $@ 

##### Datos Figura 10
#10.x : fig10.c
#	gcc $< -lm -o $@
#fig10.dat : 10.x
#	./$< > $@ 

##### Datos Figura 11
#11.x : fig11.c
#	gcc $< -lm -o $@
#fig11.dat : 11.x
	./$< > $@

##### Datos Figura 12
12.x : fig12.c
	gcc $< -lm -o $@
fig12.dat : 12.x
	./$< > $@

##### Datos Figura 13
#13.x : fig13.c
#	gcc $< -lm -o $@
#fig13.dat : 13.x
#	./$< > $@

##### Datos Figura 14
#14.x : fig14.c
#	gcc $< -lm -o $@
#fig14.dat : 14.x
#	./$< > $@

##### Datos Figura 15
15.x : fig15.c
	gcc $< -lm -o $@
fig15.dat : 15.x
	./$< > $@

##### Datos Figura 16
16.x : fig16.c
	gcc $< -lm -o $@
fig16.dat : 16.x
	./$< > $@

##### Datos Figura 17
17.x : fig17.c
	gcc $< -lm -o $@
fig17.dat : 17.x
	./$< > $@
