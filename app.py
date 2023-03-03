hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))
# Write your code here.

Totalmins=   mins + dura + (60*hour) #Transforma tudo em minutos

hr = (Totalmins//60) % 24 #encontra o total de horas de 0 a 23

min = (Totalmins - (hr*60)) % 60 #encontra o total de minutos de 0 a 59

print("O evento começou às ", hour, ":", mins," com a duração de ", dura, " minutos", sep="")
print("O evento terminou às ", hr, ":", min, sep="")
