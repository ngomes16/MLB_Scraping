def read_historical_data():
    historical_data = {}
    with open('games_data/formatted_data.txt', 'r') as file:
        for line in file:
            line = line.strip()
            if line:
                # Assuming the format is consistent ('team1', 'team2'): [list_of_scores]
                key_value = line.split(':')
                teams = eval(key_value[0].strip())
                scores = eval(key_value[1].strip())
                historical_data[teams] = scores
    return historical_data

def calculate_betting_strength(yahoo_expected_runs, historical_data):
    betting_strength = {}

    for teams, yahoo_expected in yahoo_expected_runs.items():
        # Try to find historical data matching the teams in either order
        historical_scores = historical_data.get(teams, historical_data.get((teams[1], teams[0]), []))

        if not historical_scores:
            # No historical data available for either order, skip this matchup
            betting_strength[teams] = "No historical data available"
            continue

        # Calculate the percentage of games where the team's score exceeded Yahoo's expected runs
        count_above = sum(1 for score in historical_scores if score > yahoo_expected)
        total_games = len(historical_scores)
        percentage_above = count_above / total_games if total_games > 0 else 0.0

        # Calculate the betting strength out of 10.0
        betting_strength_score = percentage_above * 10.0

        betting_strength[teams] = betting_strength_score

    return betting_strength

def determine_betting_recommendation(betting_strength):
    betting_recommendations = {}

    for teams, strength_score in betting_strength.items():
        if float(strength_score) >= 7.2:
            betting_recommendations[teams] = f"Bet Over based on betting strength {strength_score}"
        elif float(strength_score) <= 2.8:
            # Adjust strength score output based on the threshold
            adjusted_score = 7.2 - (2.8 - float(strength_score))
            betting_recommendations[teams] = f"Bet Under based on betting strength {adjusted_score}"
        else:
            betting_recommendations[teams] = "No Bet"

    return betting_recommendations

