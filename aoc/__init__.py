import requests
from pathlib import Path


def get_input(year: int, day: int):
    cookie = Path.home() / ".aoc-cookie"
    if not cookie.exists():
        raise Exception("No cookie?  Check " + str(cookie))
    cookies = {"session": cookie.read_text().strip()}

    value = requests.get(
        f"https://adventofcode.com/{year}/day/{day}/input", cookies=cookies
    )
    if value.status_code > 300:
        raise Exception("Need a better cookie?")
    return value.text
