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

def determine_betting_recommendation(betting_strength, yahoo_expected_runs):
    betting_recommendations = {}

    for teams, strength_score in betting_strength.items():
        # Round the strength score to one decimal place
        rounded_strength_score = round(strength_score, 1)
        
        # Retrieve Yahoo's predicted number
        yahoo_prediction = yahoo_expected_runs.get(teams, "unknown")

        if rounded_strength_score >= 8.0:
            betting_recommendations[teams] = f"Very favored bet on line of over {yahoo_prediction} based on betting strength {rounded_strength_score}"
        elif rounded_strength_score >= 7.2:
            betting_recommendations[teams] = f"Favored bet on line of over {yahoo_prediction} based on betting strength {rounded_strength_score}"
        elif rounded_strength_score >= 6.7:
            betting_recommendations[teams] = f"Slightly favored bet on line of over {yahoo_prediction} based on betting strength {rounded_strength_score}"
        # elif rounded_strength_score >= 3.4 and rounded_strength_score <= 6.6:
        #     betting_recommendations[teams] = f"No bet on line of {yahoo_prediction} based on low betting strength"
        elif rounded_strength_score >= 0.0 and rounded_strength_score <= 2.0:
            betting_recommendations[teams] = f"Very favored bet on line of under {yahoo_prediction} based on betting strength {10 - rounded_strength_score}"
        elif rounded_strength_score >= 2.1 and rounded_strength_score <= 2.8:
            betting_recommendations[teams] = f"Favored bet on line of under {yahoo_prediction} based on betting strength {10 - rounded_strength_score}"
        elif rounded_strength_score >= 2.9 and rounded_strength_score <= 3.3:
            betting_recommendations[teams] = f"Slightly favored bet on line of under {yahoo_prediction} based on betting strength {10 - rounded_strength_score}"
        

    return betting_recommendations


