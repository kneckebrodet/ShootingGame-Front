from mongodb import MongoDB
from interface import NewGameWindow, CountdownWindow, RankingWindow
from mqtt import MQTTClient
import threading

## SET AND CONNECT TO DATABASE
mongo = MongoDB()
mongo.connect_to_localhost()

## SET AND CONNECT TO MQTT
mqtt_client = MQTTClient("broker_address", 1883, "username", "password")
mqtt_client.connect()

game_status = 1
while game_status:
    ## OPEN NEW GAME WINDOW AND GET PLAYER NAME, SEND -START- SIGNAL TO BROKER
    new_game_window = NewGameWindow()
    new_player_name = new_game_window.run()
    mqtt_client.publish("test", 1)

    count_down_window = CountdownWindow()
    target = count_down_window.run()
    target=mqtt_client.subscribe("test")

    #mqtt_thread.join()
    new_player_points =  mqtt_client.get_points()

    ## RECIEVE EARNED POINTS FROM BROKER AND ADD TO DATABASE
    print(new_player_points)
    player_data = {new_player_name: new_player_points}
    mongo.add_new_player(player_data)

    ## OPEN RANKED LIST WINDOW, GET LIST FROM DATABASE AND DISPLAY TOP PLAYERS
    list_of_players = mongo.get_list_of_players()
    count_down_window.close_window()
    ranking_window = RankingWindow(list_of_players)
    game_status = ranking_window.run()


