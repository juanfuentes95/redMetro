# RedMetro
Tarea Red Metro para Buda.com programada en Python v3.9 64bit.

* Autor: Juan Fuentes
* Fecha: 18-05-2021
* Descripcion:
  > Encuentra el camino mas corto entre dos estaciones de una red dada.

## Uso
Ejecutar archivo "tarea.py" con Python 3. 

El archivo contiene test automáticos con los archivos de entrada "entrada1.txt" (ejemplo enviado en la tarea) y "entrada2.txt" (ejemplo propio, ver red2.png).

El archivo también posee una porción de código comentada para el ingreso manual de datos de entrada:

```python
#Input Manual
'''
entrada_in="entrada2.in"
ei_name_input = input("Ingrese Estacion Inicial: ") #ej. "A","B","C",...
ef_name_input = input("Ingrese Estacion Final: ") #ej. "A","B","C",...
train_color_input = input("Ingrese Color de Tren: ") #ej. "w"(white),"g"(green),"r"(red).
redMetro(entrada_in,ei_name_input,ef_name_input,train_color_input)
'''
```

## Formato de archivo de entrada

```python
G,I               #1 linea: Estaciones verdes. Separadas por coma.
H                 #2 linea: Estaciones rojas. Separadas por coma.
A->B->C->D->E->F  #Sig. lineas: Conexiones de la red. Separadas por "->"
C->G->H->I->F
```

## Entrada usuario:
  * Estacion Inicial = 	Estacion desde donde empezamos a buscar (ej. A) (Case-sensitive).
  * Estacion Final = Estacion hacia donde queremos llegar (ej. F) (Case-sensitive).
  * Color Tren = Color de tren (Case-sensitive).
    * "w" si es blanco.
    * "g" si es verde.
    * "r" si es rojo.

## Salida:
  * Distancia mas corta entre la Estacion inicial y final.
  * Camino mas corto trazado por el tren.
