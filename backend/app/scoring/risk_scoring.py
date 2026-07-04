def calculate_risk_score(rule):

    score = 0
    reasons =[]
    title = (rule.get("title") or "").lower()

    if "powershell" in title:
        score += 40
        reasons.append("PowerShell execution detected")

    if "credential" in title:
        score += 30
        reasons.append("Credential access keyword detected")
    if "admin" in title:
        score += 20
        reasons.append("Administrative activity detected")

    if score >= 70:
        severity = "High"
    elif score >= 30:
        severity = "Medium"
    else:
        severity = "Low"

    return {
        "risk": score,
        "severity": severity,
        "reasons": reasons
    }