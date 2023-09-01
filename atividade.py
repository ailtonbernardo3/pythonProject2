#while True:
    #nome = input("Digite o seu nome: ")
    #idade = int(input("Digite a sua idade: "))

    #if idade >18:
        #print("entrou no sistema.")

        #break

#print("acabou o sistema")

#======================================================================)

#while True:
    #nome = input("Digite o nome do aluno: ")
    #idade = int(input("Digite a idade do aluno: "))

    #notas = []
    #for i in range(4):
       # nota = float(input(f"Digite a nota {i + 1} do aluno: "))
       # notas.append(nota)

   # media = sum(notas) / len(notas)

    #print(f"Média do aluno {nome}: {media:.2f}")

    #if media > 8:
       # print("Você foi aprovado!")
      #  break
    #else:
     #   print("Você não atingiu a média mínima. Por favor, tente novamente.\n")

#======================================================================================================#



#n="12"
#idade=input("digite a sua idade")

#nome=input("digite seu nome")
#print(nome.isalpha())

#numero_letra="23a45"
#print(numero_letra.isalpha())

#==================================================================================#

#def get_int_input(prompt):
    #while True:
        #try:
            #value = int(input(prompt))
            #return value
        #except ValueError:
            #print("Por favor, digite um valor inteiro válido.")


#def get_float_input(prompt):
    #while True:
        #try:
           # value = float(input(prompt))
            #return value
        #except ValueError:
 #           print("Por favor, digite um valor numérico válido.")


#def main():
#    nome = input("Digite o nome do aluno: ")
#    idade = get_int_input("Digite a idade do aluno: ")

#    notas = []
 #   for i in range(4):
  #      nota = get_float_input(f"Digite a {i + 1}ª nota: ")
   #     notas.append(nota)
#
 #   media = sum(notas) / len(notas)
  #  print(f"Média das notas: {media:.2f}")

   # if media > 8:
    #    print("Você foi aprovado!")
    #else:
     #   print("Sua média não atingiu o valor mínimo para aprovação.")


#if __name__ == "__main__":
 #   main()


#===================================================================================#


nome= input("digite seu nome")
idade=input("digite sua idade")

while not (nome.isalpha()and idade.isdigit()):
    print("vc digitetou seu nome ou sua idade errador")
    nome = input("digite seu nome")
    idade = input("digite sua idade")

while True:
    b1 = False
    b2 = False
    b3 = False
    b4 = False

    nota1 =input("digite sua nota: ")
    if str.isdigit(nota1.replace(".", "")) or str.isdigit(nota1.replace(",", "")):
        nota1= float(nota1.replace(".", "."))
        print("depois", nota1)
        b1=True


    nota2 =input("digite sua nota2: ")
    if str.isdigit(nota2.replace(".", "")) or str.isdigit(nota2.replace(",", "")):
        nota2= float(nota2.replace(".", "."))
        print("depois", nota2)
        b2=True
    else:
        b2= False

        nota3 = input("digite sua nota3: ")
        if str.isdigit(nota3.replace(".", "")) or str.isdigit(nota3.replace(",", "")):
            nota2 = float(nota3.replace(".", "."))
            print("depois", nota3)
            b3 = True
        else:
            b3 = False

        nota4 = input("digite sua nota4: ")
        if str.isdigit(nota4.replace(".", "")) or str.isdigit(nota4.replace(",", "")):
            nota4 = float(nota4.replace(".", "."))
            print("depois", nota4)
            b4 = True
        else:
            b4 = False