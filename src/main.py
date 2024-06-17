from code_generator import parse_input_code
from file_operations import update_predefined_ratings, save_ratings_to_file, load_ratings_from_file
from rating_calculator import calculate_complexity_rating

def main():
    print("Welcome to the Game Development Complexity Rating System")
    input_code = input("Enter the unique code for the game or genre you want to rate: ")
    
    try:
        game_identifier, ratings = parse_input_code(input_code)
    except ValueError:
        print("Invalid input format. Please enter a valid code.")
        return
    
    # Update predefined ratings
    update_predefined_ratings(game_identifier, ratings)
    
    # Calculate the complexity rating
    score = calculate_complexity_rating(ratings)
    print(f"Game Development Complexity Rating for {game_identifier}: {score:.2f} (out of 100)")
    
    # Load existing ratings from file
    ratings_dict = load_ratings_from_file()
    
    # Update the dictionary with the new rating
    ratings_dict[game_identifier] = score
    
    # Save updated ratings to file
    save_ratings_to_file(ratings_dict)

if __name__ == "__main__":
    main()
