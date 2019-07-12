from abc import ABC,abstractmethod

class AppService(ABC):

    @abstractmethod
    def addEntity(self,entity):
        pass

    @abstractmethod
    def getEntity(self, entityId):
        pass

    @abstractmethod
    def deleteEntity(self, entityId):
        pass

    @abstractmethod
    def getAllEntities(self):
        pass

    @abstractmethod
    def updateEntity(self, entity):
        pass
