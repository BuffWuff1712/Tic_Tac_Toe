from flask import Flask, request, jsonify
from flask_cors import CORS
from AI_Bot import AI_Bot  # Make sure this file is in the same directory

app = Flask(__name__)
CORS(app)  # Allow requests from React frontend

@app.route('/ai-move', methods=['POST'])
def ai_move():
    data = request.json
    board = data['board']
    ai_player = data['ai']
    human_player = data['human']
    difficulty = data.get('difficulty', 'hard')

    ai_bot = AI_Bot(ai_player, human_player, difficulty=difficulty)
    move = ai_bot.minimax(board, current_player=ai_player)
    
    return jsonify({'move': move})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
