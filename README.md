# Tic-Tac-Toe with AI

This is a simple Tic-Tac-Toe game implemented in Python with an AI opponent using the Minimax algorithm. The game is played through a web interface built with Flask for the backend and HTML/CSS/JavaScript for the frontend.

## Project Structure

```
tic_tac_toe/
├── static/
│   ├── styles.css
│   └── img.jpg
├── templates/
│   └── index.html
├── app.py
└── tic_tac_toe.py
```

- **`static/`**: Contains static files such as CSS stylesheets and images.
- **`templates/`**: Contains HTML templates for the web interface.
- **`app.py`**: Flask application to handle backend logic and routes.
- **`tic_tac_toe.py`**: Python module with game logic including the Minimax algorithm for the AI.

## Prerequisites

- Python installed on your machine.
- Flask library installed (`pip install Flask`).

## Getting Started

1. Clone the repository to your local machine:
   ```bash
   git clone https://github.com/astromanu007/CODSOFT_2.git
   cd tic-tac-toe
   ```

2. Install Flask (if not already installed):
   ```bash
   pip install Flask
   ```

3. Move the `img.jpg` file to the `static/` folder.

4. Run the Flask application:
   ```bash
   python app.py
   ```

5. Open your web browser and go to `http://127.0.0.1:5000/` to play the game.

## Gameplay Instructions

- Click on any cell on the board to make a move.
- The AI opponent will automatically make its move after you make yours.
- The game status (win, lose, or draw) will be displayed at the bottom of the page.

## Customize

- You can customize the game's appearance by modifying the CSS styles in `static/styles.css`.
- You can modify the game logic or AI algorithm in `tic_tac_toe.py` for different gameplay experiences.

## License

This project is licensed under the MIT License. Feel free to modify and use it for your own purposes.
