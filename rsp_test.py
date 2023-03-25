from testing import is_valid_play
from testing import computer_play
from testing import determine_game_result
from testing import main
import subprocess

def test_rps_program():
    cp = subprocess.run(
        ["python", "testing.py"],
        text = True,
        capture_output = True,
        input = "rock\n",
    )
    assert cp.returncode == 0


def test_full_game(capsys, monkeypatch):
    def fake_input(prompt):
        print(prompt)
        return "rock"
    monkeypatch.setattr("builtins.input", fake_input)
    main()
    captured = capsys.readouterr()
    lines = captured.out.splitlines()
    assert lines[0].strip() == "rock, paper or scissors?"
    l1 = lines[1].strip()
    assert l1 in ["rock", "scissors","paper"]
    l2 = lines[2].strip()
    assert l2 in ["it's a tie","You loose","You winn"]
    assert len(lines) == 3
    if l1 == "rock":
        assert l2 == "it's a tie"
    elif l1 == "paper":
        assert l2 == "You loose"
    elif l1 == "scissors":
        assert l2 == "You winn"

def test_paper_beats_rock():
    result = determine_game_result("paper", "rock")
    assert result == "human"

def test_rock_beats_scissors():
    result = determine_game_result("rock", "scissors")
    assert result == "human"

def test_scissors_beats_paper():
    result = determine_game_result("scissors", "paper")
    assert result == "human"

def test_computer_paper_beats_rock():
    result = determine_game_result("rock", "paper")
    assert result == "computer"

def test_computer_rock_beats_scissors():
    result = determine_game_result("scissors", "rock")
    assert result == "computer"

def test_computer_scissors_beats_paper():
    result = determine_game_result("paper", "scissors")
    assert result == "computer"

def test_tie():
    for play in ["rock", "scissors", "paper"]:
        result = determine_game_result(play, play)
        assert result == "tie"

def test_computer_play_is_valid():
    assert is_valid_play(computer_play())


def test_computer_play():
    played = []
    play = computer_play()
    played.append(play)
    counter = 1
    while len(played) < 3:
        play = computer_play()
        counter += 1
        if play not in played:
            played.append(play)
        assert counter < 100

def test_rokc_is_not_valid_play():
    assert is_valid_play("rokc") is False

def test_empty_str_is_not_valid_play():
    assert is_valid_play("") is False

def test_rock_is_valid_play():
    assert is_valid_play("rock") is True

def test_paper_is_valid_play():
    assert is_valid_play("paper") is True

def test_scissors_is_valid_play():
    assert is_valid_play("scissors") is True
