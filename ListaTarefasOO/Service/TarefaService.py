from Model.Tarefa import Tarefa
from datetime import datetime

tarefas = []
proximo_id = 1

# Tarefa inicial
tarefa1 = Tarefa(proximo_id, "Estudar Python", "ANDAMENTO")
tarefas.append(tarefa1)

proximo_id += 1


def add_tarefa(desc):
    global proximo_id
    nova_tarefa= Tarefa(proximo_id,desc,"ANDAMENTO")
    proximo_id+=1
    tarefas.append(nova_tarefa)
    print("Tarefa adicionada !!!")


def list_tarefas():

    if not tarefas:
        print("Nenhuma tarefa cadastrada!")
        return

    for tarefa in tarefas:
        print("\n------------------")
        print("ID:"+str(tarefa.getId()))
        print("Descrição:"+ tarefa.getDescricao())
        print("Data:"+str(tarefa.getData()))
        print("Status:"+ tarefa.getStatus())
        print("Última mod.:"+str(tarefa.getUpdate()))


def remove_tarefa(id_tarefa):

    for tarefa in tarefas:

        if tarefa.getId() == id_tarefa:

            resp_remove = input(f"Certeza que deseja excluir a tarefa de ID {id_tarefa}? (s/n): ").lower()

            if resp_remove == "s":
                tarefas.remove(tarefa)
                print("Tarefa excluída com sucesso!")
                global proximo_id
                proximo_id-=1

            return

    print("Tarefa não encontrada!")


def conclude_tarefa(id_tarefa):

    for tarefa in tarefas:

        if tarefa.getId() == id_tarefa:

            resp_conclude = input(f"Certeza que deseja concluir a tarefa de ID {id_tarefa}? (s/n):").lower()

            if resp_conclude == "s":

                tarefa.setStatus("CONCLUIDA")

                # Atualiza data de modificação
                tarefa.setUpdate(datetime.now())

                print("Tarefa concluída com sucesso!")

            return

    print("Tarefa não encontrada!")