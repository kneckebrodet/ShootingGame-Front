from database import MongoDBClient
from interface import NewGameWindow, CountdownWindow, RankingWindow
from mqtt import MQTTClient

## SET AND CONNECT TO DATABASE
mongo = MongoDBClient()
mongo.connect_to_localhost()

## SET AND CONNECT TO MQTT
mqtt_client = MQTTClient("localhost", 1883, "admin", "123")
mqtt_client.connect()

## OPEN NEW GAME WINDOW AND GET PLAYER NAME, SEND -START- SIGNAL TO BROKER
new_game_window = NewGameWindow()
new_player_name = new_game_window.run()
mqtt_client.publish("test", 1)

## OPEN THE COUNTDOWN WINDOW WHILE GAME IS RUNNING
count_down_window = CountdownWindow()
# choose timelimit of game
count_down_window.run(15)

## RECIEVE EARNED POINTS FROM BROKER AND ADD TO DATABASE
new_player_points = mqtt_client.subscribe("test")
print(new_player_points)
player_data = {new_player_name: new_player_points}
mongo.add_new_player(player_data)

## OPEN RANKED LIST WINDOW, GET LIST FROM DATABASE AND DISPLAY TOP PLAYERS
list_of_players = mongo.get_list_of_players()
ranking_window = RankingWindow(list_of_players)
ranking_window.run()




