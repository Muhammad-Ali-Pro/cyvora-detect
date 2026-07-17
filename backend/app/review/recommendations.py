def generate_recommendations(missing_fields):

    recommendation_map = {
        "Missing title": {
            "field": "Title",
            "recommendation": "Add a clear and descriptive Sigma rule title."
        },
        "Missing description": {
            "field": "Description",
            "recommendation": "Explain what suspicious behaviour this Sigma rule detects."
        },
        "Missing author": {
            "field": "Author",
            "recommendation": "Add the author's name or organization for traceability."
        },
        "Missing logsource product": {
            "field": "Logsource",
            "recommendation": "Specify the target product (Windows, Linux, Azure, etc.)."
        },
        "Missing detection condition": {
            "field": "Condition",
            "recommendation": "Define the detection logic using Sigma conditions."
        },
        "Missing level": {
            "field": "Severity",
            "recommendation": "Assign a severity level such as low, medium, high or critical."
        },
        "Missing false positives": {
            "field": "False Positives",
            "recommendation": "Document legitimate activities that could trigger this rule."
        },
        "Missing tags": {
            "field": "MITRE Tags",
            "recommendation": "Add MITRE ATT&CK or Sigma tags to improve classification."
        }
    }

    recommendations = []

    for field in missing_fields:
        if field in recommendation_map:
            recommendations.append(recommendation_map[field])

    return recommendations