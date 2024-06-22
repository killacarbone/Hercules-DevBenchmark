import unittest
from src.code_generator import generate_code, parse_input_code

class TestCodeGenerator(unittest.TestCase):

    def test_generate_code(self):
        game_identifier = "WoW"
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
        expected_code = "WoW989989899"
        self.assertEqual(generate_code(game_identifier, ratings), expected_code)

    def test_parse_input_code(self):
        input_code = "WoW989989899"
        expected_identifier = "WoW"
        expected_ratings = {
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
        identifier, ratings = parse_input_code(input_code)
        self.assertEqual(identifier, expected_identifier)
        self.assertEqual(ratings, expected_ratings)

if __name__ == "__main__":
    unittest.main()
