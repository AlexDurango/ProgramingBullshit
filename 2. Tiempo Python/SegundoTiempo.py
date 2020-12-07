import math

try:
    tiempo_prueba = input("¿Cuanto tiempo tienes?: ")
    numero_preguntas = int(input("¿Cuantas preguntas son?: "))

    while numero_preguntas < 1:
        numero_preguntas = int(input("¿Cuantas preguntas son?: "))

    
    unidades_horas = ["h", "horas", "hora"]
    unidades_minutos = ["min", "minutos"]

    def calcularTiempoPregunta(tiempo_prueba, numero_preguntas):

        tiempo_split = tiempo_prueba.split()     

        if len(tiempo_split) > 2:

            horas = int(tiempo_split[0])
            minutos = int(tiempo_split[2])

            if tiempo_split[3] in unidades_minutos:
                total_time = (horas*60) + minutos
                tiempo_por_pregunta = float(total_time)/float(numero_preguntas)
                segundos, minutos_enteros = math.modf(round(tiempo_por_pregunta,2))
                segundos *= 60

                if segundos >= 1:
                    print("Tienes " + str(int(minutos_enteros))+ " minutos y "+ str(round(segundos,2)) + " segundos por cada pregunta.")
                    return 
                else:
                    print("Tienes " + str(int(minutos_enteros))+ " minutos por cada pregunta.")
                    return 

        elif len(tiempo_split) < 2:
             
            if tiempo_split[1] in unidades_horas:
                horas = int(tiempo_split[0])
                horas *= 60
                tiempo_por_pregunta = float(horas)/float(numero_preguntas) 
                segundos, minutos_enteros = math.modf(round(tiempo_por_pregunta,2))
                segundos *= 60
                if segundos >= 1:
                    print("Tienes " + str(int(minutos_enteros))+ " minutos y "+ str(round(segundos,2)) + " segundos por cada pregunta.")
                    return 
                else:
                    print("Tienes " + str(int(minutos_enteros))+ " minutos por cada pregunta.")
                    return

            elif tiempo_split[1] in unidades_minutos:
                minutos = int(tiempo_split[0])
                tiempo_por_pregunta = float(minutos)/float(numero_preguntas)
                segundos, minutos_enteros = math.modf(round(tiempo_por_pregunta,2))
                segundos *= 60
                if segundos >= 1:
                    print("Tienes " + str(int(minutos_enteros))+ " minutos y "+ str(round(segundos,2)) + " segundos por cada pregunta.")
                    return 
                else:
                    print("Tienes " + str(int(minutos_enteros))+ " minutos por cada pregunta.")
                    return
    
    calcularTiempoPregunta(tiempo_prueba, numero_preguntas)
    input()
except:
    print("Datos erroneos") 

