import csv
import sqlite3
import logging
from src.file_operations import create_predefined_db_connection, create_predefined_tables

def load_predefined_ratings():
    """Load predefined ratings from CSV file into the predefined_ratings.db."""
    predefined_db_path = r"C:\Users\steph\Documents\Hercules DevBenchmark\hercules devbenchmark database\db\predefined_ratings.db"
    conn = create_predefined_db_connection(predefined_db_path)
    
    if conn is not None:
        create_predefined_tables(conn)  # Ensure the table is created

        # Update the path to the CSV file in the data folder
        csv_file_path = r"C:\Users\steph\Documents\Hercules DevBenchmark\data\predefined_ratings.csv"
        with open(csv_file_path, 'r', newline='', encoding='utf-8') as csvfile:
            csv_reader = csv.DictReader(csvfile)
            cursor = conn.cursor()
            
            for row in csv_reader:
                cursor.execute("""
                    INSERT OR REPLACE INTO PredefinedRatings 
                    (game_identifier, graphics, physics, level_design, gameplay_mechanics, ai_behavior, audio, ui_ux, multiplayer, scripting)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """, (
                    row['Game Identifier'],
                    int(row['Graphics']),
                    int(row['Physics']),
                    int(row['Level Design']),
                    int(row['Gameplay Mechanics']),
                    int(row['AI Behavior']),
                    int(row['Audio']),
                    int(row['UI UX']),
                    int(row['Multiplayer']),
                    int(row['Scripting'])
                ))
                
            conn.commit()
            logging.info("Predefined ratings loaded successfully.")
            
        conn.close()
    else:
        logging.error("Error! Cannot create the predefined database connection.")

if __name__ == "__main__":
    load_predefined_ratings()
