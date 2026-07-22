import yaml


def parse_sigma_rule(file_content: bytes):

    data = yaml.safe_load(file_content) or {}
    condition = data.get("condition")

    if condition is None:
        condition = data.get("detection", {}).get("condition")

    return {
        "title": data.get("title"),
        "product": data.get("logsource", {}).get("product"),
        "condition": condition,
    }