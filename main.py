
from pyscript import document

def candidate_checker(e):
    club_members = [
        "john jujutsu",
        "yuta okkotsu",
        "megumi fushiguro",
        "yuji itadori"
    ]

    f_name = document.getElementById("first_name").value
    l_name = document.getElementById("last_name").value

    candidate = f_name.strip() + " " + l_name.strip()

    member_checker = candidate.lower() in club_members

    messages = (
        f"Sorry {candidate}, your name is not on the list.",
        f"Congratulations {candidate}! Welcome to Jujutsu High. We hope to see you at campus soon!"
    )

    document.getElementById("result").innerHTML = messages[member_checker]
