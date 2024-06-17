# game_rating_ui.py

import tkinter as tk
from tkinter import messagebox
import json
import logging
from .code_generator import parse_input_code
from .file_operations import update_predefined_ratings, save_ratings_to_file, load_ratings_from_file, normalize_ratings
from .rating_calculator import calculate_complexity_rating


# Setup logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')


class GameRatingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Game Development Complexity Rating System")
        
        self.label = tk.Label(root, text="Enter the game data in JSON format:")
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
            self.ratings_dict = load_ratings_from_file()
            self.update_listbox()
        except FileNotFoundError:
            self.ratings_dict = {}
            logging.warning("No existing ratings file found. Starting with an empty dictionary.")


    def update_listbox(self):
        self.listbox.delete(0, tk.END)
        sorted_ratings = sorted(self.ratings_dict.items(), key=lambda item: item[1], reverse=True)
        for i, (game, rating) in enumerate(sorted_ratings, start=1):
            self.listbox.insert(tk.END, f"{i}. {game}: {rating:.2f}")
        logging.debug("Listbox updated with sorted ratings.")


    def calculate_rating(self):
        input_data = self.text.get("1.0", tk.END)
        try:
            game_data = json.loads(input_data)
            game_identifier = game_data["game_identifier"]
            ratings = game_data["ratings"]
            update_predefined_ratings(game_identifier, ratings)
            score = calculate_complexity_rating(ratings)
            self.ratings_dict[game_identifier] = score
            normalized_ratings = normalize_ratings(self.ratings_dict)  # Normalize ratings
            save_ratings_to_file(normalized_ratings)  # Save normalized ratings
            self.update_listbox()
            logging.info(f"Rating calculated and saved for {game_identifier}: {normalized_ratings[game_identifier]:.2f}")
            messagebox.showinfo("Rating", f"Game Development Complexity Rating for {game_identifier}: {normalized_ratings[game_identifier]:.2f}")
        except (ValueError, json.JSONDecodeError) as e:
            messagebox.showerror("Invalid Code", str(e))
            logging.error(f"Error calculating rating: {e}")
        finally:
            self.text.delete("1.0", tk.END)


if __name__ == "__main__":    
    root = tk.Tk()
    app = GameRatingApp(root)
    root.mainloop()
