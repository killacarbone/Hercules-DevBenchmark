## License

This project is licensed under a proprietary license. See the [LICENSE](./LICENSE.md) file for details.


# Game Development Complexity Rating System

This project provides a system to rate the complexity of game development based on predefined factors.

## Project Structure

game-rating-system/
│
├── data/
│ ├── predefined_ratings.json # Stores predefined ratings
│ ├── ratings.txt # Stores calculated ratings
│
├── src/
│ ├── __init__.py # Makes src a package
│ ├── main.py # Entry point for the application
│ ├── code_generator.py # Module for generating unique codes
│ ├── rating_calculator.py # Module for calculating ratings
│ ├── file_operations.py # Module for file read/write operations
│
├── tests/
│ ├── __init__.py # Makes tests a package
│ ├── test_code_generator.py # Unit tests for code_generator.py
│ ├── test_rating_calculator.py # Unit tests for rating_calculator.py
│ ├── test_file_operations.py # Unit tests for file_operations.py
│
├── instructions.md # Instructions for generating unique codes
├── requirements.txt # Python dependencies
└── README.md # Project overview and setup instructions

## Setup

1. Clone the repository.
2. Install the dependencies:
    ```sh
    pip install -r requirements.txt
    ```
3. Run the application:
    ```sh
    python src/main.py
    ```

## Running Tests

To run the unit tests, use:
```sh
pytest tests/
