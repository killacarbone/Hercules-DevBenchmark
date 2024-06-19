#file_operations.py

import csv
import logging
import os
from .rating_calculator import calculate_complexity_rating  # Adjusted import to match your structure


def get_data_file_path(filename):
    return os.path.join(os.path.dirname(__file__), '..', 'data', filename)


def update_predefined_ratings(game_identifier, ratings):
    logging.debug(f"Updating predefined ratings for {game_identifier}.")
    file_path = get_data_file_path('predefined_ratings.csv')
    try:
        with open(file_path, 'r', newline='', encoding='utf-8') as file:
            csv_reader = csv.reader(file)
            predefined_ratings = {rows[0]: rows[1] for rows in csv_reader}

        predefined_ratings[game_identifier] = ratings

        with open(file_path, 'w', newline='', encoding='utf-8') as file:
            csv_writer = csv.writer(file)
            for key, value in predefined_ratings.items():
                csv_writer.writerow([key, value])
                
        logging.info(f"Predefined ratings updated for {game_identifier}.")
    except Exception as e:
        logging.error(f"Error updating predefined ratings: {e}")
        

def save_ratings_to_file(ratings_dict):
    logging.debug("Saving ratings to file.")
    file_path = get_data_file_path('ratings.csv')
    try:
        with open(file_path, 'w', newline='', encoding='utf-8') as file:
            csv_writer = csv.writer(file)
            csv_writer.writerow([
                'Game Title', 'Genre', 'Graphics', 'Physics and Collision Detection',
                'Level Design and World Building', 'Gameplay Mechanics', 'AI and NPC Behavior',
                'Audio', 'UI and UX', 'Multiplayer and Networking', 'Scripting and Programming', 'Comments'
            ])
            for game, data in ratings_dict.items():
                csv_writer.writerow([
                    game, data['genre'],
                    data['ratings']['Graphics'], data['ratings']['Physics and Collision Detection'],
                    data['ratings']['Level Design and World Building'], data['ratings']['Gameplay Mechanics'],
                    data['ratings']['AI and NPC Behavior'], data['ratings']['Audio'],
                    data['ratings']['UI and UX'], data['ratings']['Multiplayer and Networking'],
                    data['ratings']['Scripting and Programming'], data['comments']
                ])
        logging.info("Ratings successfully saved to file.")
    except Exception as e:
        logging.error(f"Error saving ratings to file: {e}")
             

def load_ratings_from_csv(file_path):
    logging.debug(f"Loading ratings from file: {file_path}")
    ratings_dict = {}
    try:
        with open(file_path, mode='r', encoding='utf-8') as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                game_title = row['Game Title']
                genre = row['Genre']
                ratings = {
                    'Graphics': int(row['Graphics']),
                    'Physics and Collision Detection': int(row['Physics and Collision Detection']),
                    'Level Design and World Building': int(row['Level Design and World Building']),
                    'Gameplay Mechanics': int(row['Gameplay Mechanics']),
                    'AI and NPC Behavior': int(row['AI and NPC Behavior']),
                    'Audio': int(row['Audio']),
                    'UI and UX': int(row['UI and UX']),
                    'Multiplayer and Networking': int(row['Multiplayer and Networking']),
                    'Scripting and Programming': int(row['Scripting and Programming'])
                }
                comments = row['Comments']
                ratings_dict[game_title] = {
                    'genre': genre,
                    'ratings': ratings,
                    'normalized_score': 0,  # Initialize with 0, will be calculated later
                    'comments': comments
                }
        logging.info(f"Ratings loaded from file: {file_path}")
    except Exception as e:
        logging.error(f"Error reading CSV file: {e}")
    return ratings_dict


def normalize_ratings(ratings_dict):
    logging.debug("Starting normalization of ratings.")    
    if len(ratings_dict) <= 1:
        return ratings_dict
    
    all_scores = []
    for game, data in ratings_dict.items():
        genre = data['genre']
        ratings = data['ratings']
        score = calculate_complexity_rating(ratings, genre)
        data['normalized_score'] = score
        all_scores.append(score)

    min_score = min(all_scores)
    max_score = max(all_scores)
        
    normalized_ratings = {}
    for game, data in ratings_dict.items():
        normalized_score = (data['normalized_score'] - min_score) / (max_score - min_score) * 100 if max_score > min_score else 0
        normalized_ratings[game] = {
            'genre': data['genre'],
            'ratings': data['ratings'],
            'normalized_score': normalized_score,
            'comments': data['comments']
        }
        logging.debug(f"Normalized score for {game}: {normalized_score:.2f}")
    
    logging.info("Normalization of ratings completed.")
    return normalized_ratings


