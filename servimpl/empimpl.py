from empFlaskCrud.service.serviceinfo import AppService
from empFlaskCrud.model.Empinfo import Employee
from empFlaskCrud.daoimpl.empDaoImpl import EmpDImpl
class EmployeeImpl(AppService):
    empDaoImpl = EmpDImpl()

    def checkValidEntity(self,entity):
        if entity and type(entity) == Employee:
            return True
        return False

    def addEntity(self, entity):
        if self.checkValidEntity(entity):
            EmployeeImpl.empDaoImpl.persistEntity(entity)
            print('Employee Added Successfully....')
            return
        return "employee Not saved...!"

    def getEntity(self, entityId):
        if entityId and type(entityId)==int and entityId>0:
            dbEntity = EmployeeImpl.empDaoImpl.fetchEntity(entityId)
            if dbEntity:
                return dbEntity
        print('No object with given id present...!')
        return

    def deleteEntity(self, entityId):
        dbEntity = self.getEntity(entityId)
        if dbEntity:
            EmployeeImpl.empDaoImpl.removeEntity(dbEntity)
            print('Employee Deleted Successfully...')
            return

    def getAllEntities(self):
        listOfEmps = EmployeeImpl.empDaoImpl.fetchAllEntities()
        if (len(listOfEmps) > 0):
            return listOfEmps
        print('No employee records exists..')
        return

    def updateEntity(self, entity):
        if self.checkValidEntity(entity):
            dbEntity = self.getEntity(entity.id)
            if dbEntity:
                dbEntity.name=entity.name
                dbEntity.age=entity.age
                dbEntity.city =entity.city
                dbEntity.salary=entity.salary
                EmployeeImpl.empDaoImpl.modifyEntity(dbEntity)
                print('Employee info updated successfully...')
                return
        print('Employee info not updated...')
        return