import statistics

# Historical data from formatted_data.txt
historical_data = {
    ('Dodgers', 'Phillies'): [17.0, 14.0, 16.0, 9.0, 9.0, 10.0],
    ('Orioles', 'Cubs'): [13.0, 5.0, 9.0],
    ('Yankees', 'Rays'): [9.0, 5.0, 15.0, 10.0, 11.0, 17.0, 15.0, 6.0, 7.0, 9.0, 8.0, 3.0, 11.0],
    ('Red Sox', 'Athletics'): [10.0, 13.0, 7.0, 7.0, 3.0, 11.0]
}

# Yahoo's expected runs from yahoo_scraper.py
yahoo_expected_runs = {
    ('Dodgers', 'Phillies'): 6.5,
    ('Cubs', 'Orioles'): 5.5,
    ('Rays', 'Yankees'): 10.5,
    ('Athletics', 'Red Sox'): 11.5
}

# Calculate average scores and matchup frequency
average_scores = {}
matchup_frequency = {}

for matchup, scores in historical_data.items():
    average_score = statistics.mean(scores)
    average_scores[matchup] = average_score
    
    # Count the number of matchups
    if matchup in matchup_frequency:
        matchup_frequency[matchup] += 1
    else:
        matchup_frequency[matchup] = 1

# Determine betting decision
betting_decisions = {}

for matchup, expected_runs in yahoo_expected_runs.items():
    if matchup in average_scores:
        avg_score = average_scores[matchup]
        frequency = matchup_frequency.get(matchup, 0)
        
        if expected_runs > avg_score:
            betting_decision = "Bet Over"
        else:
            betting_decision = "Bet Under"
        
        betting_decisions[matchup] = {
            'Expected Runs': expected_runs,
            'Average Score': avg_score,
            'Frequency': frequency,
            'Decision': betting_decision
        }
    else:
        betting_decisions[matchup] = {
            'Error': 'No historical data found'
        }

# Print betting decisions
for matchup, decision_info in betting_decisions.items():
    print(f"Matchup: {matchup}")
    print(f"Expected Runs: {decision_info['Expected Runs']}")
    print(f"Average Score: {decision_info['Average Score']}")
    print(f"Frequency of Matchup: {decision_info['Frequency']}")
    print(f"Decision: {decision_info['Decision']}")
    print()