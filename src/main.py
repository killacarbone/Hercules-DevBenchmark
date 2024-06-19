#main.py 

import logging
from .code_generator import parse_input_code
from .file_operations import update_predefined_ratings, save_ratings_to_file, load_ratings_from_file
from .rating_calculator import calculate_complexity_rating


# Configure logging
logging.basicConfig(
    level=logging.DEBUG,  # Change this to logging.INFO to reduce verbosity in production
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("app.log"),
        logging.StreamHandler()
    ]
)
    
    
def main():
    print("Welcome to the Game Development Complexity Rating System")
    input_code = input("Enter the unique code for the game or genre you want to rate: ")

    try:
        game_identifier, ratings = parse_input_code(input_code)
        logging.info(f"Parsed input code. Game Identifier: {game_identifier}, Ratings: {ratings}")
    except ValueError as e:
        logging.error(f"Error parsing input code: {e}")
        print("Invalid input format. Please enter a valid code.")
        return

    try:
        # Update predefined ratings
        update_predefined_ratings(game_identifier, ratings)
        logging.info(f"Updated predefined ratings for {game_identifier}")

        # Calculate the complexity rating
        score = calculate_complexity_rating(ratings)
        print(f"Game Development Complexity Rating for {game_identifier}: {score:.2f} (out of 100)")
        logging.info(f"Calculated complexity rating for {game_identifier}: {score:.2f}")

        # Load existing ratings from file
        ratings_dict = load_ratings_from_file()
        logging.info("Loaded existing ratings from file")

        # Update the dictionary with the new rating
        ratings_dict[game_identifier] = score
        logging.debug(f"Updated ratings dictionary: {ratings_dict}")

        # Save updated ratings to file
        save_ratings_to_file(ratings_dict)
        logging.info(f"Saved updated ratings to file for {game_identifier}")
    except Exception as e:
        logging.error(f"An error occurred: {e}")
        print("An error occurred while processing your request. Please try again later.")

if __name__ == "__main__":
    main()
