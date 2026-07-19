from fastapi import FastAPI, UploadFile, File
from fastapi.responses import FileResponse

from backend.app.parser.sigma_parser import parse_sigma_rule
from backend.app.validator.validator import validate_sigma_rule
from backend.app.scoring.risk_scoring import calculate_risk_score
from backend.app.scoring.mitre_mapper import map_to_mitre
from backend.app.review.rule_review import review_sigma_rule
from backend.app.report.pdf_generator import generate_pdf_report

from backend.app.config import APP_NAME, APP_VERSION


app = FastAPI()


@app.get("/")
def root():
    return {
        "project": APP_NAME,
        "status": "running",
        "version": APP_VERSION
    }


@app.post("/upload")
async def upload_sigma_rule(file: UploadFile = File(...)):

    content = await file.read()

    parsed_rule = parse_sigma_rule(content)

    validation = validate_sigma_rule(parsed_rule)

    score = calculate_risk_score(parsed_rule)

    mitre = map_to_mitre(parsed_rule)

    review = review_sigma_rule(parsed_rule)

    return {
        "rule": parsed_rule,
        "validation": validation,
        "score": score,
        "mitre": mitre,
        "review": review
    }


@app.post("/report")
async def generate_report(file: UploadFile = File(...)):

    content = await file.read()

    parsed_rule = parse_sigma_rule(content)

    validation = validate_sigma_rule(parsed_rule)

    score = calculate_risk_score(parsed_rule)

    mitre = map_to_mitre(parsed_rule)

    review = review_sigma_rule(parsed_rule)

    report_data = {
        "rule": parsed_rule,
        "validation": validation,
        "score": score,
        "mitre": mitre,
        "review": review
    }

    output_path = "cyvora_report.pdf"

    generate_pdf_report(report_data, output_path)

    return FileResponse(
        output_path,
        media_type="application/pdf",
        filename="cyvora_report.pdf"
    )