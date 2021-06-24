from csv import reader

with open("rezultati.csv", "r") as read_obj:
    csv_reader = reader(read_obj)
    tuple1 = list(csv_reader)
    print(tuple1)

lista = []

for i in tuple1:
    if int(i[2]) >49:
        print(i)
    

for ime, prezime, bodovi in tuple1:
    lista.append((prezime, ime, bodovi))
lista.sort()
print(lista)


rjecnik = {"Nedovoljan": 0, "Dovoljan": 0, "Dobar": 0, "Vrlo dobar": 0, "Odlican": 0}

for i in lista:
    if int(i[2])<50:
        rjecnik["Nedovoljan"] +=1
    elif int(i[2])<66:
        rjecnik["Dovoljan"] +=1
    elif int(i[2])<81:
        rjecnik["Dobar"] +=1
    elif int(i[2])<91:
        rjecnik["Vrlo dobar"] +=1
    elif int(i[2])>90:
        rjecnik["Odlican"] +=1

print(rjecnik)
           
           
