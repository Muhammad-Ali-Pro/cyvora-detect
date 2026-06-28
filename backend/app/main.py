from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {
        "project": "Cyvora Detect",
        "status": "running",
        "version": "0.1.0"
    }