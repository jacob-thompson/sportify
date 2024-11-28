import requests
from simple_term_menu import TerminalMenu

PROJECT = "sportify"
PROJECT_URL = f"https://github.com/jacob-thompson/{PROJECT}"
API_URL = "https://site.api.espn.com/apis/site/v2/sports/"

ERR = "ERROR:"
REPORT = f"PLEASE SUBMIT AN ISSUE REPORT:\n\t{PROJECT_URL}/issues"
UNEXPECTED = f"{ERR} AN UNEXPECTED ERROR HAS OCCURRED\n{REPORT}"

API_OK = 200
EXIT_OK = 0
EXIT_FAIL = 1

LEAGUES = [
    "[1] NFL", "[2] NBA", "[3] MLB", "[4] NHL"
]

NFL = [
    "[1] ARI", "[2] ATL", "[3] BAL", "[4] BUF",
    "[5] CAR", "[6] CHI", "[7] CIN", "[8] CLE",
    "[9] DAL", "[0] DEN", "[a] DET", "[b] GB",
    "[c] HOU", "[d] IND", "[e] JAX", "[f] KC",
    "[g] LV", "[h] LAC", "[i] LAR", "[j] MIA",
    "[k] MIN", "[l] NE", "[m] NO", "[n] NYG",
    "[o] NYJ", "[p] PHI", "[q] PIT", "[r] SF",
    "[s] SEA", "[t] TB", "[u] TEN", "[v] WSH"
]

NBA = [
    "[1] ATL", "[2] BOS", "[3] BKN", "[4] CHA",
    "[5] CHI", "[6] CLE", "[7] DAL", "[8] DEN",
    "[9] DET", "[0] GS", "[a] HOU", "[b] IND",
    "[c] LAC", "[d] LAL", "[e] MEM", "[f] MIA",
    "[g] MIL", "[h] MIN", "[i] NO", "[j] NY",
    "[k] OKC", "[l] ORL", "[m] PHI", "[n] PHX",
    "[o] POR", "[p] SAC", "[q] SA", "[r] TOR",
    "[s] UTAH", "[t] WSH"
]

MLB = [
    "[1] ARI", "[2] ATL", "[3] BAL", "[4] BOS",
    "[5] CHW", "[6] CHC", "[7] CIN", "[8] CLE",
    "[9] COL", "[0] DET", "[a] HOU", "[b] KC",
    "[c] LAA", "[d] LAD", "[e] MIA", "[f] MIL",
    "[g] MIN", "[h] NYY", "[i] NYM", "[j] OAK",
    "[k] PHI", "[l] PIT", "[m] SD", "[n] SF",
    "[o] SEA", "[p] STL", "[q] TB", "[r] TEX",
    "[s] TOR", "[t] WSH"
]

NHL = [
    "[1] ANA", "[2] BOS", "[3] BUF", "[4] CGY",
    "[5] CAR", "[6] CHI", "[7] COL", "[8] CBJ",
    "[9] DAL", "[0] DET", "[a] EDM", "[b] FLA",
    "[c] LA", "[d] MIN", "[e] MTL", "[f] NSH",
    "[g] NJ", "[h] NYI", "[i] NYR", "[j] OTT",
    "[k] PHI", "[l] PIT", "[m] SJ", "[n] SEA",
    "[o] STL", "[p] TB", "[q] TOR", "[r] UTAH",
    "[s] VAN", "[t] VGK", "[u] WSH", "[v] WPG"
]

def print_info():
    print(f"{PROJECT} {PROJECT_URL}")

def request_data(league, team):
    try:
        if league == LEAGUES[0]:
            endpoint = f"football/nfl/teams/{team}"
        elif league == LEAGUES[1]:
            endpoint = f"basketball/nba/teams/{team}"
        elif league == LEAGUES[2]:
            endpoint = f"baseball/mlb/teams/{team}"
        elif league == LEAGUES[3]:
            endpoint = f"hockey/nhl/teams/{team}"
        else: # impossible
            print(UNEXPECTED)
            raise SystemExit(EXIT_FAIL)

        response = requests.get(API_URL + endpoint)

        if response.status_code == API_OK:
            return response.json()
        else: # occurs upon unsuccessful API request
            raise Exception(f"{ERR} API RESPONSE STATUS CODE {response.status_code}")
    except requests.exceptions.RequestException as e: # unexpected, should never occur
        print(f"{UNEXPECTED}\nREQUEST EXCEPTION ENCOUNTERED: {e}")
        raise SystemExit(EXIT_FAIL)

def main():
    print_info()

    try: # get input & request output
        menu = TerminalMenu(LEAGUES, title = "LEAGUE")
        entry = menu.show()
        league = LEAGUES[entry]

        if league == LEAGUES[0]:
            teams = NFL
        elif league == LEAGUES[1]:
            teams = NBA
        elif league == LEAGUES[2]:
            teams = MLB
        elif league == LEAGUES[3]:
            teams = NHL
        else: # impossible
            print(UNEXPECTED)
            raise SystemExit(EXIT_FAIL)

        submenu = TerminalMenu(teams, title = "TEAM")
        entry = submenu.show()
        team = teams[entry].split()[1]

        data = request_data(league, team)
    except TypeError: # occurs when user presses Escape or Q to quit
        raise SystemExit(EXIT_OK)
    except Exception as e: # occurs upon unsuccessful API request
        print(e)
        raise SystemExit(EXIT_FAIL)

    print(data)
    raise SystemExit(EXIT_OK)

if __name__ == "__main__":
    main()