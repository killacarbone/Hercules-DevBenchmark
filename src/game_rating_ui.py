# game_rating_ui.py

import tkinter as tk
from tkinter import messagebox
import csv
import logging
from .code_generator import parse_input_code
from .file_operations import get_data_file_path, update_predefined_ratings, save_ratings_to_file, load_ratings_from_csv, normalize_ratings
from .rating_calculator import calculate_complexity_rating
from .dynamic_weights import dynamic_weighting_criteria, detect_genre  # Import the dynamic weighting criteria


# Setup logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')


class GameRatingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Game Development Complexity Rating System")
        
        self.label = tk.Label(root, text="Enter the game data in CSV format:")
        self.label.pack()
        
        self.text = tk.Text(root, height=10, width=50)
        self.text.pack()
        
        self.button = tk.Button(root, text="Calculate Rating", command=self.calculate_rating)
        self.button.pack()
        
        self.listbox = tk.Listbox(root, width=70, height=20)
        self.listbox.pack()
        
        self.ratings_dict = {}
        self.load_ratings()
        

    def load_ratings(self):
        try:
            file_path = get_data_file_path('ratings.csv')
            self.ratings_dict = load_ratings_from_csv(file_path)
            self.ratings_dict = normalize_ratings(self.ratings_dict)
            self.update_listbox()
        except FileNotFoundError:
            self.ratings_dict = {}
            logging.warning("No existing ratings file found. Starting with an empty dictionary.")


    def update_listbox(self):
        self.listbox.delete(0, tk.END)
        sorted_ratings = sorted(self.ratings_dict.items(), key=lambda item: item[1]['normalized_score'], reverse=True)
        for i, (game, data) in enumerate(sorted_ratings, start=1):
            self.listbox.insert(tk.END, f"{i}. {game}: {data['normalized_score']:.2f}")
        logging.debug("Listbox updated with sorted ratings.")


    def calculate_rating(self):
        input_data = self.text.get("1.0", tk.END)
        try:
            # Load CSV data from input
            csv_reader = csv.DictReader(input_data.strip().split('\n'))
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

                # Debug print to verify input data structure
                logging.debug(f"Processing game: {game_title}, Genre: {genre}, Ratings: {ratings}, Comments: {comments}")

                # Determine genre
                detected_genre = detect_genre(ratings)
                logging.debug(f"Selected/Detected genre: {detected_genre}")

                # Update predefined ratings
                update_predefined_ratings(game_title, ratings)
                score = calculate_complexity_rating(ratings, detected_genre)
                logging.debug(f"Calculated score: {score} for game: {game_title}")

                self.ratings_dict[game_title] = {
                    'genre': detected_genre,
                    'ratings': ratings,
                    'normalized_score': score,
                    'comments': comments
                }

                normalized_ratings = normalize_ratings(self.ratings_dict)
                logging.debug(f"Normalized Ratings: {normalized_ratings}")
                save_ratings_to_file(normalized_ratings)  # Save normalized ratings
                self.ratings_dict = normalized_ratings  # Update the ratings_dict with normalized ratings
                self.update_listbox()
                logging.info(f"Rating calculated and saved for {game_title}: {normalized_ratings[game_title]['normalized_score']:.2f}")
                messagebox.showinfo("Rating", f"Game Development Complexity Rating for {game_title}: {normalized_ratings[game_title]['normalized_score']:.2f}")
        except Exception as e:
            messagebox.showerror("Error", f"Unexpected error: {e}")
            logging.error(f"Unexpected error: {e}")
        finally:
            self.text.delete("1.0", tk.END)


if __name__ == "__main__":    
    root = tk.Tk()
    app = GameRatingApp(root)
    root.mainloop()
