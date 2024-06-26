import turtle
from project_root.game import Game
from project_root.menu import create_menu
from project_root.person import draw_person
from project_root.enemy import draw_enemy
from project_root.commands import ShootArrowCommand, ClearScreenCommand, RestartGameCommand

# Налаштування вікна
screen = turtle.Screen()
screen.setup(800, 800)
screen.bgcolor("white")

# Налаштування черепашки
turtle.speed(0)
turtle.hideturtle()

# Створення гри
game = Game()

# Створення меню
create_menu()

# Малюємо початкового персонажа та ворога
draw_person()
draw_enemy(game.enemy_turtle)

# Налаштування клавіш
screen.listen()
screen.onkey(ShootArrowCommand(game).execute, "s")
screen.onkey(ClearScreenCommand(game).execute, "c")
screen.onkey(turtle.bye, "q")
screen.onkey(RestartGameCommand(game).execute, "r")

# Запускаємо головний цикл програми
screen.mainloop()
