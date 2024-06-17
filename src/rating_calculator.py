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

def scale_ratings(ratings):
    max_rating = 1000  # Maximum rating value
    scaled = {factor: (rating / max_rating) * 100 for factor, rating in ratings.items()}
    print(f"Scaled Ratings: {scaled}")  # Debugging
    return scaled

def calculate_complexity_rating(ratings):
    scaled_ratings = scale_ratings(ratings)
    total_weighted_score = 0
    max_possible_score = sum(weight * 100 for weight in factors_weights.values())
    
    for factor, weight in factors_weights.items():
        rating = scaled_ratings.get(factor, 0)
        total_weighted_score += rating * weight

    normalized_score = (total_weighted_score / max_possible_score) * 100
    return normalized_score
