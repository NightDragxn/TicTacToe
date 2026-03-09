from flask import Flask, request, jsonify
from flask_cors import CORS
import math

app = Flask(__name__)
CORS(app)

def check_winner(board):
    win_configs = [(0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6)]
    for r in win_configs:
        if board[r[0]] == board[r[1]] == board[r[2]] != "":
            return board[r[0]]
    if "" not in board:
        return "Draw"
    return None

def minimax(board, depth, is_maximizing):
    res = check_winner(board)
    if res == "O": return 10 - depth
    if res == "X": return depth - 10
    if res == "Draw": return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(9):
            if board[i] == "":
                board[i] = "O"
                score = minimax(board, depth + 1, False)
                board[i] = ""
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for i in range(9):
            if board[i] == "":
                board[i] = "X"
                score = minimax(board, depth + 1, True)
                board[i] = ""
                best_score = min(score, best_score)
        return best_score

@app.route('/get_move', methods=['POST'])
def get_move():
    data = request.json
    board = data['board'] # Das Array ["X", "", "O", ...] vom JS
    
    best_score = -math.inf
    move = 0
    
    for i in range(9):
        if board[i] == "":
            board[i] = "O"
            score = minimax(board, 0, False)
            board[i] = ""
            if score > best_score:
                best_score = score
                move = i
                
    return jsonify({'move': move})

if __name__ == '__main__':
    app.run(port=5000, debug=True)