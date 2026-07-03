def validate_sigma_rule(rule):

    issues = []

    if not rule.get("title"):
        issues.append("Missing title")

    if not rule.get("product"):
        issues.append("Missing logsource product")

    if not rule.get("condition"):
        issues.append("Missing condition")

    return {
        "valid": len(issues) == 0,
        "issues": issues
    }