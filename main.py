from datetime import datetime
import json

from dateutil import tz
import requests
from simple_term_menu import TerminalMenu as Menu

PROJECT = "sportify"
PROJECT_URL = f"https://github.com/jacob-thompson/{PROJECT}"
API_URL = "https://site.api.espn.com/apis/site/v2/sports/"

ERR = "ERROR:"
REPORT = f"PLEASE SUBMIT AN ISSUE REPORT:\n\t{PROJECT_URL}/issues"
UNEXPECTED = f"{ERR} AN UNEXPECTED ERROR HAS OCCURRED\n{REPORT}"

API_OK = 200
EXIT_OK = 0
EXIT_FAIL = 1

SPORTS = {
    "football": ["NFL"],
    "basketball": ["NBA"],
    "baseball": ["MLB"],
    "hockey": ["NHL"]
}

MENU_DATA = {
    "[1] NFL": [
        "[1] ARI", "[2] ATL", "[3] BAL", "[4] BUF",
        "[5] CAR", "[6] CHI", "[7] CIN", "[8] CLE",
        "[9] DAL", "[0] DEN", "[a] DET", "[b] GB",
        "[c] HOU", "[d] IND", "[e] JAX", "[f] KC",
        "[g] LV", "[h] LAC", "[i] LAR", "[j] MIA",
        "[k] MIN", "[l] NE", "[m] NO", "[n] NYG",
        "[o] NYJ", "[p] PHI", "[q] PIT", "[r] SF",
        "[s] SEA", "[t] TB", "[u] TEN", "[v] WSH"
    ],
    "[2] NBA": [
        "[1] ATL", "[2] BOS", "[3] BKN", "[4] CHA",
        "[5] CHI", "[6] CLE", "[7] DAL", "[8] DEN",
        "[9] DET", "[0] GS", "[a] HOU", "[b] IND",
        "[c] LAC", "[d] LAL", "[e] MEM", "[f] MIA",
        "[g] MIL", "[h] MIN", "[i] NO", "[j] NY",
        "[k] OKC", "[l] ORL", "[m] PHI", "[n] PHX",
        "[o] POR", "[p] SAC", "[q] SA", "[r] TOR",
        "[s] UTAH", "[t] WSH"
    ],
    "[3] MLB": [
        "[1] ARI", "[2] ATL", "[3] BAL", "[4] BOS",
        "[5] CHW", "[6] CHC", "[7] CIN", "[8] CLE",
        "[9] COL", "[0] DET", "[a] HOU", "[b] KC",
        "[c] LAA", "[d] LAD", "[e] MIA", "[f] MIL",
        "[g] MIN", "[h] NYY", "[i] NYM", "[j] OAK",
        "[k] PHI", "[l] PIT", "[m] SD", "[n] SF",
        "[o] SEA", "[p] STL", "[q] TB", "[r] TEX",
        "[s] TOR", "[t] WSH"
    ],
    "[4] NHL": [
        "[1] ANA", "[2] BOS", "[3] BUF", "[4] CGY",
        "[5] CAR", "[6] CHI", "[7] COL", "[8] CBJ",
        "[9] DAL", "[0] DET", "[a] EDM", "[b] FLA",
        "[c] LA", "[d] MIN", "[e] MTL", "[f] NSH",
        "[g] NJ", "[h] NYI", "[i] NYR", "[j] OTT",
        "[k] PHI", "[l] PIT", "[m] SJ", "[n] SEA",
        "[o] STL", "[p] TB", "[q] TOR", "[r] UTAH",
        "[s] VAN", "[t] VGK", "[u] WSH", "[v] WPG"
    ]
}

class BadAPIRequest(Exception):
    pass

def convert(time):
    parsed = datetime.strptime(time, "%Y-%m-%dT%H:%MZ")
    utc = parsed.replace(tzinfo=tz.tzutc()) # represent time in UTC
    local = utc.astimezone(tz.tzlocal()) # convert time to local

    local_date = f"{local.date().year}-{local.date().month:02}-{local.date().day:02}"
    local_time = f"{local.time().hour:02}:{local.time().minute:02}"
    local_datetime = f"{local_date} {local_time}"

    return local_datetime

def output(data):
    name = data["team"]["displayName"]
    print(name)

    try:
        # be cautious here since a team's record field may be empty during offseason
        record = data["team"]["record"]["items"][0]["summary"]
        print(record) # TODO: expand
    except KeyError:
        pass

    link = data["team"]["links"][0]["href"]
    print(link) # TODO: expand

    venue = data["team"]["franchise"]["venue"]["fullName"]
    address = data["team"]["franchise"]["venue"]["address"]
    location = f"{venue}"
    for entity in address.values():
        location += f", {entity}"
    print(location)

    next_event = data["team"]["nextEvent"][0]
    event_name = next_event["shortName"]
    event_time = convert(next_event["date"])
    event_msg = f"{event_name} {event_time}"
    print(event_msg)

    standing = data["team"]["standingSummary"]
    print(standing)

def request_data(league, team):
    try:
        for listed_sport, associations in SPORTS.items():
            if league in associations:
                sport = listed_sport
                break

        assert sport is not None

        endpoint = f"{sport}/{league}/teams/{team}/"
        response = requests.get(API_URL + endpoint.lower())

        if response.status_code == API_OK:
            return response.json()
        else:
            raise BadAPIRequest(f"{ERR} API RESPONSE STATUS CODE {response.status_code}")
    except requests.exceptions.RequestException as e:
        # treat this case as unexpected since RequestException is "ambiguous"
        # https://requests.readthedocs.io/en/latest/api/#requests.RequestException
        print(f"{UNEXPECTED}\nREQUEST EXCEPTION ENCOUNTERED: {e}")
        raise SystemExit(EXIT_FAIL)

def main():
    print(f"{PROJECT} {PROJECT_URL}")

    leagues = list(MENU_DATA.keys())
    try: # get input & request output
        menu = Menu(leagues, title = "LEAGUE")
        entry = menu.show()
        selected_league = leagues[entry]

        for league in leagues:
            if league == selected_league:
                teams = MENU_DATA[league]
                break

        assert teams is not None

        submenu = Menu(teams, title = "TEAM", clear_screen = True)
        entry = submenu.show()
        selected_team = teams[entry]

        data = request_data(selected_league.split()[1], selected_team.split()[1])
    except BadAPIRequest as error:
        print(error)
        raise SystemExit(EXIT_FAIL)
    except TypeError: # occurs when user presses Escape or Q to quit
        raise SystemExit(EXIT_OK)
    except AssertionError: # impossible
        print(UNEXPECTED)
        raise SystemExit(EXIT_FAIL)

    output(data)
    raise SystemExit(EXIT_OK)

if __name__ == "__main__":
    main()