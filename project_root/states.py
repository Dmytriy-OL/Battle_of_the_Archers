import turtle

class GameState:
    def handle(self, game):
        pass

class PlayingState(GameState):
    def handle(self, game):
        pass

class WinState(GameState):
    def handle(self, game):
        turtle.goto(0, 0)
        turtle.color("green")
        turtle.write("Ви перемогли! Натисніть 'R' для перезапуску", align="center", font=("Arial", 24, "normal"))

class LoseState(GameState):
    def handle(self, game):
        turtle.goto(0, 0)
        turtle.color("red")
        turtle.write("Ви програли! Натисніть 'R' для перезапуску", align="center", font=("Arial", 24, "normal"))
