import unittest
import requests

class ApiTest(unittest.TestCase):
    URL_LANDING_PAGE = "http://127.0.0.1:5000/"
    URL_RESET = "{}reset".format(URL_LANDING_PAGE)
    URL_GAME = "{}game".format(URL_LANDING_PAGE)
    URL_USER = "{}user".format(URL_LANDING_PAGE)
    URL_USER_1 = "{}user/1".format(URL_LANDING_PAGE)
    URL_USER_2 = "{}user/2".format(URL_LANDING_PAGE)
    
    def test_landing_page(self):
        response = requests.get(ApiTest.URL_LANDING_PAGE)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 5)
        self.assertTrue(response.json()['/game'] in ['Plays the game, and displays winner.'])
        self.assertTrue(response.json()["/reset"] in ["Reset all scores to zero."])
        self.assertTrue(response.json()["/user"] in ["Displays both of the player's scores."])
        self.assertTrue(response.json()["/user/1"] in ["Displays player one's score."])
        self.assertTrue(response.json()["/user/2"] in ["Displays player two's score."])

    def test_reset_page(self):
        response = requests.get(ApiTest.URL_RESET)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 1)
        self.assertEqual(response.json()["Messege"], "Successfully reset scores.")
        response = requests.get(ApiTest.URL_USER)
        self.assertTrue(response.json()[0]["Score"] in [0])
        self.assertTrue(response.json()[1]["Score"] in [0])

    def test_game_page(self):
        response = requests.get(ApiTest.URL_GAME)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 1)
        self.assertTrue(response.json()['Winner'] in ['Player 1', 'Player 2'])
    
    def test_user_page(self):
        response = requests.get(ApiTest.URL_USER)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 2)

    def test_user_1_page(self):
        response = requests.get(ApiTest.URL_USER_1)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 2)

    def test_user_2_page(self):
        response = requests.get(ApiTest.URL_USER_2)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 2)



if __name__ == '__main__':
        unittest.main()