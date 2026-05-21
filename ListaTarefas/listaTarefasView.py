
from datetime import datetime


id=1
escolha=0
tarefas=[]

#Tarefa Teste
tarefa1 = { 
    'id':id,
    'descricao':"Formatar Computador",
    'status':"ANDAMENTO",
    'data':datetime.now(),
    'update':datetime.now()
    }

tarefas.append(tarefa1)
id+=1

def addTarefa():
     global id
     print("")
     descricao = input("Desc:")
     data = datetime.now()
     update = datetime.now()
     
     nova_Tarefa = { #Cria o Dicionário
         'id':id,
         'descricao':descricao,
         'status':"ANDAMENTO",
         'data':data,
         'update':update
         }
     
     tarefas.append(nova_Tarefa) #Adiciona o dicionário na lista
     
     print("Tarefa adicionada com sucesso!!!")
     id+=1

def listarTarefas():
    
    for tarefa in tarefas:
        idTarefa = tarefa['id']
        descTarefa = tarefa['descricao']
        statusTarefa = tarefa['status']
        dataTarefa = tarefa['data']
        updateTarefa = tarefa['update']
        
        print("")
        print("ID:"+str(idTarefa))
        print("Descricao:"+descTarefa)
        print("Status:"+statusTarefa)
        print("Data:"+str(dataTarefa))
        print("Ultimo Update:"+str(updateTarefa))
        print("")

def excluirTarefa():
    idExclusao = int(input("Digite o ID para exclusão:"))
    resp=""
    for tarefa in tarefas: 
        global id
        
        if (tarefa['id']==idExclusao):
            resp = input((f"Certeza que deseja exlcuir a tarefa com ID:{idExclusao}?(S/N):")).lower()
        
        if(resp=="s"):
            tarefas.remove(tarefa)
            id-=1
            print("Tarefa Excluída com sucesso!!!\n")
            return
        
            
def concluirTarefa():
    idConcluir=int(input(("Digite o id da tarefa que deseja Concluir:")))
    
    
    for tarefa in tarefas:
        if (tarefa['id']==idConcluir):
            respConcluir = input(f"Concluir a tarefa de ID {idConcluir}?:").lower()
            
            if(respConcluir=="s"):
                tarefa['status']="CONCLUÍDA"
                tarefa['update']=datetime.now()
                print("Tarefa Concluída com sucesso!!")
                return 
        
    
while True:
     if(escolha==6):
         break
     if(escolha>5):
         print("Insira um valor válido!!!!")
         
     print("-------Menu-------\n")
     print("1.Adicinar\n")
     print("2.Listar\n")
     print("3.Excluir\n")
     print("4.Concluir\n")
     print("5.Sair")
     print("---------------------")
     escolha=int(input("Escolha:"))
        
     match escolha:
         case 1:
          addTarefa() 
          
         case 2:
          listarTarefas()
          
         case 3:
          excluirTarefa()
             
         case 4:
          concluirTarefa()
         
         case 5:
             print("FIM!!")
