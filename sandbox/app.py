from flask import Flask, request, jsonify, abort
import sqlite3
import war

app = Flask(__name__)

conn = sqlite3.connect('player_database.db', check_same_thread=False) 
c = conn.cursor()

# c.execute('''
#           CREATE TABLE IF NOT EXISTS players
#           ([player_name] INTEGER PRIMARY KEY, [num_wins] INTEGER)
#           ''')
          
# c.execute('''
#           INSERT INTO players (player_name, num_wins)
#                 VALUES
#                 (1, 0),
#                 (2, 0)
#           ''')
                     
conn.commit()

# Display a json options menu for endpoints
@app.route('/')
def index():
  output = dict([("/reset", "Reset all scores to zero."), 
           ("/game", "Plays the game, and displays winner."),
           ("/user", "Displays both of the player's scores."),
           ("/user/1", " Displays player one's score."),
           ("/user/2", " Displays player two's score.")])
  return jsonify(output)

# Displays a single player's score
@app.route('/user/<username>')
def show_user(username):
  c.execute("SELECT * FROM players WHERE (player_name = (?))", (username))
  response = c.fetchone()
  if(not response):
    abort(404)
  response = {"Player": response[0], "Score": response[1]}
  return jsonify(response)

# Displays both player's scores
@app.route('/user')
def user():
  c.execute("SELECT * FROM players")
  response = c.fetchall()
  output = []
  for x in response:
    output.append({"Player": x[0], "Score": x[1]})
  return jsonify(output)

# Reset all the player's scores.
@app.route('/reset')
def reset():
  c.execute("UPDATE players SET num_wins = 0")
  conn.commit()
  response = {"Messege": "Successfully reset scores."}
  return jsonify(response)  

# Plays the game and displays the winner.
@app.route('/game')
def game():
  winner = war.play()
  c.execute("UPDATE players SET num_wins = num_wins + 1 WHERE player_name = (?)", (winner,))
  conn.commit()
  response = {"winner": f"Player {winner}"}
  return jsonify(response)  
