def draw_enemy(enemy_turtle):
    enemy_turtle.width(3)
    enemy_turtle.speed(0)
    enemy_turtle.color("red")

    # Малюємо обличчя
    enemy_turtle.penup()
    enemy_turtle.goto(200, -150)
    enemy_turtle.pendown()
    enemy_turtle.begin_fill()
    enemy_turtle.circle(50)
    enemy_turtle.end_fill()

    # Малюємо тіло
    enemy_turtle.penup()
    enemy_turtle.goto(200, -150)
    enemy_turtle.pendown()
    enemy_turtle.goto(200, -250)

    # Малюємо ліву ногу
    enemy_turtle.penup()
    enemy_turtle.goto(200, -250)
    enemy_turtle.pendown()
    enemy_turtle.goto(180, -300)

    # Малюємо праву ногу
    enemy_turtle.penup()
    enemy_turtle.goto(200, -250)
    enemy_turtle.pendown()
    enemy_turtle.goto(220, -300)

    # Малюємо ліву руку
    enemy_turtle.penup()
    enemy_turtle.goto(200, -200)
    enemy_turtle.pendown()
    enemy_turtle.goto(160, -250)

    # Малюємо праву руку
    enemy_turtle.penup()
    enemy_turtle.goto(200, -200)
    enemy_turtle.pendown()
    enemy_turtle.goto(240, -250)

    # Малюємо лук
    enemy_turtle.penup()
    enemy_turtle.goto(240, -250)
    enemy_turtle.pendown()
    enemy_turtle.goto(240, -230)
    enemy_turtle.goto(180, -230)
    enemy_turtle.goto(180, -250)
    enemy_turtle.goto(240, -250)

    enemy_turtle.hideturtle()
