import logging

factors_weights = {
    'Graphics': 10,
    'Physics and Collision Detection': 9,
    'Level Design and World Building': 10,
    'Gameplay Mechanics': 10,
    'AI and NPC Behavior': 9,
    'Audio': 9,
    'UI and UX': 9,
    'Multiplayer and Networking': 5,
    'Scripting and Programming': 10
}

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

def scale_ratings(ratings):
    max_rating = 1000  # Maximum rating value
    scaled = {factor: (rating / max_rating) * 100 for factor, rating in ratings.items()}
    print(f"Scaled Ratings: {scaled}")  # Debugging
    return scaled

def calculate_complexity_rating(ratings, genre=None):
    scaled_ratings = scale_ratings(ratings)
    total_weighted_score = 0
    
    if genre and genre in dynamic_weighting_criteria:
        weights = dynamic_weighting_criteria[genre]
        logging.debug(f"Using dynamic weights for genre {genre}: {weights}")
    else:
        weights = factors_weights
        logging.debug(f"Using default weights: {weights}")
    
    max_possible_score = sum(weight * 100 for weight in weights.values())
    
    for factor, weight in weights.items():
        rating = scaled_ratings.get(factor, 0)
        total_weighted_score += rating * weight
    
    normalized_score = (total_weighted_score / max_possible_score) * 100
    logging.debug(f"Calculated normalized score: {normalized_score}")
    return normalized_score
