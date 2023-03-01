hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))


minsT=  mins + dura + (60*hour)
# Write your code here.
horasT =
minutos = mins + dura

rest = minutos % 60
horas = int(hour + (dura+rest)/60) 
horast = int((horas+rest)/12) 
#val =(mins // 60)

# 1print(rest)
# print("O evento começou às ", hour, ":", mins," com a duração de ", dura, " minutos", sep="")
# print("O evento terminou às ", horas, ":", rest, sep="")
# print(horast)
print(minsT)