import sqlite3
# SQLite objects created in a thread can only be used in that same thread, thus
# the need for the check_same_thread flag to be false.
conn = sqlite3.connect('player_database', check_same_thread=False) 
c = conn.cursor()

c.execute('''
          CREATE TABLE IF NOT EXISTS players
          ([player_name] INTEGER PRIMARY KEY, [num_wins] INTEGER)
          ''')
          
c.execute('''
          INSERT INTO players (player_name, num_wins)
                VALUES
                (1, 0),
                (2, 0)
          ''')
                     
conn.commit()