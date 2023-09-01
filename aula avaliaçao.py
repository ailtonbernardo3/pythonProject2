# Inicializar a lista de tarefas vazia
tarefas = []

# Função para mostrar o menu
def mostrar_menu():
    print("\n===== Lista de Tarefas =====")
    print("1. Adicionar Tarefa")
    print("2. Listar Tarefas")
    print("3. Marcar Tarefa como Concluída")
    print("4. Sair do Sistema")
    print("============================")

# Loop principal do sistema
while True:
    mostrar_menu()
    escolha = input("Escolha uma opção: ")

    if escolha == '1':
        tarefa = input("Digite a tarefa que deseja adicionar: ")
        tarefas.append(tarefa)
        print(f"Tarefa '{tarefa}' adicionada com sucesso!")

    elif escolha == '2':
        print("\n===== Lista de Tarefas =====")
        for index, tarefa in enumerate(tarefas, start=1):
            print(f"{index}. {tarefa}")
        print("============================")

    elif escolha == '3':
        if len(tarefas) == 0:
            print("Não há tarefas para marcar como concluídas.")
        else:
            index = int(input("Digite o número da tarefa que deseja marcar como concluída: "))
            if 1 <= index <= len(tarefas):
                tarefa_concluida = tarefas.pop(index - 1)
                print(f"Tarefa '{tarefa_concluida}' marcada como concluída!")
            else:
                print("Número de tarefa inválido!")

    elif escolha == '4':
        print("Saindo do Sistema. Obrigado!")
        break

    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")
