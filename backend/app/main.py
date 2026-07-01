from fastapi import FastAPI, UploadFile, File
from backend.app.parser.sigma_parser import parse_sigma_rule

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

    content = await file.read()

    parsed_rule = parse_sigma_rule(content)

    return parsed_rule