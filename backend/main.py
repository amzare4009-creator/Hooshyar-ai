from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {
        "project" : "Hooshyar AI" ,
        "version" : "0.1",
        "message" : "Welcome to Hooshyar AI"
    }