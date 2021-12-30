import uvicorn
from typing import Optional
from fastapi import FastAPI, Request

from pydantic import BaseModel
from fastapi.routing import APIRouter

app = FastAPI()

class emp(BaseModel):
    name: str
    id: int
    age: int
    address: str
    salary: int

@app.get("/")
def read_root():
     return {"Welcome Employee"}

@app.put("emp/{emp_id}")
def read_id(id: int,age: int, name:str, address:str, salary:int ):
    return {"id": id, "age":age, "name":name, "address":address, "salary":salary}

@app.post("emp/{emp_id}")
def create_id(id: int,age: int, name:str, address:str, salary:int ):
    return {"id": id, "age":age, "name":name, "address":address, "salary":salary}

@app.delete("emp/{emp_id}")
def delete_id(id:int):
    return app









