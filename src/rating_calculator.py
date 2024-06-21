import logging  # Import logging module for logging messages
from typing import Dict, Optional  # Import typing for type annotations
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

def scale_ratings(ratings: Dict[str, int]) -> Dict[str, float]:
    """Scale ratings to a 0-100 scale."""
    max_rating = 1000  # Maximum rating value
    scaled = {factor: (rating / max_rating) * 100 for factor, rating in ratings.items()}  # Scale each rating
    # print(f"Scaled Ratings: {scaled}")  # Debugging
    # logging.debug(f"Scaled Ratings: {scaled}")  # Log scaled ratings
    return scaled  # Return scaled ratings

def calculate_complexity_rating(ratings: Dict[str, int], genre: Optional[str] = None) -> float:
    """Calculate the complexity rating with optional genre-based weighting."""
    try:
        logging.info(f"Starting calculation for genre: {genre}")  # Log the start of calculation
        
        scaled_ratings = scale_ratings(ratings)  # Scale the ratings
        total_weighted_score = 0  # Initialize total weighted score
        
        # Select appropriate weights based on genre
        if genre and genre in dynamic_weighting_criteria:
            weights = dynamic_weighting_criteria[genre]  # Use dynamic weights
            logging.debug(f"Using dynamic weights for genre {genre}: {weights}")  # Log dynamic weights
        else:
            weights = factors_weights  # Use default weights
            logging.debug(f"Using default weights: {weights}")  # Log default weights
        
        # Calculate the maximum possible score for normalization
        max_possible_score = sum(weight * 100 for weight in weights.values())  # Calculate max possible score
        
        # Compute the weighted score
        for factor, weight in weights.items():
            rating = scaled_ratings.get(factor, 0)  # Get scaled rating for factor
            # logging.debug(f"Factor: {factor}, Weight: {weight}, Scaled Rating: {rating}")  # Log each factor's details
            total_weighted_score += rating * weight  # Add weighted rating to total
        
        normalized_score = (total_weighted_score / max_possible_score) * 100  # Normalize the score to 0-100
        logging.info(f"Calculated normalized score: {normalized_score}")  # Log the calculated score
        
        return normalized_score  # Return the normalized score
    except Exception as e:
        logging.error(f"Error in calculating complexity rating: {e}")  # Log any errors
        raise  # Re-raise the exception

# Initialize logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# For testing
# if __name__ == "__main__":
#     sample_ratings = {
#         'Graphics': 900,
#         'Physics and Collision Detection': 850,
#         'Level Design and World Building': 920,
#         'Gameplay Mechanics': 880,
#         'AI and NPC Behavior': 800,
#         'Audio': 850,
#         'UI and UX': 820,
#         'Multiplayer and Networking': 700,
#         'Scripting and Programming': 860
#     }

#     print(calculate_complexity_rating(sample_ratings, genre='RPG'))  # Test calculation for RPG
#     print(calculate_complexity_rating(sample_ratings, genre='Shooter'))  # Test calculation for Shooter
#     print(calculate_complexity_rating(sample_ratings))  # Test calculation with no genre