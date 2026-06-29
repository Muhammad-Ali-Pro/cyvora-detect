from fastapi import FastAPI, UploadFile, File

app = FastAPI()


@app.get("/")
def root():
    return {
        "project": "Cyvora Detect",
        "status": "running",
        "version": "0.1.0"
    }


@app.post("/upload")
async def upload_sigma_rule(file: UploadFile = File(...)):
    return {
        "filename": file.filename,
        "message": "Sigma rule uploaded successfully."
    }