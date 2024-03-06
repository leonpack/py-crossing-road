import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
from tkinter import messagebox

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.move, "Up")
screen.onkey(player.step_back, "Down")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_cars()
    car_manager.move_car()

    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            messagebox.showinfo("Game Over", f"Your final score is: {scoreboard.level - 1}")

    if player.is_at_finishing_line():
        scoreboard.increase_level()
        player.go_to_start()
        car_manager.level_up()


screen.exitonclick()