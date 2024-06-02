import turtle
from project_root.person import draw_person
from project_root.enemy import draw_enemy

def check_hit(arrow, target, game):
    if target == "enemy":
        if -300 <= arrow.ycor() <= -150:  # Попадання в голову, тіло або ноги
            game.enemy_lives -= 1
    elif target == "person":
        if -300 <= arrow.ycor() <= -150:  # Попадання в голову, тіло або ноги
            game.person_lives -= 1

    # Оновлення екрану після пострілу
    arrow.hideturtle()
    game.clear_screen()

    if game.enemy_lives == 0:
        turtle.goto(0, 0)
        turtle.color("green")
        turtle.write("Ви перемогли! Натисніть 'R' для перезапуску", align="center", font=("Arial", 24, "normal"))
    elif game.person_lives == 0:
        turtle.goto(0, 0)
        turtle.color("red")
        turtle.write("Ви програли! Натисніть 'R' для перезапуску", align="center", font=("Arial", 24, "normal"))
    else:
        if game.turn == "person":
            game.turn = "enemy"
            game.shoot_enemy_arrow()
        else:
            game.turn = "person"

def clear_screen(enemy_turtle):
    turtle.clear()
    draw_person()
    draw_enemy(enemy_turtle)
    turtle.update()
