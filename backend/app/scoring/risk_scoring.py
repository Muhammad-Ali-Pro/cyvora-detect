def calculate_risk_score(rule):

    score = 0

    title = (rule.get("title") or "").lower()

    if "powershell" in title:
        score += 40

    if "credential" in title:
        score += 30

    if "admin" in title:
        score += 20

    if score >= 70:
        severity = "High"
    elif score >= 30:
        severity = "Medium"
    else:
        severity = "Low"

    return {
        "risk": score,
        "severity": severity
    }