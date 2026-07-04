from fastapi import FastAPI, UploadFile, File
from backend.app.parser.sigma_parser import parse_sigma_rule
from backend.app.validator.validator import validate_sigma_rule
from backend.app.scoring.risk_scoring import calculate_risk_score
from backend.app.scoring.mitre_mapper import map_to_mitre

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

    validation = validate_sigma_rule(parsed_rule)

    score = calculate_risk_score(parsed_rule)

    mitre = map_to_mitre(parsed_rule)

    return {
    "rule": parsed_rule,
    "validation": validation,
    "score": score,
    "mitre" : mitre
}