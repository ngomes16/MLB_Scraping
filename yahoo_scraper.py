import requests
from bs4 import BeautifulSoup

def scrape_yahoo_odds(url):
    try:
        # Make a request to the URL
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for bad status codes

        # Parse the HTML content
        soup = BeautifulSoup(response.content, "html.parser")

        # Find the upcoming games section
        upcoming_games_section = soup.find("h3", class_="YahooSans-Bold Pb(20px) smartphone_Bdb(border-standings)", text="Upcoming")

        if upcoming_games_section:
            # Find the container with all games under the upcoming games section
            games_container = upcoming_games_section.find_next("div", class_="bet-packs-wrapper")
            if games_container:
                # Iterate over each game container
                odds_data = {}
                games = games_container.find_all("div", class_="Fxg(1)")
                for game in games:
                    # Initialize variables to store team names and the associated number
                    team_names = []
                    associated_number = None

                    # Find all spans with the specific class containing team names
                    team_spans = game.find_all("span", class_="Fw(600) Pend(4px) Ell D(ib) Maw(190px) Va(m)")
                    for team_span in team_spans:
                        team_names.append(team_span.text.strip())

                    # Find the associated number
                    associated_spans = game.find_all("span", class_="Lh(19px)")
                    if len(associated_spans) >= 4:
                        try:
                            associated_number = float(associated_spans[3].text.replace('O ', '').replace('U ', ''))
                        except ValueError:
                            continue

                    # Ensure there are exactly two team names and an associated number
                    if len(team_names) == 2 and associated_number is not None:
                        # Sort team names alphabetically
                        sorted_teams = tuple(sorted(team_names))
                        odds_data[sorted_teams] = associated_number

                return odds_data
            else:
                print("No games container found under upcoming games section.")
                return {}
        else:
            print("Upcoming games section not found.")
            return {}

    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return {}

if __name__ == "__main__":
    url = "https://sports.yahoo.com/mlb/odds/"
    yahoo_expected_runs = scrape_yahoo_odds(url)
    print(yahoo_expected_runs)
