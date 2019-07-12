from empFlaskCrud.util.dbconfig import db


class Employee(db.Model): # this cls is a child of db.model .. sqlalchemy--orm
    id = db.Column('Emp_ID', db.Integer, primary_key=True)
    name = db.Column('Emp_Name', db.String(100))
    age = db.Column('Emp_Age', db.Integer)
    city = db.Column('Emp_', db.String(200))
    salary = db.Column('Emp_Salary', db.Integer)
print("entered from git")

