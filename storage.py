import json
from pathlib import Path
from typing import Any


BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"
TASKS_FILE = DATA_DIR / "tasks.json"


def save_tasks(tasks: list[dict[str, Any]]) -> None:
    """Save tasks to a JSON file."""
    try:
        DATA_DIR.mkdir(parents=True, exist_ok=True)
        with TASKS_FILE.open("w", encoding="utf-8") as file:
		json.dump(tasks, file, sort_keys=True, indent=2, ensure_ascii=False)
    except (OSError, TypeError, ValueError) as e:
        raise RuntimeError(f"Failed to save tasks: {e}") from e


def load_tasks() -> list[dict[str, Any]]:
    """Load tasks from a JSON file."""
    if not TASKS_FILE.exists():
        return []
    try:
        with TASKS_FILE.open("r", encoding="utf-8") as file:
            return json.load(file)
    except (OSError, json.JSONDecodeError) as e:
        raise RuntimeError(f"Failed to load tasks: {e}") from e