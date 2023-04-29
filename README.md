# ShootingGame-Front
This is a laser-shooting game. Input your player-name and the game will begin after a short countdown. 
During the game you have to shoot as many targets as possible during a certain amout of time. The targets are controlled by a Raspberry Pi 4,
and you can use any type of laser pointer/gun to hit the targets. The display device and the raspi are connected through a MQTT broker.
When the game is finished, all the player names with scores are saved in a MongoDB database, and the top 9players are displayed in a ranked list.
