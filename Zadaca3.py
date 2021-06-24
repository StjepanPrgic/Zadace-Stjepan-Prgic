import re


pattern = "(\w),\s[0-5],\s(\w)"

rijec = input("Unesite string u formatu prvo slovo imena, broj 0-5, zadnje slovo prezimena")

result = re.match(pattern, rijec)

if result:
    print(result)
else:
    print("Pogresan unos")
