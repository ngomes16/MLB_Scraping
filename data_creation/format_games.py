from collections import defaultdict

# Initialize a defaultdict with list to store the formatted data
formatted_data = defaultdict(list)

# Open the games_sample.txt file for reading
with open('games_data/games_sample.txt', 'r') as file:
    # Iterate over each line in the file
    for line in file:
        # Skip empty lines
        if line.strip() == "":
            continue
        
        print(f"Processing line: {line.strip()}")  # Debugging print statement
        # Split the line by ", " to separate the matchup and number
        parts = line.strip().split(", ")
        if len(parts) == 2:
            matchup = parts[0]
            number = float(parts[1])

            # Split the matchup by " @ " to separate the team names
            teams = matchup.split(" @ ")
            if len(teams) == 2:
                team1 = teams[0].strip()
                team2 = teams[1].strip()

                # Ensure consistent order for the matchup key
                key = tuple(sorted([team1, team2]))

                # Append the number to the list associated with the key
                formatted_data[key].append(number)
                print(f"Updated dictionary: {key} -> {formatted_data[key]}")  # Debugging print statement

# Print the formatted data dictionary
print("Formatted Data:")
for key, value in formatted_data.items():
    print(f"{key}: {value}")
