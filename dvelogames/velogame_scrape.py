import json
import time
from typing import Any

import bs4
import requests

BASE_URL = (
    "https://www.velogames.com/velogame/2024/leaguescores.php?league=14808756&ga=13&st="
)
STAGES = range(1, 17)
SLEEPY_TIME = 1  # Since velogames does not offer an API this value is quite relaxed
RESULTS_FILE = "results.json"


def results_2_soup(stage: int) -> bs4.BeautifulSoup:
    url = f"{BASE_URL}{stage}"
    page = requests.get(url)
    return bs4.BeautifulSoup(page.text, "html.parser")


def soup_2_users(soup: bs4.BeautifulSoup) -> bs4.element.Tag:
    """
    indices 0 and 2 below are newlines
    type ignored because the stubs don't list `children` as a possible return type
    """
    return list(soup.find(id="users").children)[1]  # type: ignore


def users_2_dict(users: bs4.element.Tag) -> dict[str, Any]:
    playaz = users.find_all("li")
    res = {}
    for hater in playaz:
        directeur_sportif = hater.find_all("p")[1].string
        team_name = hater.find("a").string
        score = int(hater.find_all("p")[0].string)
        res[team_name] = {"score": score, "ds": directeur_sportif}
    return res


def get_all_results() -> dict[str, Any]:
    all_results = {}
    for stage in STAGES:
        print(f"on stage {stage}")
        stage_results = results_2_soup(stage)
        playa_results = soup_2_users(stage_results)
        data = users_2_dict(playa_results)
        for playa, value in data.items():
            score = value["score"]
            ds = value["ds"]
            if playa not in all_results:
                all_results[playa] = {"ds": ds, "scores": [score]}
            else:
                all_results[playa]["scores"].append(score)
        time.sleep(SLEEPY_TIME)
    return all_results


if __name__ == "__main__":
    results = get_all_results()
    with open(RESULTS_FILE, "w") as f:
        f.write(json.dumps(results))
