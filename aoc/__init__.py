import requests
from pathlib import Path
from bs4 import BeautifulSoup


def get_input(year: int, day: int, sample=None):
    if sample is not None:
        return sample_input(year, day, sample)
    else:
        return get_input_real(year, day)


def get_input_real(year: int, day: int):
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


def sample_input(year, day, sel=None):
    cookie = Path.home() / ".aoc-cookie"
    if not cookie.exists():
        raise Exception("No cookie?  Check " + str(cookie))
    cookies = {"session": cookie.read_text().strip()}

    value = requests.get(f"https://adventofcode.com/{year}/day/{day}", cookies=cookies)
    soup = BeautifulSoup(value.text, features="html.parser")
    inputs = {}
    for idx, code_info in enumerate(soup.find_all("pre")):
        inputs[idx] = code_info.text
    if sel is None:
        sel = input(f"select: {sorted(inputs.keys())}")
    return inputs[int(sel)]
