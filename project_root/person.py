import turtle

def draw_person():
    turtle.width(3)
    turtle.speed(0)
    turtle.color("black")

    # Drawing the face
    turtle.penup()
    turtle.goto(-200, -150)
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(50)
    turtle.end_fill()

    # Drawing the body
    turtle.penup()
    turtle.goto(-200, -150)
    turtle.pendown()
    turtle.goto(-200, -250)

    # Drawing the left leg
    turtle.penup()
    turtle.goto(-200, -250)
    turtle.pendown()
    turtle.goto(-220, -300)

    # Drawing the right leg
    turtle.penup()
    turtle.goto(-200, -250)
    turtle.pendown()
    turtle.goto(-180, -300)

    # Drawing the left arm
    turtle.penup()
    turtle.goto(-200, -200)
    turtle.pendown()
    turtle.goto(-240, -250)

    # Drawing the right arm
    turtle.penup()
    turtle.goto(-200, -200)
    turtle.pendown()
    turtle.goto(-160, -250)

    # Drawing the bow
    turtle.penup()
    turtle.goto(-240, -250)
    turtle.pendown()
    turtle.goto(-240, -230)
    turtle.goto(-180, -230)
    turtle.goto(-180, -250)
    turtle.goto(-240, -250)

    turtle.hideturtle()
