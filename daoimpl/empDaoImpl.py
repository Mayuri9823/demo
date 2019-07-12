from empFlaskCrud.dao.daoinfo import DAOContract
from empFlaskCrud.util.dbconfig import db
from empFlaskCrud.model.Empinfo import Employee

class EmpDImpl(DAOContract):

    def persistEntity(self, entity):
        db.session.add(entity)
        self.commitAndRemove()

    def removeEntity(self, entityID):
        db.session.delete(entityID)
        self.commitAndRemove()

    def fetchEntity(self, entityId):
        return Employee.query.filter_by(id=entityId).first()

    def fetchAllEntities(self):
        return Employee.query.all()

    def modifyEntity(self, entity):
        self.commitAndRemove()

    def commitAndRemove(self):
            db.session.commit()
            db.session.remove()