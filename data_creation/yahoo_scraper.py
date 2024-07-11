import requests
from bs4 import BeautifulSoup

url = "https://sports.yahoo.com/mlb/odds/"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

games = soup.find("div", class_="bet-packs-wrapper")

odds_data = {}

# Iterate over each game container
for game in games:
    # Find all divs with the class "Fxg(1)" within each game container
    res = game.find_all("div", class_="Fxg(1)")
    
    # Initialize variables to store team names and the associated number
    team_names = []
    associated_number = None

    for item in res:
        # Find all spans with the specific class containing team names
        team_spans = item.find_all("span", class_="Fw(600) Pend(4px) Ell D(ib) Maw(190px) Va(m)")
        
        for team_span in team_spans:
            team_names.append(team_span.text.strip())
        
        # Find all spans with the class "Lh(19px)" and get the third instance
        associated_spans = item.find_all("span", class_="Lh(19px)")
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

# Print the dictionary
print(odds_data)
