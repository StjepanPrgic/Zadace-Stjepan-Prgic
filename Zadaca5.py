def parniGenerator(broj):
    parniBroj = 2
    while parniBroj<broj:
        yield parniBroj
        parniBroj +=2

def neparniGenerator(broj):
    neparniBroj = 1
    while neparniBroj<broj:
        yield neparniBroj
        neparniBroj +=2


broj = int(input("Unesite broj: "))


for i in parniGenerator(broj):
    print(i)

for i in neparniGenerator(broj):
    print(i)

    
