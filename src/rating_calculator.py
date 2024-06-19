# rating_calculator.py 

import logging
from typing import Dict, Optional
from .dynamic_weights import dynamic_weighting_criteria  # Ensure this import is present


# Define factors weights for the default calculation
factors_weights: Dict[str, int] = {
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


# Function to scale ratings from a maximum rating value
def scale_ratings(ratings: Dict[str, int]) -> Dict[str, float]:
    max_rating = 1000  # Maximum rating value
    scaled = {factor: (rating / max_rating) * 100 for factor, rating in ratings.items()}
    print(f"Scaled Ratings: {scaled}")  # Debugging
    logging.debug(f"Scaled Ratings: {scaled}")  # Reduced extensive debug log
    return scaled


# Function to calculate the complexity rating with optional genre-based weighting
def calculate_complexity_rating(ratings: Dict[str, int], genre: Optional[str] = None) -> float:
    try:
        logging.info(f"Starting calculation for genre: {genre}")
        
        scaled_ratings = scale_ratings(ratings)
        total_weighted_score = 0
        
        # Select appropriate weights based on genre
        if genre and genre in dynamic_weighting_criteria:
            weights = dynamic_weighting_criteria[genre]
            logging.debug(f"Using dynamic weights for genre {genre}: {weights}")
        else:
            weights = factors_weights
            logging.debug(f"Using default weights: {weights}")
        
        # Calculate the maximum possible score for normalization
        max_possible_score = sum(weight * 100 for weight in weights.values())
        
        # Compute the weighted score based on scaled ratings and selected weights
        for factor, weight in weights.items():
            rating = scaled_ratings.get(factor, 0)
            logging.debug(f"Factor: {factor}, Weight: {weight}, Scaled Rating: {rating}")
            total_weighted_score += rating * weight
        
        # Normalize the total weighted score to a percentage
        normalized_score = (total_weighted_score / max_possible_score) * 100
        logging.info(f"Calculated normalized score: {normalized_score}")
        
        return normalized_score
    except Exception as e:
        logging.error(f"Error in calculating complexity rating: {e}")
        raise

# Initialize logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# For testing, you might want to add a small section to call the functions and observe the logs
if __name__ == "__main__":
    # Sample ratings for testing
    sample_ratings = {
        'Graphics': 900,
        'Physics and Collision Detection': 850,
        'Level Design and World Building': 920,
        'Gameplay Mechanics': 880,
        'AI and NPC Behavior': 800,
        'Audio': 850,
        'UI and UX': 820,
        'Multiplayer and Networking': 700,
        'Scripting and Programming': 860
    }

    # Test calculation for an RPG game
    print(calculate_complexity_rating(sample_ratings, genre='RPG'))

    # Test calculation for a Shooter game
    print(calculate_complexity_rating(sample_ratings, genre='Shooter'))

    # Test calculation with no genre specified (should use default weights)
    print(calculate_complexity_rating(sample_ratings))