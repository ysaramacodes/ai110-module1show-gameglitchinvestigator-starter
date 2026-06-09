from logic_utils import check_guess

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    result = check_guess(50, 50)
    assert result == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    result = check_guess(60, 50)
    assert result == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    result = check_guess(40, 50)
    assert result == "Too Low"

# Hint text tests
def test_hint_easy_start():
    """Easy difficulty at start: 6 attempts, 0 used = 6 left"""
    attempt_limit = 6
    attempts_used = 0
    attempts_left = attempt_limit - attempts_used
    
    hint_text = f"Guess a number between 1 and 20. Attempts left: {attempts_left}"
    assert "1 and 20" in hint_text
    assert "Attempts left: 6" in hint_text

def test_hint_easy_midgame():
    """Easy difficulty mid-game: 6 attempts, 3 used = 3 left"""
    attempt_limit = 6
    attempts_used = 3
    attempts_left = attempt_limit - attempts_used
    
    hint_text = f"Guess a number between 1 and 20. Attempts left: {attempts_left}"
    assert "1 and 20" in hint_text
    assert "Attempts left: 3" in hint_text

def test_hint_hard_last_attempt():
    """Hard difficulty last attempt: 5 attempts, 4 used = 1 left"""
    attempt_limit = 5
    attempts_used = 4
    attempts_left = attempt_limit - attempts_used
    
    hint_text = f"Guess a number between 1 and 50. Attempts left: {attempts_left}"
    assert "1 and 50" in hint_text
    assert "Attempts left: 1" in hint_text

def test_hint_normal_start():
    """Normal difficulty at start: 8 attempts, 0 used = 8 left"""
    attempt_limit = 8
    attempts_used = 0
    attempts_left = attempt_limit - attempts_used
    
    hint_text = f"Guess a number between 1 and 100. Attempts left: {attempts_left}"
    assert "1 and 100" in hint_text
    assert "Attempts left: 8" in hint_text

def test_hint_normal_all_used():
    """Normal difficulty out of attempts: 8 attempts, 8 used = 0 left"""
    attempt_limit = 8
    attempts_used = 8
    attempts_left = attempt_limit - attempts_used
    
    hint_text = f"Guess a number between 1 and 100. Attempts left: {attempts_left}"
    assert "1 and 100" in hint_text
    assert "Attempts left: 0" in hint_text