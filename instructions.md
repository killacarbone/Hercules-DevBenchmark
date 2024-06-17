# Instructions for Generating a Unique Code

To ensure that anyone can generate and return accurate codes for the system, follow these steps:

## Standard Format for Code Generation

1. **Game Identifier**: Use a recognizable short form of the game’s name (e.g., "WoW" for "World of Warcraft").
2. **Ratings**: List ratings in a specific order for each factor:
    - Graphics
    - Physics and Collision Detection
    - Level Design and World Building
    - Gameplay Mechanics
    - AI and NPC Behavior
    - Audio
    - UI and UX
    - Multiplayer and Networking
    - Scripting and Programming

## Value Limits

- Ratings for each factor should be an integer between 0 and 1000, inclusive.

## Example Format

**Format**: `<GameIdentifier>-<Graphics><Physics><LevelDesign><Gameplay><AI><Audio><UIUX><Multiplayer><Scripting>`

## Steps to Generate a Unique Code for a Game

1. **Identify the Game**: Use a short, clear identifier for the game (e.g., "WoW" for "World of Warcraft").
2. **Collect Ratings**: Gather the ratings for each factor, ensuring they are integers between 0 and 1000.
3. **Construct the Code**: Combine the identifier and the ratings in the specified order.

## Example

1. **Collect Ratings**:
    - Graphics: 923
    - Physics and Collision Detection: 854
    - Level Design and World Building: 920
    - Gameplay Mechanics: 930
    - AI and NPC Behavior: 878
    - Audio: 890
    - UI and UX: 860
    - Multiplayer and Networking: 870
    - Scripting and Programming: 880

2. **Use the Identifier**: "WoW"
3. **Generate the Code**: Combine the identifier and ratings in the specified order.

**Generated Code**: `WoW-923854920930878890860870880`

## Example Communication Template

To generate a code for the Game Development Complexity Rating System:

1. **Game Identifier**: Use a short, recognizable form of the game's name (e.g., "WoW" for "World of Warcraft").
2. **Ratings**: Provide the ratings in the following order (each rating should be an integer between 0 and 1000):
    - Graphics: [rating]
    - Physics and Collision Detection: [rating]
    - Level Design and World Building: [rating]
    - Gameplay Mechanics: [rating]
    - AI and NPC Behavior: [rating]
    - Audio: [rating]
    - UI and UX: [rating]
    - Multiplayer and Networking: [rating]
    - Scripting and Programming: [rating]
3. **Construct the Code**: Combine the identifier and the ratings in the order specified.

**Example**:
- Game: World of Warcraft
- Identifier: WoW
- Ratings: 923, 854, 920, 930, 878, 890, 860, 870, 880
- Generated Code: WoW-923854920930878890860870880

## Automating the Process

Consider creating a web-based form or an interactive bot where users input the game name and ratings, and it automatically generates the code. This ensures consistency and accuracy, and anyone can use it without needing to understand the underlying logic.
