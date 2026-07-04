def map_to_mitre(rule):

    title = (rule.get("title") or "").lower()

    if "powershell" in title:
        return {
            "technique": "T1059.001",
            "name": "PowerShell",
            "tactic": "Execution"
        }

    return {}