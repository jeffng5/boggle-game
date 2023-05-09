from boggle import Boggle
from flask import Flask, render_template, request, jsonify
from flask import session 
from flask_debugtoolbar import DebugToolbarExtension
import requests

app= Flask(__name__)
app.config['SECRET_KEY'] = 'nowayJose'
app.config['DEBUG_TB_INTERCEPT_REDIRECTS']= False
# debug= DebugToolbarExtension(app)
boggle_game = Boggle()
board= boggle_game.make_board()


@app.route('/')
def make_board():
    
    return render_template('board.html', board=board)

@app.route('/game')
def play():
    session['board']
    score = 0
    entry = request.args.get('guess')
    
    words=entry
    result = boggle_game.check_valid_word(board, words)
    total=[]
    if result == 'ok':
        score += len(entry)
        total.append(score)
    summation = sum(total)
    return render_template('board.html', board=board, check=words, result=result, total=summation) 

