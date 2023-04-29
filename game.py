from mongodb import MongoDB
from interface import NewGameWindow, CountdownWindow, RankingWindow
from mqtt import MQTTClient
import threading

## Set and connect to database
mongo = MongoDB()
mongo.connect_to_localhost()

## SET and connect to MQTT
mqtt_client = MQTTClient("broker_address", 1883, "username", "password")
mqtt_client.connect()

game_status = 1
while game_status:
    ## Open a new-game window and get the player name
    new_game_window = NewGameWindow()
    new_player_name = new_game_window.run()
    # Send start signal to broker
    mqtt_client.publish("topic", 1)

    # Begin countdown and start the game.
    count_down_window = CountdownWindow()
    count_down_window.run()
    
    # Get the scores from broker
    mqtt_client.subscribe("topic")
    new_player_points = mqtt_client.get_points()

    # Create the player records and store in database
    player_data = {new_player_name: new_player_points}
    mongo.add_new_player(player_data)

    # Retrieving all player records from database and display the top 9 players
    list_of_players = mongo.get_list_of_players()
    count_down_window.close_window()
    ranking_window = RankingWindow(list_of_players)
    # if New Game-button is pressed: Go from the top again
    # if Exit-button is pressed: Exit the game
    game_status = ranking_window.run()


