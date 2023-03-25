import subprocess

def test_rps_program():
    cp = subprocess.run(
        ["python", "testing.py"],
        text = True,
        capture_output = True,
        input = "rock\n",
    )
    assert cp.returncode == 0
    assert cp.stderr == ""
    outputs = [
        "rock, paper or scissors? scissors\nYou win\n",
        "rock, paper or scissors? rock\nit's a tie\n",
        "rock, paper or scissors? paper\nYou loose\n",
    ]
    assert cp.stdout in outputs