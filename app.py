from boggle import Boggle
from flask import Flask, render_template, request, jsonify
from flask import session 
# from flask_debugtoolbar import DebugToolbarExtension

app= Flask(__name__)
app.config['SECRET_KEY'] = 'nowayJose'
app.config['DEBUG_TB_INTERCEPT_REDIRECTS']= False
# debug= DebugToolbarExtension(app)
boggle_game = Boggle()


# start game here
@app.route('/')
def make_board():
    #reset running total to 0
    session['running_total'] = 0
    #setup board
    board=boggle_game.make_board()
    session['board']=board
    return render_template('board.html', board=board)

@app.route('/game')
def play():
    #keep board constant by storing in sessions
    board= session['board']
    #get the value of form entry
    entry = request.args.get('guess')
    words=entry
    #function to check if word is valid
    result = boggle_game.check_valid_word(board, words)
    running_total=0
    #keeping track of score
    score=0
    if result == 'ok':
        score += len(entry)
        running_total += score 
        session['running_total'] = session['running_total'] + running_total
    
    
    #keeping track of high score
    if session['running_total'] > session['high_score']:   
        session['high_score']= session['running_total']
    return render_template('board.html', board=board, check=words, result=result) 

