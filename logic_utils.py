
def get_range_for_difficulty(difficulty: str):
    """Return (low, high) inclusive range for a given difficulty."""
    if difficulty == "Easy":
        return 1, 20
    if difficulty == "Normal":
        return 1, 100
    if difficulty == "Hard":
        return 1, 50
    return 1, 100


def parse_guess(raw: str, low: int = None, high: int = None):
    """
    Parse user input into an int guess.

    If low and high are provided, also validate the guess is within range.

    Returns: (ok: bool, guess_int: int | None, error_message: str | None)
    """
    if raw is None:
        return False, None, "Enter a guess."

    if raw == "":
        return False, None, "Enter a guess."

    try:
        if "." in raw:
            value = int(float(raw))
        else:
            value = int(raw)
    except Exception:
        return False, None, "That is not a number."

    if low is not None and high is not None:
        if value < low or value > high:
            return False, value, f"Guess must be between {low} and {high}."

    return True, value, None


def check_guess(guess, secret):
    """
    Compare guess to secret and return the outcome string.

    outcome examples: "Win", "Too High", "Too Low"
    """
    if guess == secret:
        return "Win"

    if guess > secret:
        return "Too High"
    else:
        return "Too Low"


def update_score(current_score: int, outcome: str, attempt_number: int):
    """Update score based on outcome and attempt number."""
    if outcome == "Win":
        points = 100 - 10 * (attempt_number + 1)
        if points < 10:
            points = 10
        return current_score + points

    if outcome == "Too High":
        if attempt_number % 2 == 0:
            return current_score + 5
        return current_score - 5

    if outcome == "Too Low":
        return current_score - 5

    return current_score


# --- Highscore persistence helpers ---
import json
from datetime import datetime
from typing import List, Dict

HIGHSCORE_FILE = "highscores.json"


def load_highscores(filepath: str = HIGHSCORE_FILE) -> List[Dict]:
    """Load highscores from a JSON file, returning a list of records.

    Each record is a dict with keys: `name`, `score`, `difficulty`, `timestamp`.
    If the file does not exist or is invalid, returns an empty list.
    """
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            data = json.load(f)
            if isinstance(data, list):
                return data
    except FileNotFoundError:
        return []
    except Exception:
        return []
    return []


def save_highscore(name: str, score: int, difficulty: str, filepath: str = HIGHSCORE_FILE):
    """Append a new highscore record and persist the sorted list to disk."""
    records = load_highscores(filepath)
    record = {
        "name": name,
        "score": score,
        "difficulty": difficulty,
        "timestamp": datetime.utcnow().isoformat(),
    }
    records.append(record)
    # keep records sorted descending by score
    records.sort(key=lambda r: r.get("score", 0), reverse=True)
    try:
        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(records, f, indent=2)
    except Exception:
        # If saving fails, silently ignore to avoid breaking the game UI
        pass


def get_top_highscores(n: int = 5, filepath: str = HIGHSCORE_FILE) -> List[Dict]:
    """Return the top `n` highscores (sorted descending).

    Defaults use the module-level `HIGHSCORE_FILE`.
    """
    records = load_highscores(filepath)
    records.sort(key=lambda r: r.get("score", 0), reverse=True)
    return records[:n]


# --- Highscore persistence helpers ---
import json
import os
import time

HIGHSCORE_FILE = "highscores.json"


def load_highscores():
    """Load highscores from disk. Returns a list of entries.

    Each entry: {"name": str, "score": int, "difficulty": str, "ts": int}
    """
    if not os.path.exists(HIGHSCORE_FILE):
        return []
    try:
        with open(HIGHSCORE_FILE, "r") as fh:
            return json.load(fh)
    except Exception:
        return []


def save_highscore(name: str, score: int, difficulty: str):
    """Append a highscore entry and persist top 10 scores.

    Returns the updated highscores list.
    """
    hs = load_highscores()
    entry = {"name": name or "Anonymous", "score": int(score), "difficulty": difficulty, "ts": int(time.time())}
    hs.append(entry)
    hs.sort(key=lambda e: e["score"], reverse=True)
    hs = hs[:10]
    try:
        with open(HIGHSCORE_FILE, "w") as fh:
            json.dump(hs, fh, indent=2)
    except Exception:
        # best-effort persistence; ignore failures
        pass
    return hs


def get_top_highscores(difficulty: str = None, limit: int = 5):
    """Return top `limit` highscores. If `difficulty` provided, filter by it."""
    hs = load_highscores()
    if difficulty:
        hs = [e for e in hs if e.get("difficulty") == difficulty]
    return hs[:limit]
