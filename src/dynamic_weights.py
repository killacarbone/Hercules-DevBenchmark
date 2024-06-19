# dynamic_weights.py

import logging
from typing import Dict, Any, Optional

# Define dynamic weighting criteria
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
    """
    Detects the genre of a game based on provided ratings.

    Parameters:
        ratings (dict): A dictionary of ratings for various factors.

    Returns:
        str: The detected genre.
    """
    try:
        logging.debug("Starting genre detection.")
        logging.debug(f"Ratings provided: {ratings}")

        # Calculate scores for each genre
        scores = {genre: sum(min(ratings.get(factor, 0) / weight, 1) for factor, weight in criteria.items())
                  for genre, criteria in dynamic_weighting_criteria.items()}

        detected_genre = max(scores, key=scores.get)
        logging.info(f"Detected genre: {detected_genre} with score: {scores[detected_genre]}")
        return detected_genre
    except Exception as e:
        logging.error(f"Error detecting genre: {e}")
        return None

