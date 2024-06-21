import csv  # Import CSV module for handling CSV files
import logging  # Import logging module for logging messages
import os  # Import os module for file path operations
import sqlite3  # Import sqlite3 module for SQLite database operations
from sqlite3 import Error  # Import Error class from sqlite3
from .rating_calculator import calculate_complexity_rating  # Import calculate_complexity_rating function

def get_data_file_path(filename):
    """Construct the full path to a data file."""
    return os.path.join(os.path.dirname(__file__), '..', 'data', filename)  # Construct and return the full file path

def get_predefined_db_path():
    """Return the path to the predefined ratings database."""
    return r"C:\Users\steph\Documents\Hercules DevBenchmark\hercules devbenchmark database\db\predefined_ratings.db"

def create_predefined_db_connection(db_file):
    """Create a database connection to the SQLite database specified by db_file."""
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        logging.info(f"Connected to SQLite database: {db_file}")
    except Error as e:
        logging.error(e)
    return conn

def create_predefined_tables(conn):
    """Create predefined ratings table in the SQLite database."""
    sql_create_predefined_ratings_table = """ CREATE TABLE IF NOT EXISTS PredefinedRatings (
                                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                                game_identifier TEXT NOT NULL,
                                                graphics INTEGER,
                                                physics INTEGER,
                                                level_design INTEGER,
                                                gameplay_mechanics INTEGER,
                                                ai_behavior INTEGER,
                                                audio INTEGER,
                                                ui_ux INTEGER,
                                                multiplayer INTEGER,
                                                scripting INTEGER
                                            ); """
    try:
        c = conn.cursor()
        c.execute(sql_create_predefined_ratings_table)
        logging.info("Predefined ratings table created or already exists.")
    except Error as e:
        logging.error(e)

def update_predefined_ratings_db(game_identifier, ratings):
    """Update predefined ratings in the database for a given game."""
    db_path = get_predefined_db_path()
    conn = create_predefined_db_connection(db_path)
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute("""
                INSERT OR REPLACE INTO PredefinedRatings 
                (game_identifier, graphics, physics, level_design, gameplay_mechanics, ai_behavior, audio, ui_ux, multiplayer, scripting)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                game_identifier, 
                ratings['Graphics'], 
                ratings['Physics and Collision Detection'], 
                ratings['Level Design and World Building'], 
                ratings['Gameplay Mechanics'], 
                ratings['AI and NPC Behavior'], 
                ratings['Audio'], 
                ratings['UI and UX'], 
                ratings['Multiplayer and Networking'], 
                ratings['Scripting and Programming']
            ))
            conn.commit()
            logging.info(f"Predefined ratings updated for {game_identifier}.")
        except Error as e:
            logging.error(f"Error updating predefined ratings in the database: {e}")
        finally:
            conn.close()

def save_ratings_to_file(ratings_dict):
    """Save the ratings dictionary to a CSV file."""
    file_path = get_data_file_path('ratings.csv')  # Get the path to the ratings CSV file
    try:
        with open(file_path, 'w', newline='', encoding='utf-8') as file:  # Open the CSV file for writing
            csv_writer = csv.writer(file)  # Create a CSV writer object
            csv_writer.writerow([
                'Game Title', 'Genre', 'Graphics', 'Physics and Collision Detection',
                'Level Design and World Building', 'Gameplay Mechanics', 'AI and NPC Behavior',
                'Audio', 'UI and UX', 'Multiplayer and Networking', 'Scripting and Programming', 'Comments'
            ])  # Write the header row to the CSV file
            for game, data in ratings_dict.items():
                csv_writer.writerow([
                    game, data['genre'],
                    data['ratings']['Graphics'], data['ratings']['Physics and Collision Detection'],
                    data['ratings']['Level Design and World Building'], data['ratings']['Gameplay Mechanics'],
                    data['ratings']['AI and NPC Behavior'], data['ratings']['Audio'],
                    data['ratings']['UI and UX'], data['ratings']['Multiplayer and Networking'],
                    data['ratings']['Scripting and Programming'], data['comments']
                ])  # Write each game's ratings to the CSV file
        logging.info("Ratings successfully saved to file.")  # Log successful save
    except Exception as e:
        logging.error(f"Error saving ratings to file: {e}")  # Log any errors that occur

def load_ratings_from_file():
    """Load existing ratings from the ratings file."""
    file_path = get_data_file_path('ratings.csv')  # Get the path to the ratings CSV file
    ratings_dict = {}
    try:
        with open(file_path, mode='r', encoding='utf-8') as file:  # Open the CSV file for reading
            csv_reader = csv.DictReader(file)  # Create a CSV dictionary reader object
            for row in csv_reader:
                game_title = row['Game Title']  # Extract the game title
                genre = row['Genre']  # Extract the genre
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
                }  # Extract and convert the ratings
                comments = row['Comments']  # Extract the comments
                ratings_dict[game_title] = {
                    'genre': genre,
                    'ratings': ratings,
                    'normalized_score': 0,  # Initialize normalized score
                    'comments': comments
                }  # Add the game ratings to the dictionary
        logging.info(f"Ratings loaded from file: {file_path}")  # Log successful load
    except Exception as e:
        logging.error(f"Error reading CSV file: {e}")  # Log any errors that occur
    return ratings_dict  # Return the ratings dictionary

def normalize_ratings(ratings_dict):
    """Normalize the ratings to a 0-100 scale."""
    logging.debug("Starting normalization of ratings.")  # Log the normalization operation
    if len(ratings_dict) <= 1:
        return ratings_dict  # Return the original dictionary if it has 1 or fewer entries
    
    all_scores = []
    for game, data in ratings_dict.items():
        genre = data['genre']  # Get the genre of the game
        ratings = data['ratings']  # Get the ratings of the game
        score = calculate_complexity_rating(ratings, genre)  # Calculate the complexity rating
        data['normalized_score'] = score  # Set the normalized score
        all_scores.append(score)  # Add the score to the list of all scores

    min_score = min(all_scores)  # Find the minimum score
    max_score = max(all_scores)  # Find the maximum score
    
    logging.debug(f"All scores before normalization: {all_scores}")
    logging.debug(f"Min score: {min_score}, Max score: {max_score}")

        
    normalized_ratings = {}
    for game, data in ratings_dict.items():
        normalized_score = (data['normalized_score'] - min_score) / (max_score - min_score) * 100 if max_score > min_score else 0  # Normalize the score
        normalized_ratings[game] = {
            'genre': data['genre'],
            'ratings': data['ratings'],
            'normalized_score': normalized_score,  # Set the normalized score
            'comments': data['comments']
        }  # Add the normalized ratings to the dictionary
        logging.debug(f"Normalized score for {game}: {normalized_score:.2f}")  # Log the normalized score
    
    logging.info("Normalization of ratings completed.")  # Log successful normalization
    return normalized_ratings  # Return the dictionary with normalized ratings