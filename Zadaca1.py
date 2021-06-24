import random



names = ['Josip', 'Ivan', 'Ivan', 'Josip', 'Ivan', 'Ivan', 'Katarina', 'Božena', 'Ivona', 'Marija', 'Josipa', 'Marko', 'Dario', 'Mihael',
'Stana', 'Bruno', 'Anamarija', 'Andrea', 'Petar', 'Marko', 'Amnesa', 'Nikola', 'Antonela', 'Leon', 'Ivan', 'Ante', 'Ivan',
'Jure', 'Jan', 'Florijan', 'Boris', 'Ivan', 'Stipe', 'Damir', 'Ana', 'Tin', 'Iva', 'Kristina', 'Josip', 'Tomislav', 'Luka', 'Ivan',
'Martin', 'Marko', 'Ante', 'Nikolina', 'Ivan', 'Toni', 'Ante', 'Darija', 'Dominik', 'Lucija', 'Luka', 'Ana', 'Emanuel',
'Petar', 'Matej', 'Stjepan', 'Josip', 'Luka', 'Marija', 'Toni', 'Iva ', 'Perica', 'Antonio', 'Ante', 'Marijan', 'Mario',
'Antonio', 'Stipe', 'Filip', 'Ivan', 'Ivan', 'Luka', 'Ante Bruno', 'Ivan', 'Vinko', 'Ivan', 'Matijas', 'Ivan', 'Freda', 'Kristina',
'Josip', 'Lucija']

rjecnik = {}
ocjene = {}
zbroj = 0
prolazZbroj = 0
for i in names:
    rjecnik[i] = rjecnik.get(i,0)+1



for i in rjecnik:
    rjecnik[i] = random.randint(1,5)

print(rjecnik)

for value in rjecnik.values():
    ocjene[value] = ocjene.get(value, 0)+1

print(ocjene)


for ocjena in rjecnik.values():
    zbroj += ocjena
    if ocjena != 1:
        prolazZbroj += ocjena
print(zbroj)
print(prolazZbroj)

    
prosjek = (prolazZbroj/zbroj)*10
print(prosjek)

