from datetime import datetime

from dateutil import tz
import requests

from .meta import API_URL, API_OK, SPORTS, EXIT_FAIL, UNEXPECTED


class BadAPIRequest(Exception):
    pass


def convert(time):
    parsed = datetime.strptime(time, "%Y-%m-%dT%H:%MZ")
    utc = parsed.replace(tzinfo=tz.tzutc())  # represent time in UTC
    local = utc.astimezone(tz.tzlocal())  # convert time to local

    year = local.date().year
    month = local.date().month
    day = local.date().day
    hour = local.time().hour
    minute = local.time().minute

    local_date = f"{year}-{month:02}-{day:02}"
    local_time = f"{hour:02}:{minute:02}"
    local_datetime = f"{local_date} {local_time}"

    return local_datetime


def output(data):
    link = data["team"]["links"][0]["href"]
    print(link)  # TODO: expand

    name = data["team"]["displayName"]
    print(name, end=" - ")

    standing = data["team"]["standingSummary"]
    print(standing, end=" ")

    try:
        # a team's record field may be empty during offseason
        record = data["team"]["record"]["items"][0]["summary"]
        print(f"({record})")  # TODO: expand
    except KeyError:
        print()

    venue = data["team"]["franchise"]["venue"]["fullName"]
    address = data["team"]["franchise"]["venue"]["address"]
    location = "".join(f", {entity}" for entity in address.values())
    print(f"{venue}{location}")

    next_event = data["team"]["nextEvent"][0]
    event_name = next_event["name"]
    event_time = convert(next_event["date"])
    event_msg = f"{event_name} {event_time}"
    print(event_msg)


def request_data(league, team):
    try:
        sport = [
            listed
            for listed, associations in SPORTS.items()
            if league in associations
        ]
        assert sport != [], "INVALID SPORT"

        endpoint = f"{sport[0]}/{league}/teams/{team}/"
        response = requests.get(API_URL + endpoint.lower())

        if response.status_code == API_OK:
            return response.json()
        else:
            raise BadAPIRequest(f"ERROR: API RESPONSE STATUS CODE {response.status_code}")
    except requests.exceptions.RequestException as error:
        # treat this case as unexpected since RequestException is "ambiguous"
        # https://requests.readthedocs.io/en/latest/api/#requests.RequestException
        print(f"{UNEXPECTED}\nREQUEST EXCEPTION ENCOUNTERED: {error}")
        raise SystemExit(EXIT_FAIL)
