# Rock, Paper, Scissors Extended Game

This project is an extended version of the classic "Rock, Paper, Scissors" game with customizable options such as Lizard, Spock, and more. Players can provide their own list of game options, or the game defaults to the classic "Rock, Paper, Scissors" version if no options are specified.

## Features
- Support for custom game options (e.g., rock, paper, scissors, lizard, spock).
- A circular algorithm to determine which option wins or loses.
- Defaults to classic Rock, Paper, Scissors if no options are provided.
- Unit tests using `unittest` framework.

## Installation

To run this project, follow these steps:

### 1. Clone the repository
```bash
git clone <repository-url>
cd <repository-folder>
```

### 2. Create and activate a virtual environment
You can create a virtual environment using `venv` to manage dependencies:

- On macOS/Linux:
  ```bash
  python3 -m venv venv
  source venv/bin/activate
  ```

- On Windows:
  ```bash
  python -m venv venv
  venv\Scripts\activate
  ```

### 3. Install the required dependencies
The required Python packages are listed in the `requirements.txt` file. Install them with:
```bash
pip install -r requirements.txt
```

## Running the Application

To start the game, run the following command:
```bash
python game.py
```

## Running Unit Tests

The project uses the `unitest` framework. To run all unit tests, use the following command:
```bash
python -m unittest test_game.TestGame
```

Make sure that you have activated the virtual environment before running any command.

## Dependencies

- Python 3.x
- `unitest` 1.4.34 (included in the Python Standard Library)
