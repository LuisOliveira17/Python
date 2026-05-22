from Model.Tarefa import *
from View.Menu import *
import Service.TarefaService as tarefa_service

while True:
    Menu.mostrar()

    try:
        escolha = int(input("Escolha: "))
    except ValueError:
        print("Digite um número válido!")
        continue

    match escolha:
        case 1:
           descricao = input("Desc: ")
           tarefa_service.add_tarefa(descricao)
        case 2:
            tarefa_service.list_tarefas()
        case 3:
            idExcluir = int(input("Digite o ID para excluir:"))
            tarefa_service.remove_tarefa(idExcluir)
        case 4:
            idConcluir = int(input("Digite o ID para concluir:"))
            tarefa_service.conclude_tarefa(idConcluir)
        case 5:
            print("PROGRAMA FINALIZADO!")
            break
        case _:
            print("Opção inválida!")


    



