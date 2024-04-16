Algoritmo matriz1
	Dimension matriz[4,4] //declaramos matriz de 3 filas y 4 columnas
	para i=0 Hasta 2 Con Paso 1 //ciclo para las filas
		para j=0 Hasta 3 Con Paso 1 //ciclo para las celdas de cada fila
			matriz[i,j]=Aleatorio(10,99)
			Escribir matriz[i,j] ,"|"Sin Saltar
			valor=valor+1
		FinPara
		Escribir ""
	FinPara
FinAlgoritmo