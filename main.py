from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Resume Optimizer App is running!"}
