import logging  # Import logging module for logging messages
from src.file_operations import create_predefined_db_connection, create_predefined_tables, get_predefined_db_path  # Import necessary functions
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

def initialize_predefined_database():
    """Initialize the predefined SQLite database and create tables if they do not exist."""
    predefined_db_path = get_predefined_db_path()  # Get the path to the predefined database
    conn = create_predefined_db_connection(predefined_db_path)  # Create a connection to the predefined database

    if conn is not None:
        create_predefined_tables(conn)  # Create the predefined ratings table
        conn.close()  # Close the connection
    else:
        logging.error("Error! Cannot create the predefined database connection.")

# Ensure predefined database is initialized
initialize_predefined_database()

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
    
    logging.debug("Attempting to create a database connection.")
    conn = create_connection(database)  # Create a database connection

    if conn is not None:
        logging.debug("Database connection established.")
        try:
            create_table(conn, sql_create_games_table)  # Create Games table
            logging.info("Games table created or already exists.")
        except Exception as e:
            logging.error(f"Failed to create Games table: {e}")

        try:
            create_table(conn, sql_create_ratings_table)  # Create Ratings table
            logging.info("Ratings table created or already exists.")
        except Exception as e:
            logging.error(f"Failed to create Ratings table: {e}")
    else:
        logging.error("Error! Cannot create the database connection.")

    return conn  # Return the connection object

def main():
    """Main function to run the Game Development Complexity Rating System."""
    logging.debug("Starting the application.")
    conn = initialize_database()  # Initialize the database and get the connection object
    if conn is not None:
        logging.debug("Database initialized successfully.")
        root = tk.Tk()  # Create the main window
        app = GameRatingApp(root, conn)  # Create an instance of the application
        root.mainloop()  # Run the main loop
        logging.debug("Main loop started.")
    else:
        logging.error("Failed to initialize the database.")

if __name__ == "__main__":
    main()  # Run the main function if the script is executed directly
