import sqlite3
conn = sqlite3.connect('player_database') 
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