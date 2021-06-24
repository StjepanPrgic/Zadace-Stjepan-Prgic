ime = input("Unesite ime: ")



def pozdrav(ime):
    return "Pozdrav", ime


x = lambda ime: "Dobrodosao " + ime



def func3(function, ime):
    return function(ime)


print(func3(pozdrav, ime))

