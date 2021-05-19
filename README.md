# RedMetro
Tarea Red Metro para Buda.com

* Autor: Juan Fuentes
* Fecha: 18-05-2021
* Descripcion:
  > Encuentra el camino mas corto entre dos estaciones dadas.

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
  * Color Tren = Color de tren.
    * "w" si es blanco.
    * "g" si es verde.
    * "r" si es rojo.

## Salida:
  * Distancia mas corta entre la Estacion inicial y final.
  * Camino mas corto trazado por el tren.
