def function(rijec):
    if len(rijec) == 1:
        return rijec
    else:
        return function(rijec[1:]) + rijec[0]


rijec = input("Unesite rijec: ")
print(function(rijec))
