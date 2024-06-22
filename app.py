from flask import Flask, render_template, jsonify, request
import tic_tac_toe

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/move', methods=['POST'])
def move():
    data = request.get_json()
    board = data['board']
    row = data['row']
    col = data['col']
    
    if not tic_tac_toe.make_move(board, row, col, 'X'):
        return jsonify({'error': 'Invalid move'})
    
    game_over_message = tic_tac_toe.check_game_over(board)
    if game_over_message:
        return jsonify({'board': board, 'message': game_over_message})
    
    ai_move = tic_tac_toe.best_move(board)
    if ai_move:
        tic_tac_toe.make_move(board, ai_move[0], ai_move[1], 'O')
    
    game_over_message = tic_tac_toe.check_game_over(board)
    return jsonify({'board': board, 'message': game_over_message})

if __name__ == '__main__':
    app.run(debug=True)
