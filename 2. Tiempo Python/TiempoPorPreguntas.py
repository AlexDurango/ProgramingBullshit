
import math 

minutos = 0
tiempo = input("¿Cuanto tiempo tienes para la prueba?: ")
tiempo_split = tiempo.split()
numero_preguntas = int(input("¿Cuantas preguntas son?: "))


if numero_preguntas == 0 or len(tiempo_split) <= 1:
    print("Datos erroneos, intentalo de nuevo.")

elif tiempo_split[1] == 'h' or tiempo_split[1] == 'horas' or tiempo_split[1] == 'hora':

    hours_in_min = int(tiempo[0]) * 60

    if len(tiempo_split) > 2 and numero_preguntas != 0:

        if (int(tiempo_split[2]) > 59):
            print("Datos erroneos, intentalo de nuevo.")

        minutos = int(tiempo_split[2])
        total_time = hours_in_min + minutos
        time_per_question = float(total_time)/float(numero_preguntas)
        seconds, entire_minutes = math.modf(round(time_per_question,2))
        seconds = seconds * 60
        if seconds >= 1 :
            print ("Tienes " + str(int(entire_minutes))+ " minutos y "+ str(round(seconds,2)) + " segundos por cada pregunta.")
        else:
            print ("Tienes " + str(int(entire_minutes))+ " minutos por cada pregunta.")


    else:
        total_time = hours_in_min 
        time_per_question = float(total_time)/float(numero_preguntas)
        print ("Tienes " + str(int(time_per_question))+ " minutos por cada pregunta.")

elif tiempo_split[1] == 'min' or tiempo_split[1] == 'minutos':

    minutos_enteros = int(tiempo_split[0])
    time_per_question = float(minutos_enteros)/float(numero_preguntas)
    seconds, entire_minutes = math.modf(round(time_per_question,2))
    seconds *= 60
    if seconds >= 1 :
        print ("Tienes " + str(int(entire_minutes))+ " minutos y "+ str(round(seconds,2)) + " segundos por cada pregunta.")
    else:
        print ("Tienes " + str(int(entire_minutes))+ " minutos por cada pregunta.")


input()

    