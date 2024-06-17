import json
import logging
import os

def get_data_file_path(filename):
    return os.path.join(os.path.dirname(__file__), '..', 'data', filename)

def update_predefined_ratings(game_identifier, ratings):
    file_path = get_data_file_path('predefined_ratings.json')
    try:
        with open(file_path, 'r') as file:
            predefined_ratings = json.load(file)
    except FileNotFoundError:
        predefined_ratings = {}
    
    predefined_ratings[game_identifier] = ratings
    
    with open(file_path, 'w') as file:
        json.dump(predefined_ratings, file, indent=4)

def save_ratings_to_file(ratings_dict):
    file_path = get_data_file_path('ratings.txt')
    with open(file_path, 'w') as file:
        for game, rating in ratings_dict.items():
            file.write(f"{game}: {rating:.2f}\n")

def load_ratings_from_file():
    file_path = get_data_file_path('ratings.txt')
    try:
        with open(file_path, 'r') as file:
            ratings_dict = {line.split(': ')[0]: float(line.split(': ')[1]) for line in file.readlines() if ': ' in line}
    except FileNotFoundError:
        ratings_dict = {}
    return ratings_dict

def normalize_ratings(ratings_dict):
    logging.debug(f"Original Ratings: {ratings_dict}")
    all_scores = list(ratings_dict.values())
    min_score = min(all_scores)
    max_score = max(all_scores)
    logging.debug(f"Min Score: {min_score}, Max Score: {max_score}")
    
    normalized_ratings = {}
    for game, score in ratings_dict.items():
        normalized_score = (score - min_score) / (max_score - min_score) * 100
        normalized_ratings[game] = normalized_score
        logging.debug(f"Normalized score for {game}: {normalized_score:.2f}")
    
    logging.debug(f"Normalized Ratings: {normalized_ratings}")
    return normalized_ratings



