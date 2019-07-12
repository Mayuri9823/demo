from abc import ABC,abstractmethod

class DAOContract(ABC):

    @abstractmethod
    def persistEntity(self,entity):
        pass

    @abstractmethod
    def removeEntity(self,entityID):
        pass

    @abstractmethod
    def fetchEntity(self,entityId):
        pass

    @abstractmethod
    def fetchAllEntities(self):
        pass

    @abstractmethod
    def modifyEntity(self,entity):
        pass