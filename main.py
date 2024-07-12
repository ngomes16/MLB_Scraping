from yahoo_scraper import scrape_yahoo_odds
from data_processing import read_historical_data, calculate_betting_strength, determine_betting_recommendation
from twitter import authenticate_twitter, post_to_twitter

def main():

    # Step 1: Fetch Yahoo's Expected Runs
    url = "https://sports.yahoo.com/mlb/odds/"
    yahoo_expected_runs = scrape_yahoo_odds(url)

    url = "https://sports.yahoo.com/mlb/odds/"
    yahoo_expected_runs = scrape_yahoo_odds(url)

    # Step 2: Read Historical Data
    historical_data = read_historical_data()

    # Step 3: Calculate Betting Strength
    betting_strength = calculate_betting_strength(yahoo_expected_runs, historical_data)

    # Step 4: Determine Betting Recommendation
    betting_recommendations = determine_betting_recommendation(betting_strength, yahoo_expected_runs)


    # Prepare messages
    messages = [f"For {teams[0]} v {teams[1]} there is a {recommendation}" for teams, recommendation in betting_recommendations.items()]

    # Authenticate Twitter API
    client = authenticate_twitter()

    # Post to Twitter
    post_to_twitter(client, messages)
   
   


if __name__ == "__main__":
    main()
