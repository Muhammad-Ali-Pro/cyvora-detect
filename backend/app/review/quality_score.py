def calculate_quality_score(missing_fields):

    score = 100

    deductions = {
        "Missing title": 5,
        "Missing description": 10,
        "Missing author": 10,
        "Missing logsource product": 10,
        "Missing detection condition": 25,
        "Missing level": 10,
        "Missing false positives": 15,
        "Missing tags": 15,
    }

    for field in missing_fields:
        score -= deductions.get(field, 0)

    if score < 0:
        score = 0

    if score >= 90:
        grade = "A"
    elif score >= 80:
        grade = "B"
    elif score >= 70:
        grade = "C"
    elif score >= 60:
        grade = "D"
    else:
        grade = "F"

    return {
        "score": score,
        "grade": grade
    }