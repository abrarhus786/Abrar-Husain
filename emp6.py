from enum import Enum

from fastapi import FastAPI

class Employee(str, Enum):
    vaquar = "101"
    mohsin = "102"
    abrar = "103"
app = FastAPI()
@app.get("/")
async def get_name(emp: Employee):
    if emp == Employee.vaquar:
        return {"ID":101,"Name": "Vaquar", "Age":34, "Salary":5000}
    if emp == Employee.mohsin:
        return {"ID":102,"Name": "Mohsin", "Age": 32, "Salary": 5000}
    if emp == Employee.abrar:
        return {"ID":103,"Name": "Abrar", "Age": 26, "Salary": 1000}

