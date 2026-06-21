
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
        # first-attempt (attempt_number == 1) should be 100 points
        points = 100 - 10 * (attempt_number - 1)
        if points < 10:
            points = 10
        new_score = current_score + points
        return max(new_score, 0)

    if outcome == "Too High":
        new_score = current_score - 5
        return max(new_score, 0)

    if outcome == "Too Low":
        new_score = current_score - 5
        return max(new_score, 0)

    return max(current_score, 0)


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
    """Persist a player's highscore but keep only their best per difficulty.

    Behavior:
    - If the player already has a record for the same difficulty, keep the higher score.
    - Otherwise append a new record.
    - Always sort descending by score before saving.
    """
    records = load_highscores(filepath)
    name = (name or "Anonymous").strip()

    # find existing record for this player+difficulty
    replaced = False
    for r in records:
        if r.get("name") == name and r.get("difficulty") == difficulty:
            # if existing score is lower, replace it; otherwise keep existing
            if int(r.get("score", 0)) < int(score):
                r["score"] = int(score)
                r["timestamp"] = datetime.utcnow().isoformat()
            replaced = True
            break

    if not replaced:
        records.append({
            "name": name,
            "score": int(score),
            "difficulty": difficulty,
            "timestamp": datetime.utcnow().isoformat(),
        })

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
    """Persist a player's highscore (best-per-player-per-difficulty) and return updated list."""
    hs = load_highscores()
    name = (name or "Anonymous").strip()

    # find existing entry for player+difficulty
    found = False
    for e in hs:
        if e.get("name") == name and e.get("difficulty") == difficulty:
            found = True
            if int(e.get("score", 0)) < int(score):
                e["score"] = int(score)
                e["ts"] = int(time.time())
            break

    if not found:
        hs.append({"name": name, "score": int(score), "difficulty": difficulty, "ts": int(time.time())})

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
    hs.sort(key=lambda e: e.get("score", 0), reverse=True)
    return hs[:limit]
