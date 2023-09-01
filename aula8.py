lista=[1,2,3,4,2,3]
dupla=(1,2,3,4,2,3)
dicionario={"um":1,"dois":2,"tres":3}
conjunto={1,2,3,4,2,3}

print(f"lista: {lista}")
print(f"dupla: {dupla}")
print(f"dicionario: {dicionario}")
print(f"conjunto: {conjunto}")

tamanho=len(conjunto)

conjunto.add(4)
if len(conjunto)==tamanho:
    print("login ja existe!")

#criar um sistema que nao permita repetiçaodo login

login={"admin"}
while True:
    login=input("cadastre o seu login: ")
    tamanho=len(login)
    login.__add__(login)
    if len(login)!=tamanho:
        break
    else:
        print("esse login ja existe")

print(f"login:{login}")

print("#"*30)

conjunto2={23,45,67,80,80}
for valor in conjunto2:
    print(valor)

