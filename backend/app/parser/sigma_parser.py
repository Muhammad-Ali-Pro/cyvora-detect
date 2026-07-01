import yaml


def parse_sigma_rule(file_content: bytes):

    data = yaml.safe_load(file_content)

    return {
        "title": data.get("title"),
        "product": data.get("logsource", {}).get("product"),
        "condition": data.get("condition"),
    }