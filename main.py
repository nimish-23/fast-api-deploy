from fastapi import FastAPI

app = FastAPI()

@app.get("/home")
def home():
    return {"message":"hello"}

@app.get("/about")
def about():
    return {"message":"about"}
