#funçoes
#eu presiso calcular a media

valor1=4.5
valor2=7
valor3=8.5
media=(valor1+valor2+valor3)/3
print(media)


valores=[4,5,7,8,5]
media=sum(valores)/len(valores)
print(media)


# imagina q fazer media na minha empresa e um rostinho diria
# vou fazer essa açao de modo pratico
#se eu for criar uma funçao para o (metodo 1) posso fazer assin

#para criar uma finçao preciso suar a palavra reservada "def"
#o q vai entrar os parenteses e chamado de paramentro


def media(n1,n2,n3):
    if n1.isdingit() and n2.isdigit() and n3.isdingit():
        print((int(n1)+int(n2)+int(n3))/3)
    else:
        print("voce precisa digitar um valor inteiro")



n1=input("valor1 ")
n2=input("valor2 ")
n3=input("valor3 ")

media(n1,n2,n3)


media("56","45","112")

#criar
def soma(n1,n2,n3,n4):
    print(n1+n2+n3+n4)


#usar
soma(45,78,90,1)


#criar
def dividir(n1,n2):
    print(n1/n2)


#usar
dividir(5,109)

#==========================================================



