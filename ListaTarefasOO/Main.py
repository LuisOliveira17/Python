from Model.Tarefa import *
from View.Menu import *
from Service.TarefaService import *

class Main:
    idTarefa=2

    def execTarefa():
        descTarefa = input("Desc:")
        novaTarefa = Tarefa(Main.idTarefa,descTarefa,"ANDAMENTO")
        TarefaService.addTarefa(novaTarefa)
        Main.idTarefa+=1
    
    def execExcluirTarefa():
        idExcluir = int(input("Digite o ID para excluir:"))
        TarefaService.removeTarefa(idExcluir)
        Main.idTarefa-=1

    def execConcludeTarefa():
        idConcluir = int(input("Digite o ID para concluir:"))
        TarefaService.concludeTarefa(idConcluir)
        



while True:
    Menu.mostrar()

    try:
        escolha = int(input("Escolha: "))
    except ValueError:
        print("Digite um número válido!")
        continue

    match escolha:
        case 1:
            Main.execTarefa()
        case 2:
            TarefaService.listTarefas()
        case 3:
            Main.execExcluirTarefa()
        case 4:
            Main.execConcludeTarefa()
        case 5:
            print("PROGRAMA FINALIZADO!")
            break
        case _:
            print("Opção inválida!")


    



