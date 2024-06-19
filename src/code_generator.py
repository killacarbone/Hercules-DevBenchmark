#code_generator.py

import logging

    
# Define dynamic weighting criteria
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
    logging.debug(f"Generating code for game: {game_identifier}")
    
    code = game_identifier + '-'
    for factor in factors:
        code += str(ratings[factor]).zfill(4)  # Pad with zeros for consistent length    
    logging.debug(f"Generated code: {code}")
    return code

def parse_input_code(input_code):
    logging.debug(f"Parsing input code: {input_code}")
    
    try:
        game_identifier, ratings_digits = input_code.split('-')
    except ValueError:
        logging.error("Invalid input code format.")
        raise ValueError("Invalid input code format. Ensure it contains a hyphen separating the game identifier and the ratings.")
    
    print(f"Game Identifier: {game_identifier}")
    logging.debug(f"Game Identifier: {game_identifier}")
    print(f"Ratings Digits: {ratings_digits}")
    logging.debug(f"Ratings Digits: {ratings_digits}")
    
    # Ensure the ratings_digits length is a multiple of 4 and matches the number of factors
    if len(ratings_digits) % 4 != 0 or len(ratings_digits) // 4 != len(factors):
        logging.error("Ratings digits length is not a multiple of 4 or does not match the expected number of factors.")
        raise ValueError("Invalid input code: incorrect digit length or number of ratings.")
    
    try:
        ratings_values = [int(ratings_digits[i:i+4]) for i in range(0, len(ratings_digits), 4)]
    except ValueError:
        logging.error("Ratings must be numeric values.")
        raise ValueError("Invalid input code: ratings must be numeric values.")
    
    logging.debug(f"Ratings Values: {ratings_values}")
    print(f"Ratings Values: {ratings_values}")
    
    # Map the parsed ratings to their respective factors
    ratings = dict(zip(factors, ratings_values))
    logging.debug(f"Parsed ratings: {ratings}")
    
    return game_identifier, ratings




    


