import yaml
from pathlib import Path

BASE_DIR = Path(__file__).parent
CONFIG_PATH = BASE_DIR / "config.yaml"
RULES_DIR = BASE_DIR / "rules"


def load_config():
    with open(CONFIG_PATH) as f:
        return yaml.safe_load(f)


def list_rules_to_run(config):
    tasks = []
    for table, details in config.get("tables", {}).items():
        if not details.get("enabled", False):
            continue
        for rule in details.get("rules", []):
            tasks.append((table, rule))
    return tasks


def main():
    config = load_config()
    tasks = list_rules_to_run(config)

    print("Data Quality Rules to execute:")
    for table, rule in tasks:
        print(f"- Table: {table:<10} | Rule: {rule}")


if __name__ == "__main__":
    main()