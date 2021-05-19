#Programa red de metro Buda.com
#	Autor: Juan Fuentes
#	Fecha: 18-05-2021
#	Descripcion:
#		Encuentra el camino mas corto entre dos estaciones dadas.
#	Formato archivo de red:
#		G,I 				#1 linea: Estaciones verdes. Separadas por coma.
#		H 					#2 linea: Estaciones rojas. Separadas por coma.
#		A->B->C->D->E->F 	#Sig. lineas: Conexiones de la red. Separadas por "->"
#		C->G->H->I->F
#	Entrada usuario:
#		Estacion Inicial = 	Estacion desde donde empezamos a buscar (ej. A) (Case-sensitive).
#		Estacion Final = Estacion hacia donde queremos llegar (ej. F) (Case-sensitive).
#		Color Tren = Color de tren. "w" si es Blanco, "g" si es verde, o "r" si es rojo.
#	Salida:
#		Distancia mas corta entre la Estacion inicial y final.
#		Camino mas corto trazado por el tren.
#---------------------------------------------------------------------------------------------------

#Variables globales que guardan la mejor ruta y distancia encontrada.
BEST_PATH = [] #Lista tipo Station
BEST_DISTANCE = 999999

#Clase Station
#	Atributos de la clase:
#		name = Nombre estacion (ej. "A","B","C",...).
#		color = Color estacion ("w"=white,"g"=green,"r"=red).
#		connections = Array de tipo Station. Contiene todas las estaciones conectadas de la instancia.

class Station:
	def __init__(self, name,color):
		self.name = name
		self.color = color
		self.connections = [] 

#Funcion searchFinalStation(...)
#	Descripcion:
#		Busca el camino mas corto desde una estacion inicial hacia una final en una	red de metro dada.
#	Parametros:
#		ea = Estacion actual
#		ef = Estacion final
#		train_color = Color del tren ("w","g","r").
#		distance = Distancia recorrida hasta el momento.
#		station_list = Lista de tipo Station que contiene las Estaciones visitadas hasta el momento.
#	Salida:
#		Funcion Void
#		Modifica las variables globales BEST_DISTANCE and BEST_PATH a su valor optimo.

def searchFinalStation(ea,ef,train_color,distance,station_list):
	global BEST_DISTANCE
	global BEST_PATH

	distance = distance + 1
	station_list.append(ea) #Anadiendo a lista de estaciones visitadas

	#Si encontramos una mejor ruta, actualizamos BEST_PATH.
	if ea.name == ef.name:
		if distance < BEST_DISTANCE:
			BEST_DISTANCE = distance
			BEST_PATH = station_list
			return

	#Si un tren express pasa por una estacion de otro color, su distancia no se cuenta.
	if ((train_color == "g" and ea.color == "r") or 
		(train_color == "r" and ea.color == "g")):
		distance = distance - 1

	#Cada conexion de la estacion actual "ea" es un posible camino hacia "ef".
	for i in range(0,len(ea.connections)):
		isInStationList = False #La estacion ya fue recorrida?.
		for j in range(0,len(station_list)):			
			if ea.connections[i].name == station_list[j].name:
				isInStationList = True
		if not isInStationList: #Si no fue recorrida, entonces es un posible camino.
			searchFinalStation(ea.connections[i],ef,train_color,distance,station_list.copy())
	return

#Funcion redMetro(...)
#	Descripcion:
#		Inicializa variables y crea estaciones de la red de metro.
#	Parametros:
#		entrada_in = Nombre archivo de texto de entrada
#		ei_name_input = Nombre estacion inicial
#		ef_name_input = Nombre estacion final
#		train_color_input = Define color del tren ("w","g","r").
#	Salida:
#		Funcion Void
#		Imprime BEST_DISTANCE (num. estaciones recorridas) y BEST_PATH (camino mas corto).

def redMetro(entrada_in, ei_name_input, ef_name_input, train_color_input):
	global BEST_PATH
	global BEST_DISTANCE

	#0. Inicializa variables globales
	BEST_PATH = []
	BEST_DISTANCE = 999999

	#1. Inicializar variables y listas.
	all_stations = [] #Lista tipo Station. Contiene todas las estaciones de la red.
	green_stations = [] #Lista tipo str. Contiene el nombre de todas las est. verdes.
	red_stations = [] # Lista tipo str. Contiene el nombre de todas las est. rojas.

	#2. Procesar red de metro de archivo externo.
	file = open(entrada_in, "r")
	count_lines = 0
	for line in file:
		line = line.strip()
		if count_lines <= 1:
			#2.1. Clasificando Estaciones por colores
			lines = line.split(",")
			if count_lines == 0: #Primera linea: Est. Verdes
				for i in range(0,len(lines)):
					green_stations.append(lines[i])
			elif count_lines == 1: #Segunda linea: Est. Rojas
				for i in range(0,len(lines)):
					red_stations.append(lines[i])
			count_lines = count_lines + 1
		else:
			#2.2. Crear estaciones
			lines = line.split("->")		
			for i in range(0,len(lines)-1):
				#Si la estacion actual (i) existe, ocuparemos su informacion.
				index1 = -1
				for j in range(0,len(all_stations)):
					if all_stations[j].name == lines[i]:
						index1 = j
						break
				if index1 != -1: #La estacion ya existe.
					e1 = all_stations[j]
				else: #La estacion no existe, hay que crearla.
					e1 = Station(lines[i],"w")
					for j in range(0,len(green_stations)): 
						if e1.name == green_stations[j]: #Si es verde.
							e1.color = "g"
							break
					for j in range(0,len(red_stations)): 
						if e1.name == red_stations[j]: #Si es roja.
							e1.color = "r"
							break
					
				#Si la estacion siguiente (i+1) existe, ocuparemos su informacion.
				index2 = -1
				for j in range(0,len(all_stations)):
					if all_stations[j].name == lines[i+1]:
						index2 = j
						break
				if index2 != -1: #La estacion ya existe.
					e2 = all_stations[j]
				else: #La estacion no existe, hay que crearla.
					e2 = Station(lines[i+1],"w")
					for j in range(0,len(green_stations)):
						if e2.name == green_stations[j]: #Si es verde.
							e2.color = "g"
							break
					for j in range(0,len(red_stations)):
						if e2.name == red_stations[j]: #Si es roja.
							e2.color = "r"
							break

				#En este punto:
				# 	e1 es la estacion actual (i).
				# 	e2 es la estacion siguiente (i+1).

				#2.3. Creando conexion entre e1 y e2.
				#Creando la conexion e1->e2.
				connection = False
				for j in range(0,len(e1.connections)):
					if e1.connections[j].name == e2.name:				
						connection = True
						break
				if not connection:
					e1.connections.append(e2)

				#Creando la conexion e2->e1.
				connection = False
				for j in range(0,len(e2.connections)):
					if e2.connections[j].name == e1.name:				
						connection = True
						break
				if not connection:
					e2.connections.append(e1)

				#2.4. Anadir o reemplazar en all_stations.
				if index1 != -1:
					all_stations[index1] = e1
				else:
					all_stations.append(e1)	
				
				if index2 != -1:
					all_stations[index2] = e2
				else:
					all_stations.append(e2)

	#3.Ingreso datos usuario.
	ei_name = ei_name_input
	ef_name = ef_name_input
	train_color = train_color_input

	#4. Validacion de datos.
	#4.1. Busqueda de la estacion inicial en el registro all_stations.
	ei_index = -1
	for i in range(0,len(all_stations)):
		if all_stations[i].name == ei_name:
			ei_index = i
	if ei_index == -1:
		print("Error: Estacion inicial no existe")
		return

	#4.2. Busqueda de la estacion final en el registro all_stations.
	ef_index = -1
	for i in range(0,len(all_stations)):
		if all_stations[i].name == ef_name:
			ef_index = i
	if ef_index == -1:
		print("Error: Estacion final no existe")
		return

	#4.3. El tren no puede llegar a destino si:
	#		a) El tren es verde y la estacion final es roja.
	#		b) El tren es rojo y la estacion final es verde.
	if ((train_color == "g" and all_stations[ef_index].color == "r") or
		(train_color == "r" and all_stations[ef_index].color == "g")):
		print("Error: El tren no puede llegar a destino, ya que la estacion es de otro color.")
		print("Color Tren: "+ train_color + ". Color estacion final: "+all_stations[ef_index].color+".")
		return	

	#5. Busqueda
	ei = all_stations[ei_index]
	ef = all_stations[ef_index]
	station_list = []
	searchFinalStation(ei,ef,train_color,0,station_list.copy())

	#6. Limpiar BEST_PATH si el tren es de color.
	FINAL_BEST_PATH = []
	if train_color == "g":
		#Si el tren es verde, tenemos que eliminar los rojos.
		for i in range(0,len(BEST_PATH)):
			isThere = False
			for j in range(0,len(red_stations)):
				if BEST_PATH[i].name == red_stations[j]:
					isThere = True
			if not isThere:
				FINAL_BEST_PATH.append(BEST_PATH[i])
	elif train_color == "r":
		#Si el tren es rojo, tenemos que eliminar los verdes.
		for i in range(0,len(BEST_PATH)):
			isThere = False
			for j in range(0,len(green_stations)):
				if BEST_PATH[i].name == green_stations[j]:
					isThere = True
			if not isThere:
				FINAL_BEST_PATH.append(BEST_PATH[i])
	else:
		#Si el tren es blanco, no hay necesidad de eliminar estaciones.
		FINAL_BEST_PATH = BEST_PATH
		
	#7. Resultados
	print(" ")
	print("Entrada: "+ entrada_in)
	print("Color Tren: " + train_color)
	print("Num. estaciones recorridas: " + str(BEST_DISTANCE))
	for i in range(0,len(FINAL_BEST_PATH)):
		if i < len(FINAL_BEST_PATH)-1:
			print(FINAL_BEST_PATH[i].name + "->",end='')
		else:
			print(FINAL_BEST_PATH[i].name)
	return

# Funcion debug_print_stations()
#	Descripcion:
#		(DEBUG) Imprime informacion de cada estacion: Su nombre, color y conexiones.
# 	Parametros:
#		all_station = Lista con todas las estaciones y conexiones de la red.
#	Salida:
#		Funcion Void.

def debug_print_stations(all_stations):
	for i in range(0,len(all_stations)):
		print(" ")
		print("Estacion:")
		print("Nombre: "+ all_stations[i].name+". Color: "+all_stations[i].color+".")
		print("Conexiones:")
		for j in range(0,len(all_stations[i].connections)):
			if j < len(all_stations[i].connections)-1:
				print(all_stations[i].connections[j].name+ ", ",end='')
			else:
				print(all_stations[i].connections[j].name+ ".")			
	return

#---------------------------------------------------------------------------------------------------

#Test
#Test 1
entrada_in="entrada1.in" #Ejemplo "Tarea Buda.com - Metro" 
ei_name_input = "A"
ef_name_input = "F"
train_color_input = "w"
redMetro(entrada_in,ei_name_input,ef_name_input,train_color_input)

entrada_in="entrada1.in"
ei_name_input = "A"
ef_name_input = "F"
train_color_input = "r"
redMetro(entrada_in,ei_name_input,ef_name_input,train_color_input)

entrada_in="entrada1.in"
ei_name_input = "A"
ef_name_input = "F"
train_color_input = "g"
redMetro(entrada_in,ei_name_input,ef_name_input,train_color_input)

#Test 2
entrada_in="entrada2.in" #Ejemplo propio (ver red2.png)
ei_name_input = "M"
ef_name_input = "H"
train_color_input = "w"
redMetro(entrada_in,ei_name_input,ef_name_input,train_color_input)

entrada_in="entrada2.in"
ei_name_input = "M"
ef_name_input = "H"
train_color_input = "r"
redMetro(entrada_in,ei_name_input,ef_name_input,train_color_input)

entrada_in="entrada2.in"
ei_name_input = "M"
ef_name_input = "H"
train_color_input = "g"
redMetro(entrada_in,ei_name_input,ef_name_input,train_color_input)

#Input Manual
'''
entrada_in="entrada2.in"
ei_name_input = input("Ingrese Estacion Inicial: ") #ej. "A","B","C",...
ef_name_input = input("Ingrese Estacion Final: ") #ej. "A","B","C",...
train_color_input = input("Ingrese Color de Tren: ") #ej. "w"(white),"g"(green),"r"(red).
redMetro(entrada_in,ei_name_input,ef_name_input,train_color_input)
'''