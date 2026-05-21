from datetime import datetime

class Tarefa:

    def __init__(self, id, descricao, status):
        self.id = id
        self.descricao = descricao
        self.status = status
        self.data = datetime.now()
        self.update = datetime.now()

    def getId(self):
        return self.id

    def setId(self, id):
        self.id = id

    def getDescricao(self):
        return self.descricao

    def setDescricao(self, descricao):
        self.descricao = descricao
        self.update = datetime.now()

    def getData(self):
        return self.data

    def getUpdate(self):
        return self.update
    

