# Aspen-Capital-Code-Challenge---War
This is a card game between two players. The objective of this game is to get all the cards.

# How to run this application:

This application runs using `Python`, `Flask`, and `SQLite3`. In order to get this application running you would need to:
1. Start the virtual environment by navigating to `./venv/Scripts/` and run the command `activate`.
2. Navigate back to the root folder `sandbox` and set a few environment variables up:
    ```
    set FLASK_ENV=development
    set FLASK_APP=app.py
    ```
3. Then we can run the command `flask run` to run the application.

# End-Points
There are multiple endpoints for this game:
1. `/reset` - Resets the scores for both players back to zero. 
2. `/game` - Plays the game, and displays the winner of that round, while also updating the database.
3. `/user` - Displays both of the player's scores.
4. `/user/1` - Displays player one's score.
5. `/user/2` - Displays player two's score.

# Details about any further changes
There is obviously a lot to clean up here. I would like to have had more time to work on the game itself, the communication between the database and the client, and also the interactions with the user. There is a lot to do in terms of making an actual GUI that would the application/game more appealing and inviting to the user. 

As of right now the game simply displays the winner without any information of what happened during that round. Adding some feedback about the steps being taken during the round would be absolutely necessary for any front-end developement. Working on the security of the project is also something I did not have a chance to do. Protecting from something like `query injection` is very important and should be high on the list of priorities.

Finally, cleaning up the code and making it more presentable is always a plus. I myself, always try to work clearly and concisely, but debugging and trying new things doesn't always allow for clean code.
