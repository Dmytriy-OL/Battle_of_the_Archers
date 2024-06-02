import turtle

def create_menu():
    menu = turtle.Turtle()
    menu.speed(0)
    menu.color("black")
    menu.penup()
    menu.goto(-300, 300)
    menu.hideturtle()
    menu.write("Меню:", font=("Arial", 16, "normal"))
    menu.goto(-300, 270)
    menu.write("S - Стрільба", font=("Arial", 12, "normal"))
    menu.goto(-300, 240)
    menu.write("C - Очистити екран", font=("Arial", 12, "normal"))
    menu.goto(-300, 210)
    menu.write("Q - Вийти з програми", font=("Arial", 12, "normal"))
    menu.goto(-300, 180)
    menu.write("R - Перезапуск гри", font=("Arial", 12, "normal"))
