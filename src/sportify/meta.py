PROJECT = "sportify"
PROJECT_URL = f"https://github.com/jacob-thompson/{PROJECT}"
API_URL = "https://site.api.espn.com/apis/site/v2/sports/"

ERR = "ERROR:"
REPORT = f"PLEASE SUBMIT AN ISSUE REPORT:\n\t{PROJECT_URL}/issues"
UNEXPECTED = f"{ERR} AN UNEXPECTED ERROR HAS OCCURRED\n{REPORT}"

SPORTS = {
    "football": {
        "NFL"
    },
    "basketball": {
        "NBA"
    },
    "baseball": {
        "MLB"
    },
    "hockey": {
        "NHL"
    }
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

API_OK = 200
EXIT_OK = 0
EXIT_FAIL = 1
