import unittest
import os
from src.file_operations import load_predefined_ratings, save_predefined_ratings, load_ratings_from_file, save_ratings_to_file

class TestFileOperations(unittest.TestCase):

    def setUp(self):
        self.predefined_ratings_file = 'test_predefined_ratings.json'
        self.ratings_file = 'test_ratings.txt'
        self.sample_predefined_ratings = {
            "WoW": {
                "Graphics": 9,
                "Physics and Collision Detection": 8,
                "Level Design and World Building": 9,
                "Gameplay Mechanics": 9,
                "AI and NPC Behavior": 8,
                "Audio": 9,
                "UI and UX": 9,
                "Multiplayer and Networking": 9,
                "Scripting and Programming": 9
            }
        }
        self.sample_ratings = {
            "WoW": 86.00
        }

    def tearDown(self):
        if os.path.exists(self.predefined_ratings_file):
            os.remove(self.predefined_ratings_file)
        if os.path.exists(self.ratings_file):
            os.remove(self.ratings_file)

    def test_save_and_load_predefined_ratings(self):
        save_predefined_ratings(self.sample_predefined_ratings, self.predefined_ratings_file)
        loaded_ratings = load_predefined_ratings(self.predefined_ratings_file)
        self.assertEqual(loaded_ratings, self.sample_predefined_ratings)

    def test_save_and_load_ratings(self):
        save_ratings_to_file(self.sample_ratings, self.ratings_file)
        loaded_ratings = load_ratings_from_file(self.ratings_file)
        self.assertEqual(loaded_ratings, self.sample_ratings)

if __name__ == "__main__":
    unittest.main()
