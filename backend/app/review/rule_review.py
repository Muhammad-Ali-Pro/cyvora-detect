from .recommendations import generate_recommendations


def review_sigma_rule(rule):

    strengths = []
    missing = []

    if rule.get("title"):
        strengths.append("Title present")
    else:
        missing.append("Missing title")

    if rule.get("description"):
        strengths.append("Description present")
    else:
        missing.append("Missing description")

    if rule.get("author"):
        strengths.append("Author present")
    else:
        missing.append("Missing author")

    if rule.get("product"):
        strengths.append("Logsource product present")
    else:
        missing.append("Missing logsource product")

    if rule.get("condition"):
        strengths.append("Detection condition present")
    else:
        missing.append("Missing detection condition")

    if rule.get("level"):
        strengths.append("Level present")
    else:
        missing.append("Missing level")

    if rule.get("falsepositives"):
        strengths.append("False positives documented")
    else:
        missing.append("Missing false positives")

    if rule.get("tags"):
        strengths.append("MITRE/Tags present")
    else:
        missing.append("Missing tags")

    if len(missing) == 0:
        status = "Excellent"
    elif len(missing) <= 2:
        status = "Good"
    else:
        status = "Needs Improvement"

    recommendations = generate_recommendations(missing)

    return {
        "status": status,
        "strengths": strengths,
        "missing": missing,
        "recommendations": recommendations
    }