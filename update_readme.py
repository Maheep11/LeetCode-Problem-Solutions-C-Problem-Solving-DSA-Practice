import requests
import re

USERNAME = "WAS8aXvrJv"

def get_stats(username):
    url = "https://leetcode-stats-api.herokuapp.com/" + username
    res = requests.get(url)
    data = res.json()
    return {
        "easy": data["easySolved"],
        "medium": data["mediumSolved"],
        "hard": data["hardSolved"],
        "total": data["totalSolved"]
    }

def update_readme(stats):
    with open("README.md", "r", encoding="utf-8") as f:
        content = f.read()

    content = re.sub(r"\| Easy\s+\| \d+\s+\|", f"| Easy       | {stats['easy']}              |", content)
    content = re.sub(r"\| Medium\s+\| \d+\s+\|", f"| Medium     | {stats['medium']}              |", content)
    content = re.sub(r"\| Hard\s+\| \d+\s+\|", f"| Hard       | {stats['hard']}              |", content)

    with open("README.md", "w", encoding="utf-8") as f:
        f.write(content)

if __name__ == "__main__":
    stats = get_stats(USERNAME)
    update_readme(stats)
