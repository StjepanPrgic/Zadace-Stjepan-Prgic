import re

patternEmail = "(\w)+\.(\w)+@(\w)+\.(\w)+\.(\w)+"
patternEduId = "(\w)+(\d)?@(\w)+.(\w)+"



email = input("Unesite email: ")
eduId = input("Unesite eduId: ")

resultEmail = re.match(patternEmail, email)
resultEduId = re.match(patternEduId, eduId)

if resultEmail:
    print(resultEmail)
else:
    print("Pogresan email")

if resultEduId:
    print(resultEduId)
else:
    print("Pogresan eduId")
