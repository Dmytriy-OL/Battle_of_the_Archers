import turtle
from project_root.person import draw_person
from project_root.enemy import draw_enemy

def check_hit(arrow, target, game):
    x, y = arrow.position()
    if target == "enemy":
        if 150 <= x <= 250 and -300 <= y <= -150:
            game.enemy_lives -= 1
    elif target == "person":
        if -250 <= x <= -150 and -300 <= y <= -150:
            game.person_lives -= 1

    arrow.hideturtle()
    game.clear_screen()

def clear_screen(enemy_turtle):
    turtle.clear()
    draw_person()
    draw_enemy(enemy_turtle)
