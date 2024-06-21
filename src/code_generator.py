import logging  # Import logging module for logging messages

# Define dynamic weighting criteria for different game genres
dynamic_weighting_criteria = {
    'RPG': {
        'Graphics': 20,
        'Gameplay Mechanics': 25,
        'Story': 30,
        'Audio': 10,
        'UI and UX': 15
    },
    'Shooter': {
        'Graphics': 25,
        'Gameplay Mechanics': 30,
        'Multiplayer and Networking': 20,
        'Audio': 15,
        'UI and UX': 10
    },
    # Add more genres and criteria as needed
}

# List of rating factors
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

def generate_code(game_identifier, ratings):
    """Generate a unique code for a game based on its identifier and ratings."""
    # logging.debug(f"Generating code for game: {game_identifier}")  # Log the generation process
    
    code = game_identifier + '-'  # Start the code with the game identifier
    for factor in factors:
        code += str(ratings[factor]).zfill(4)  # Append each rating to the code, zero-padded to 4 digits
    
    # logging.debug(f"Generated code: {code}")  # Log the generated code
    return code  # Return the generated code

def parse_input_code(input_code):
    """Parse an input code to extract the game identifier and ratings."""
    # logging.debug(f"Parsing input code: {input_code}")  # Log the parsing process
    
    try:
        game_identifier, ratings_digits = input_code.split('-')  # Split the code into identifier and ratings
    except ValueError:
        # logging.error("Invalid input code format.")  # Log error if split fails
        raise ValueError("Invalid input code format. Ensure it contains a hyphen separating the game identifier and the ratings.")  # Raise an exception
    
    print(f"Game Identifier: {game_identifier}")  # Print the game identifier
    # logging.debug(f"Game Identifier: {game_identifier}")  # Log the game identifier
    print(f"Ratings Digits: {ratings_digits}")  # Print the ratings digits
    # logging.debug(f"Ratings Digits: {ratings_digits}")  # Log the ratings digits
    
    # Ensure the ratings_digits length is a multiple of 4 and matches the number of factors
    if len(ratings_digits) % 4 != 0 or len(ratings_digits) // 4 != len(factors):
        # logging.error("Ratings digits length is not a multiple of 4 or does not match the expected number of factors.")  # Log error if length is invalid
        raise ValueError("Invalid input code: incorrect digit length or number of ratings.")  # Raise an exception
    
    try:
        ratings_values = [int(ratings_digits[i:i+4]) for i in range(0, len(ratings_digits), 4)]  # Convert ratings to integers
    except ValueError:
        # logging.error("Ratings must be numeric values.")  # Log error if conversion fails
        raise ValueError("Invalid input code: ratings must be numeric values.")  # Raise an exception
    
    # logging.debug(f"Ratings Values: {ratings_values}")  # Log the ratings values
    print(f"Ratings Values: {ratings_values}")  # Print the ratings values
    
    # Map the parsed ratings to their respective factors
    ratings = dict(zip(factors, ratings_values))  # Create a dictionary of ratings
    # logging.debug(f"Parsed ratings: {ratings}")  # Log the parsed ratings
    
    return game_identifier, ratings  # Return the game identifier and ratings
