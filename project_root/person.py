import turtle

def draw_person():
    turtle.width(3)
    turtle.speed(0)
    turtle.color("black")

    # Малюємо обличчя
    turtle.penup()
    turtle.goto(-200, -150)
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(50)
    turtle.end_fill()

    # Малюємо тіло
    turtle.penup()
    turtle.goto(-200, -150)
    turtle.pendown()
    turtle.goto(-200, -250)

    # Малюємо ліву ногу
    turtle.penup()
    turtle.goto(-200, -250)
    turtle.pendown()
    turtle.goto(-220, -300)

    # Малюємо праву ногу
    turtle.penup()
    turtle.goto(-200, -250)
    turtle.pendown()
    turtle.goto(-180, -300)

    # Малюємо ліву руку
    turtle.penup()
    turtle.goto(-200, -200)
    turtle.pendown()
    turtle.goto(-240, -250)

    # Малюємо праву руку
    turtle.penup()
    turtle.goto(-200, -200)
    turtle.pendown()
    turtle.goto(-160, -250)

    # Малюємо лук
    turtle.penup()
    turtle.goto(-240, -250)
    turtle.pendown()
    turtle.goto(-240, -230)
    turtle.goto(-180, -230)
    turtle.goto(-180, -250)
    turtle.goto(-240, -250)

    turtle.hideturtle()
