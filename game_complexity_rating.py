import json

# Load predefined ratings from JSON file
try:
    with open('predefined_ratings.json', 'r') as file:
        predefined_ratings = json.load(file)
except FileNotFoundError:
    predefined_ratings = {}

# Define the factors and weights
factors_weights = {
    'Graphics': 20,
    'Physics and Collision Detection': 10,
    'Level Design and World Building': 15,
    'Gameplay Mechanics': 20,
    'AI and NPC Behavior': 10,
    'Audio': 5,
    'UI and UX': 10,
    'Multiplayer and Networking': 5,
    'Scripting and Programming': 10
}

# Function to calculate the complexity rating
def calculate_complexity_rating(ratings):
    total_weighted_score = 0
    max_score = 0

    for factor, weight in factors_weights.items():
        rating = ratings.get(factor, 0)
        total_weighted_score += rating * weight
        max_score += 10 * weight

    normalized_score = (total_weighted_score / max_score) * 100
    return normalized_score

# Function to save ratings to a file
def save_ratings_to_file(ratings_dict, filename="ratings.txt"):
    sorted_ratings = sorted(ratings_dict.items(), key=lambda item: item[1], reverse=True)
    with open(filename, 'w') as file:
        for code, score in sorted_ratings:
            file.write(f"{code}: {score:.2f}\n")

# Function to parse the input code and extract ratings
def parse_input_code(input_code):
    # Extract the game identifier (first part of the code until the digits start)
    import re
    match = re.match(r"([a-zA-Z]+)(\d+)", input_code)
    if not match:
        raise ValueError("Invalid code format")
    
    game_identifier = match.group(1)
    ratings_digits = match.group(2)
    
    # Extract the ratings (remaining part of the code)
    ratings_values = [int(digit) for digit in ratings_digits]
    
    # Define the order of the factors
    factors = [
        'Graphics',
        'Physics and Collision Detection',
        'Level Design and World Building',
        'Gameplay Mechanics',
        'AI and NPC Behavior',
        'Audio',
        'UI and UX',
        'Multiplayer and Networking',
        'Scripting and Programming'
    ]
    
    # Create a dictionary of ratings
    ratings = dict(zip(factors, ratings_values))
    
    return game_identifier, ratings

# Function to update the predefined ratings dictionary and file
def update_predefined_ratings(code, ratings):
    predefined_ratings[code] = ratings

    # Save updated predefined ratings to file
    with open('predefined_ratings.json', 'w') as file:
        json.dump(predefined_ratings, file, indent=4)

# Main function to run the program
def main():
    print("Welcome to the Game Development Complexity Rating System")
    input_code = input("Enter the unique code for the game or genre you want to rate: ")
    
    try:
        game_identifier, ratings = parse_input_code(input_code)
    except ValueError:
        print("Invalid input format. Please enter a valid code.")
        return

    # Update predefined ratings
    update_predefined_ratings(game_identifier, ratings)
    
    # Calculate the complexity rating
    score = calculate_complexity_rating(ratings)
    print(f"Game Development Complexity Rating for {game_identifier}: {score:.2f} (out of 100)")

    # Load existing ratings from file
    try:
        with open("ratings.txt", 'r') as file:
            ratings_dict = {line.split(': ')[0]: float(line.split(': ')[1]) for line in file.readlines()}
    except FileNotFoundError:
        ratings_dict = {}

    # Update the dictionary with the new rating
    ratings_dict[game_identifier] = score

    # Save updated ratings to file
    save_ratings_to_file(ratings_dict)

if __name__ == "__main__":
    main()
