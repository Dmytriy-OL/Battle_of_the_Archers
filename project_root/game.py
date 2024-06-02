import turtle
import random
from project_root.utils import check_hit, clear_screen

class Game:
    def __init__(self):
        self.person_lives = 3
        self.enemy_lives = 3
        self.turn = "person"
        self.enemy_turtle = turtle.Turtle()
        self.enemy_turtle.hideturtle()

    def shoot_arrow(self):
        arrow = turtle.Turtle()
        arrow.color("black")
        arrow.shape("triangle")
        arrow.penup()
        arrow.goto(-200, -230)
        arrow.setheading(0)
        arrow.speed(1)
        self.random_arrow_flight(arrow, 200)
        check_hit(arrow, "enemy", self)

    def shoot_enemy_arrow(self):
        enemy_arrow = turtle.Turtle()
        enemy_arrow.color("red")
        enemy_arrow.shape("triangle")
        enemy_arrow.penup()
        enemy_arrow.goto(200, -230)
        enemy_arrow.setheading(180)
        enemy_arrow.speed(1)
        self.random_arrow_flight(enemy_arrow, -200)
        check_hit(enemy_arrow, "person", self)

    def random_arrow_flight(self, arrow, target_x):
        hit_chance = random.choice([True, False])  # 50% шанс попадання
        if hit_chance:
            target_y = random.choice([-150, -250, -300])
        else:
            target_y = random.choice([-50, -120, -220, -350])  # Мимо цілі
        arrow.goto(target_x, target_y)

    def clear_screen(self):
        clear_screen(self.enemy_turtle)

    def restart_game(self):
        self.person_lives = 3
        self.enemy_lives = 3
        self.turn = "person"
        self.clear_screen()
