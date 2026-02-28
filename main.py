from fastapi import FastAPI, Path, HTTPException, Query
import json

app = FastAPI()

def load_data():
    with open("student_data.json",'r') as f:
        data = json.load(f)
    return data

@app.get("/home")
def home():
    return {"message":"hello"}

@app.get("/students")
def students():
    data = load_data()
    return data
    
@app.get("/students/{id}")
def student_by_id(id:str =  Path(...,description="enter the id of student", example="1")):
    data = load_data()
    
    if id in data:
        return data[id]

    return {"message":"student not found"}

@app.get("/sort")
def sort_students(sort_by:str = Query(...,description="enter the key to sort by form [age,cgpa]"), order:str = Query(...,description="enter the order to sort by form [asc,desc]")):
    data = load_data()

    if sort_by not in ["age", "cgpa"]:
        raise HTTPException(status_code=400, detail="Invalid sort key")
    
    if order not in ["asc", "desc"]:
        raise HTTPException(status_code=400, detail="Invalid order")
    
    sort_order = True if order == "desc" else False

    sorted_data = sorted(data.values(), key=lambda x: x.get(sort_by), reverse=sort_order)

    return sorted_data