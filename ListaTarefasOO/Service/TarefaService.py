from Model.Tarefa import *
from datetime import datetime

class TarefaService:
    tarefas = []

    tarefa1  = Tarefa(1,"Estudar Python","ANDAMENTO")
    tarefas.append(tarefa1)

    def addTarefa(tarefa:Tarefa):
        TarefaService.tarefas.append(tarefa)
        print("Tarefa adicionada!!!")
    
    def listTarefas():
        for tarefa in TarefaService.tarefas:
            print("")
            print("ID:"+str(tarefa.getId()))
            print("Descricao:"+tarefa.getDescricao())
            print("Data:"+str(tarefa.getData()))
            print("Status:"+tarefa.getStatus())
            print("Ultima mod."+ str(tarefa.getUpdate()))
    
    def removeTarefa(id):
        for tarefa in TarefaService.tarefas:
            if(tarefa.getId()==id):
                respRemove=input(f"Certeza que deseja excluir a tarefa de ID {id}:").lower()
                if(respRemove=="s"):
                    TarefaService.tarefas.remove(tarefa)
                    print("Tarefa excluida com sucesso!!!!")
                    break

    def concludeTarefa(id):
        for tarefa in TarefaService.tarefas:
            if(tarefa.getId()==id):
                respRemove=input(f"Certeza que deseja Concluir a tarefa de ID {id}:").lower()
                if(respRemove=="s"):
                    tarefa.setStatus("CONCLUIDA")
                    print("Tarefa Concluída com sucesso!!!!")
                    break
    


    


       
        

        
        
