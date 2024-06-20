import logging  # Import logging module for logging messages
from typing import Dict, Any, Optional  # Import typing for type annotations

# Define dynamic weighting criteria for different game genres
dynamic_weighting_criteria: Dict[str, Dict[str, int]] = {
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

def detect_genre(ratings: Dict[str, Any]) -> Optional[str]:
    """ Detect the genre of a game based on provided ratings. """
    try:
        logging.debug("Starting genre detection.")  # Log the start of genre detection
        logging.debug(f"Ratings provided: {ratings}")  # Log the provided ratings

        # Calculate scores for each genre
        scores = {genre: sum(min(ratings.get(factor, 0) / weight, 1) for factor, weight in criteria.items())
                  for genre, criteria in dynamic_weighting_criteria.items()}  # Calculate scores for genres

        detected_genre = max(scores, key=scores.get)  # Detect genre with highest score
        logging.info(f"Detected genre: {detected_genre} with score: {scores[detected_genre]}")  # Log detected genre
        return detected_genre  # Return the detected genre
    except Exception as e:
        logging.error(f"Error detecting genre: {e}")  # Log any errors
        return None  # Return None if an error occurs
