# Genos Discord Bot

Genos is a Discord bot built using the Discord.py library. It comes with various modules, including conversation, moderation, code help, API interactions, and a simple database system.

## Description

Genos is designed to be a versatile Discord bot with the following modules:

### 1. Conversation Module

- Responds to various greetings and farewells.
- Introduces itself when asked.

### 2. Moderation Module

- Includes a command to clear messages in a channel.

### 3. Code Help Module

- Provides information about lists, strings, and dictionaries in Python.

### 4. API Module

- Fetches and displays memes, cat images, and dog images using external APIs.
- Includes a command to fetch movie information from IMDb (currently commented out).

### 5. Database Module

- Allows storing, changing, retrieving, and deleting data in a simple database.

### 6. Hangman Game
- Displays a word and hint for game. Stores score of different players.

## Installation

1. Clone the repository.

    ```bash
    git clone https://github.com/r-abhinav/genos.git
    ```

2. Install the required dependencies.

    ```bash
    pip install -r requirements.txt
    ```

3. Set up environment variables for your Discord bot token and IMDb API key.
4. Run the bot.

    ```bash
    python bot.py
    ```

## Commands

### Conversation Module

- Various greetings and farewells.
- **`introduce yourself`**: Get to know Genos.

### Moderation Module

- **`clear <number>`**: Clear a specified number of messages in the channel.

### Code Help Module

- **`codeh list`**: Information about Python lists.
- **`codeh str`**: Information about Python strings.
- **`codeh dict`**: Information about Python dictionaries.

### API Module

- **`send meme`**: Display a random meme.
- **`send cat`**: Display a random cat image.
- **`send dog`**: Display a random dog image.
- **`mov <movie title>`**: Fetch information about a movie.

### Database Module

- **`store <key> <value>`**: Store data in the database.
- **`change <old_key> <new_key>`**: Change the key in the database.
- **`get <key>`**: Retrieve data from the database.
- **`getnum <number>`**: Retrieve data by specifying a number.
- **`dele <key>`**: Delete data from the database.
- **`delenum <number>`**: Delete data by specifying a number.
- **`all`**: Display all stored values in the database.

### Additional Commands

- **`datab`**: Displays all entries in the database.
- **`luffy`**: Clears all entries in the database.

### Hangman Game

- **`hn`**: Starts a hangman game.
- Type a single letter to guess the word.
- Use **`stop`** to stop the game.
- Use **`hint`** for a hint.

### Leaderboard

- **`top`**: Displays the leaderboard with user scores and averages.
