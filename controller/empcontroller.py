from empFlaskCrud.constants.Appconstants import *
from empFlaskCrud.util.dbconfig import app
from flask import render_template, request as req
from empFlaskCrud.model.Empinfo import Employee
from empFlaskCrud.servimpl.empimpl import EmployeeImpl

serviceImpl = EmployeeImpl()


@app.route("/employee/",methods=["GET"])
def getemployeeLandingPage():
    return  render_template("employee.html",Emplist=serviceImpl.getAllEntities(),entity=dummyEntity())


@app.route("/save/",methods=["POST"])
def saveemployeeInfo():


    emp = Employee(id=int(req.form['EmpId']), name=req.form['Empname'], age=req.form['EmpAge'],city=req.form['Empcity'], salary=req.form['EmpSalary'])
    if int(req.form['EmpId']) > 0:
        serviceImpl.updateEntity(emp)
    else:
        serviceImpl.addEntity(emp)
    return render_template("employee.html", msg= EMPLOYEE_SAVED_SUCCESS, Emplist=serviceImpl.getAllEntities(),
                           entity=dummyEntity())

@app.route("/editemp/<id>",methods=["GET"])
def editEmployee(id):
    print('inside edit employee ',id)
    id=int(id)
    return render_template("employee.html", Emplist=serviceImpl.getAllEntities(),entity = serviceImpl.getEntity(id))

@app.route("/deleteemp/<id>",methods=["GET"])
def deleteCustomer(id):
    print('inside delete employee ', id)
    serviceImpl.deleteEntity(int(id))
    return render_template("employee.html", Emplist=serviceImpl.getAllEntities(),entity=dummyEntity())


def dummyEntity():
    return Employee(id=0,name="",age="",city="",salary="")
