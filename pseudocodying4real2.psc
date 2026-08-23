	Algoritmo administrador_academico
			
			Escribir "===== SISTEMA DE GESTIÓN ACADÉMICA ====="
			
			Repetir
				Escribir "Ingrese la cantidad de estudiantes a registrar:"
				Leer n
			Hasta Que n >= 1
			
			Repetir
				Escribir "Ingrese cantidad de componentes a evaluar (5-7):"
				Leer num_componentes
			Hasta Que num_componentes >= 5 Y num_componentes <= 7
			
			Dimension nombres[n], areas[n], carreras[n]
			Dimension componentes[num_componentes]
			Dimension notas[n, num_componentes]
			Dimension promedios[n]
			
			Para j <- 1 Hasta num_componentes Hacer
				Repetir
					Escribir "Nombre del componente ", j, ":"
					Leer componentes[j]
				Hasta Que componentes[j] <> ""
			FinPara
			
			Para i <- 1 Hasta n Hacer
				Escribir ""
				Escribir "--- Registrando estudiante N°", i, " ---"
				
				Repetir
					Escribir "Nombre:"
					Leer nombres[i]
				Hasta Que nombres[i] <> ""
				
				Repetir
					Escribir "Área (1-Ciencias y Tecnología, 2-Salud, 3-Humanidades):"
					Leer opc
					Segun opc Hacer
						1: areas[i] <- "Ciencias y Tecnología"
						2: areas[i] <- "Salud"
						3: areas[i] <- "Humanidades"
					FinSegun
				Hasta Que opc >= 1 Y opc <= 3
				
				Repetir
					Escribir "Carrera:"
					Leer carreras[i]
				Hasta Que carreras[i] <> ""
				
				Escribir "--- Ingreso de notas ---"
				suma_ind <- 0
				Para j <- 1 Hasta num_componentes Hacer
					Repetir
						Escribir "Nota de ", componentes[j], " (0-100):"
						Leer notas[i, j]
					Hasta Que notas[i, j] >= 0 Y notas[i, j] <= 100
					suma_ind <- suma_ind + notas[i, j]
				FinPara
				
				promedios[i] <- suma_ind / num_componentes
			FinPara
			
			suma_grupal <- 0
			nota_max <- notas[1, 1]
			nota_min <- notas[1, 1]
			ind_mejor <- 1
			
			Para i <- 1 Hasta n Hacer
				suma_grupal <- suma_grupal + promedios[i]
				
				Si promedios[i] > promedios[ind_mejor] Entonces
					ind_mejor <- i
				FinSi
				
				Para j <- 1 Hasta num_componentes Hacer
					Si notas[i, j] > nota_max Entonces
						nota_max <- notas[i, j]
					FinSi
					Si notas[i, j] < nota_min Entonces
						nota_min <- notas[i, j]
					FinSi
				FinPara
			FinPara
			
			promedio_grupal <- suma_grupal / n
			
			Escribir ""
			Escribir "==================== LISTADO FINAL ===================="
			
			Para i <- 1 Hasta n Hacer
				Escribir "Estudiante: ", nombres[i], " | Área: ", areas[i], " | Carrera: ", carreras[i]
				Para j <- 1 Hasta num_componentes Hacer
					Escribir "   ", componentes[j], ": ", notas[i, j]
				FinPara
				Escribir "   >> Promedio individual: ", promedios[i]
				
				Si i = ind_mejor Entonces
					Escribir "   *** MEJOR PROMEDIO DEL GRUPO ***"
				FinSi
				Escribir "---------------------------------------------------------"
			FinPara
			
			Escribir ""
			Escribir "Promedio general del grupo: ", promedio_grupal
			Escribir "Nota MÁXIMA del grupo: ", nota_max
			Escribir "Nota MÍNIMA del grupo: ", nota_min
			Escribir "Estudiante con mejor promedio: ", nombres[ind_mejor]
			
			
			
	FinAlgoritmo
		