from empFlaskCrud.util.dbconfig import app,db
from empFlaskCrud.servimpl.empimpl import EmployeeImpl
from empFlaskCrud.controller.empcontroller import *
x=EmployeeImpl()
if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)