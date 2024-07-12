from yahoo_scraper import scrape_yahoo_odds
from data_processing import read_historical_data, calculate_betting_strength, determine_betting_recommendation

def main():
    # Step 1: Fetch Yahoo's Expected Runs
    url = "https://sports.yahoo.com/mlb/odds/"
    yahoo_expected_runs = scrape_yahoo_odds(url)

    if not yahoo_expected_runs:
        print("Failed to fetch Yahoo's expected runs. Exiting.")
        return

    # Step 2: Read Historical Data
    historical_data = read_historical_data()

    # Step 3: Calculate Betting Strength
    betting_strength = calculate_betting_strength(yahoo_expected_runs, historical_data)

    # Step 4: Determine Betting Recommendation
    betting_recommendations = determine_betting_recommendation(betting_strength)

    # Print or use betting recommendations
    for teams, recommendation in betting_recommendations.items():
        print(f"For {teams}: {recommendation} based on betting strength {betting_strength[teams]}")

if __name__ == "__main__":
    main()
