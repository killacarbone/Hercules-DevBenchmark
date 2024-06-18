# src/dynamic_weights.py

import logging

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

# dynamic_weights.py

genre_criteria = {
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
    }
    # Add more genres and criteria as needed
}

def detect_genre(ratings):
    logging.debug(f"Detecting genre for ratings: {ratings}")
    scores = {genre: sum(min(ratings.get(factor, 0) / weight, 1) for factor, weight in criteria.items())
              for genre, criteria in genre_criteria.items()}
    for genre, criteria in genre_criteria.items():
        logging.debug(f"Evaluating criteria for genre: {genre}")
        for factor, weight in criteria.items():
            logging.debug(f"Factor: {factor}, Weight: {weight}, Current Score: {scores[genre]}")
    
    detected_genre = max(scores, key=scores.get)
    logging.debug(f"Detected genre: {detected_genre} with score: {scores[detected_genre]}")
    return detected_genre


