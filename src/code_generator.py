def generate_code(game_identifier, ratings):
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
    
    code = game_identifier + '-'
    for factor in factors:
        code += str(ratings[factor]).zfill(4)  # Pad with zeros for consistent length
    
    return code

def parse_input_code(input_code):
    try:
        game_identifier, ratings_digits = input_code.split('-')
    except ValueError:
        raise ValueError("Invalid input code format. Ensure it contains a hyphen separating the game identifier and the ratings.")
    
    print(f"Game Identifier: {game_identifier}")
    print(f"Ratings Digits: {ratings_digits}")
    
    # Ensure the ratings_digits length is a multiple of 4 and matches the number of factors
    if len(ratings_digits) % 4 != 0:
        print(f"Error: Ratings digits length ({len(ratings_digits)}) is not a multiple of 4.")
        raise ValueError("Invalid input code: incorrect digit length.")
    
    if len(ratings_digits) // 4 != 9:
        print(f"Error: Number of ratings ({len(ratings_digits) // 4}) does not match expected number of factors (9).")
        raise ValueError("Invalid input code: incorrect number of ratings.")
    
    try:
        ratings_values = [
            int(ratings_digits[i:i+4]) for i in range(0, len(ratings_digits), 4)
        ]
    except ValueError:
        raise ValueError("Invalid input code: ratings must be numeric values.")
    
    print(f"Ratings Values: {ratings_values}")
    
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
    
    # Ensure the length of ratings_values matches the number of factors
    if len(ratings_values) != len(factors):
        print(f"Error: Number of parsed ratings ({len(ratings_values)}) does not match number of factors ({len(factors)}).")
        raise ValueError("Invalid input code: incorrect number of ratings.")
    
    ratings = dict(zip(factors, ratings_values))
    
    print(f"Parsed Ratings: {ratings}")
    
    return game_identifier, ratings




    


