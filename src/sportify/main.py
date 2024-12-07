from .sportify import *

def main():
    print(f"{PROJECT} {PROJECT_URL}")

    leagues = list(MENU_DATA.keys())
    try: # get input & request output
        menu = Menu(leagues, title = "LEAGUE", clear_screen = True)
        entry = menu.show()
        selected_league = leagues[entry]

        teams = [MENU_DATA[league] for league in leagues if league == selected_league]
        assert teams != []

        submenu = Menu(teams[0], title = "TEAM", clear_screen = True)
        entry = submenu.show()
        selected_team = teams[0][entry]

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
