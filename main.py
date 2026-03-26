import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player=Player()
car_manager=CarManager()
scoreboard=Scoreboard()
game_is_on = True
screen.listen()
screen.onkey(player.move,"Up")
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_cars()
    if player.ycor()>280 :
        player.win_position()
        car_manager.level_up()
        scoreboard.update_score()
    for car in car_manager.all_cars:
        if player.distance(car) < 18:
            game_is_on = False
            scoreboard.game_over()
    

screen.exitonclick()