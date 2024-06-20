import logging
import sqlite3  # Import sqlite3 module for SQLite database operations
from sqlite3 import Error  # Import Error class from sqlite3

def create_connection(db_file):
    """Create a database connection to the SQLite database specified by db_file."""
    conn = None  # Initialize connection variable
    try:
        conn = sqlite3.connect(db_file)  # Connect to the database
        print(f"Connected to SQLite database: {db_file}")  # Print success message
    except Error as e:
        print(e)  # Print error message
    return conn  # Return the connection object

def create_table(conn, create_table_sql):
    """Create a table from the create_table_sql statement."""
    try:
        c = conn.cursor()  # Create a cursor object
        c.execute(create_table_sql)  # Execute the create table statement
    except Error as e:
        print(e)  # Print error message

def insert_game(conn, game):
    """Insert a new game into the Games table."""
    sql = '''INSERT INTO Games(title, genre, comments)
             VALUES(?, ?, ?)'''  # SQL insert statement
    cur = conn.cursor()  # Create a cursor object
    cur.execute(sql, game)  # Execute the insert statement
    conn.commit()  # Commit the transaction
    return cur.lastrowid  # Return the last row ID

def insert_rating(conn, rating):
    """Insert a new rating into the Ratings table."""
    sql = '''INSERT INTO Ratings(game_id, factor, score)
             VALUES(?, ?, ?)'''  # SQL insert statement
    cur = conn.cursor()  # Create a cursor object
    cur.execute(sql, rating)  # Execute the insert statement
    conn.commit()  # Commit the transaction
    return cur.lastrowid  # Return the last row ID

def select_all_games(conn):
    """Query all rows in the Games table."""
    cur = conn.cursor()  # Create a cursor object
    cur.execute("SELECT * FROM Games")  # Execute the select statement
    rows = cur.fetchall()  # Fetch all rows
    logging.debug(f"select_all_games fetched: {rows}")  # Add this line for debugging
    return rows  # Return fetched rows

def select_all_ratings(conn):
    """Query all rows in the Ratings table."""
    cur = conn.cursor()  # Create a cursor object
    cur.execute("SELECT * FROM Ratings")  # Execute the select statement
    rows = cur.fetchall()  # Fetch all rows
    logging.debug(f"select_all_ratings fetched: {rows}")  # Add this line for debugging
    return rows  # Return fetched rows

