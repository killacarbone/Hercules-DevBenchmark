import unittest
from src.rating_calculator import calculate_complexity_rating

class TestRatingCalculator(unittest.TestCase):

    def test_calculate_complexity_rating(self):
        ratings = {
            'Graphics': 9,
            'Physics and Collision Detection': 8,
            'Level Design and World Building': 9,
            'Gameplay Mechanics': 9,
            'AI and NPC Behavior': 8,
            'Audio': 9,
            'UI and UX': 9,
            'Multiplayer and Networking': 9,
            'Scripting and Programming': 9
        }
        expected_score = 86.00
        self.assertAlmostEqual(calculate_complexity_rating(ratings), expected_score, places=2)

if __name__ == "__main__":
    unittest.main()
