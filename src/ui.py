import tkinter as tk  # Import tkinter for GUI
import logging  # Import logging module for logging messages
import csv  # Import CSV module for handling CSV files
from tkinter import messagebox  # Import messagebox for dialog boxes
from src.file_operations import update_predefined_ratings, save_ratings_to_file, normalize_ratings  # Import functions from file_operations
from src.rating_calculator import calculate_complexity_rating  # Import calculate_complexity_rating function
from src.db_operations import insert_game, insert_rating, select_all_games, select_all_ratings  # Import functions from db_operations
from src.dynamic_weights import detect_genre  # Import detect_genre function

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class GameRatingApp:
    def __init__(self, root, conn):
        """ Initialize the GUI application. """
        self.root = root
        self.conn = conn  # Database connection
        self.root.title("Game Development Complexity Rating System")  # Set the window title
        
        # UI elements
        self.label = tk.Label(root, text="Enter the game data in CSV format:")  # Label
        self.label.pack()
        
        self.text = tk.Text(root, height=10, width=50)  # Text box for input
        self.text.pack()
        
        self.button = tk.Button(root, text="Calculate Rating", command=self.calculate_rating)  # Button to trigger rating calculation
        self.button.pack()
        
        self.listbox = tk.Listbox(root, width=70, height=20)  # Listbox to display ratings
        self.listbox.pack()
        
        self.ratings_dict = {}  # Dictionary to store ratings
        self.load_ratings_from_db()  # Load existing ratings from the database
        self.update_listbox()  # Update the listbox with loaded ratings
    
    def load_ratings_from_db(self):
        """ Load ratings from the database and update the listbox. """
        if self.conn:
            try:
                games = select_all_games(self.conn)  # Query all games from the database
                ratings = select_all_ratings(self.conn)  # Query all ratings from the database

                # Debugging statements to check data fetched
                logging.debug(f"Games fetched: {games}")
                logging.debug(f"Ratings fetched: {ratings}")

                if not games or not ratings:
                    logging.error("Failed to load games or ratings from the database.")
                    return

                logging.info(f"Loaded {len(games)} games from the database.")
                logging.info(f"Loaded {len(ratings)} ratings from the database.")

                for game in games:
                    game_id, title, genre, comments = game
                    game_ratings = {factor: score for _, _, factor, score in ratings if _ == game_id}
                    logging.debug(f"Game ID: {game_id}, Title: {title}, Ratings: {game_ratings}")

                    self.ratings_dict[title] = {
                        'genre': genre,
                        'ratings': game_ratings,
                        'normalized_score': 0,  # Will be updated after normalization
                        'comments': comments
                    }

                self.ratings_dict = normalize_ratings(self.ratings_dict)  # Normalize the ratings
                self.update_listbox()  # Update the listbox with normalized ratings
                logging.info("Ratings loaded and normalized from the database.")
            except Exception as e:
                logging.error(f"Error loading ratings from the database: {e}")

    def update_listbox(self):
        """ Update the listbox with sorted ratings. """
        self.listbox.delete(0, tk.END)  # Clear the listbox
        sorted_ratings = sorted(self.ratings_dict.items(), key=lambda item: item[1]['normalized_score'], reverse=True)
        for i, (game, data) in enumerate(sorted_ratings, start=1):
            self.listbox.insert(tk.END, f"{i}. {game}: {data['normalized_score']:.2f}")  # Insert sorted ratings into listbox
        logging.debug("Listbox updated with sorted ratings.")

    def calculate_rating(self):
        """ Calculate and display the game rating based on input data. """
        input_data = self.text.get("1.0", tk.END)  # Get input data from text box
        
        try:
            csv_reader = csv.DictReader(input_data.strip().split('\n'))  # Read CSV data from input
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
                
                logging.debug(f"Processing game: {game_title}, Genre: {genre}")

                detected_genre = detect_genre(ratings)  # Detect the genre based on ratings
                logging.debug(f"Detected genre: {detected_genre}")
                
                update_predefined_ratings(game_title, ratings)  # Update predefined ratings
                score = calculate_complexity_rating(ratings, detected_genre)  # Calculate complexity rating
                logging.info(f"Calculated score for {game_title}: {score}")

                self.ratings_dict[game_title] = {
                    'genre': detected_genre,
                    'ratings': ratings,
                    'normalized_score': score,
                    'comments': comments
                }

                self.ratings_dict = normalize_ratings(self.ratings_dict)  # Normalize ratings
                save_ratings_to_file(self.ratings_dict)  # Save ratings to file
                self.update_listbox()  # Update the listbox
                messagebox.showinfo("Rating", f"Game Development Complexity Rating for {game_title}: {self.ratings_dict[game_title]['normalized_score']:.2f}")  # Show rating

                # Insert into database
                game_id = insert_game(self.conn, (game_title, genre, comments))  # Insert game into database
                for factor, score in ratings.items():
                    insert_rating(self.conn, (game_id, factor, score))  # Insert ratings into database
                    
        except Exception as e:
            messagebox.showerror("Error", f"Unexpected error: {e}")  # Show error message
            logging.error(f"Unexpected error: {e}")
        finally:
            self.text.delete("1.0", tk.END)  # Clear the text box
