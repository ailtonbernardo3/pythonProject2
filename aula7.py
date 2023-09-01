

#listaTest=["rua","tel"]
#print(listaTest[0])
#listaTest[0]="pedro"
#print(listaTest[0])
#print("#"*30)


#lista=["rogerio","pedro","maria","joao"]

#for i in range(len(lista)):
    #lista[i]= lista[i].title()

    #print(lista)




#listaTest=["ailton","luiz","tiao"]

#listaTest[0]="ailton"
#print(listaTest[0])

#listaTest[0]="luiz"
#print(listaTest[0])

#listaTest[0]="tiao"
#print(listaTest[0])
#print("#"*10)

#test = ['Alice', 'Bob', 'Carol']

#print(" ", test)

#test[0] = 'Eve'

#test[1] = 'David'

#test[2] = 'Frank'

#print(" ", test)
#novalista2=[]
#novalista2.append("A")
#novalista2.append("B")
#novalista2.append("C")
#novalista2.append("D")
#novalista2.append("E")
#print(novalista2)
#print(novalista2.count("A"))
#print(novalista2.remove("D"))
#print(novalista2)
#print("seja bem vindo")
#print("voce precisa logar")
#nome:str= input("digite seu nome")
#senha:str= input("digite sua senha")
#if nome in ["pedro","maria","santos"] and senha =="1234":

   # while True:
   #     pass
##else:
    #print("nome ou senha nao exitem no sistema")






usuario=list()

while True:
    print("seja bem vindo!")
    print("#",20,"menu", "#"*20)
    print(""""para cadastra digite ->1
    para sair digite 2
    """)
    bnt=input("digte a opiçao desejada: ")

    if bnt=="1":
        nome:str= input("nome")
        rg:str= input("rg")
        ano_nasc: str = input("ano_nasc")

        tel1:str=input("digite seu telefone 1: ")
        tel2:str=input("digite seu telefone 2: ")
        telefones=[tel1,tel2]
        print("#" * 20, "cadastro de dispensas", "#" * 20)
        despesas=list()
        while True:
            descriçao:str=input("descriçao da despesa: ")
            valor=input("digite o valor R$ ")

            data_despesas=dummy_threading.date.today()
            despesas={"descriçao" :descriçao,"valor":valor,"date_desprsa":data_despesas}
            despesas.append(despesas)
            resposta=input("deseja continuar cadastrando sim ou nao: ".strip())



