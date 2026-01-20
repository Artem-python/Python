import json


def task() -> float:
    with open('input.json') as f:
        data = json.load(f)

    return round(sum(item["score"] * item["weight"] for item in data), 3)


print(task())
