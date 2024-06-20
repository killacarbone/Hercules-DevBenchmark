import logging  # Import logging module for logging messages
from src.file_operations import get_data_file_path  # Import function from file_operations module
from src.db_operations import create_connection, create_table  # Import functions from db_operations module
from src.ui import GameRatingApp  # Import the GameRatingApp class
import tkinter as tk  # Import tkinter for GUI

# Configure logging
logging.basicConfig(
    level=logging.DEBUG,  # Set logging level to DEBUG
    format='%(asctime)s - %(levelname)s - %(message)s',  # Set logging format
    handlers=[
        logging.FileHandler("app.log"),  # Log to a file named app.log
        logging.StreamHandler()  # Log to the console
    ]
)

def initialize_database():
    """Initialize the SQLite database and create tables if they do not exist."""
    database = r"C:\Users\steph\Documents\Hercules DevBenchmark\hercules devbenchmark database\db\hercules_devbenchmark.db"  # Path to the database file

    sql_create_games_table = """ CREATE TABLE IF NOT EXISTS Games (
                                    game_id INTEGER PRIMARY KEY AUTOINCREMENT,
                                    title TEXT NOT NULL,
                                    genre TEXT NOT NULL,
                                    comments TEXT
                                ); """  # SQL statement to create Games table

    sql_create_ratings_table = """CREATE TABLE IF NOT EXISTS Ratings (
                                      rating_id INTEGER PRIMARY KEY AUTOINCREMENT,
                                      game_id INTEGER NOT NULL,
                                      factor TEXT NOT NULL,
                                      score INTEGER NOT NULL,
                                      FOREIGN KEY (game_id) REFERENCES Games (game_id)
                                  );"""  # SQL statement to create Ratings table

    conn = create_connection(database)  # Create a database connection

    if conn is not None:  # create tables
        create_table(conn, sql_create_games_table)  # Create Games table
        create_table(conn, sql_create_ratings_table)  # Create Ratings table
    else:
        print("Error! cannot create the database connection.")  # Print error if connection fails
    
    return conn  # Return the connection object

def main():
    """Main function to run the Game Development Complexity Rating System."""
    conn = initialize_database()  # Initialize the database and get the connection object
    if conn is not None:
        root = tk.Tk()  # Create the main window
        app = GameRatingApp(root, conn)  # Create an instance of the application
        root.mainloop()  # Run the main loop
    else:
        print("Failed to initialize the database.")  # Print error if database initialization fails

if __name__ == "__main__":
    main()  # Run the main function if the script is executed directly
