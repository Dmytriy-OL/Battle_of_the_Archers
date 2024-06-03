class Command:
    def execute(self):
        pass

class ShootArrowCommand(Command):
    def __init__(self, game):
        self.game = game

    def execute(self):
        self.game.shoot_arrow()

class ClearScreenCommand(Command):
    def __init__(self, game):
        self.game = game

    def execute(self):
        self.game.clear_screen()

class RestartGameCommand(Command):
    def __init__(self, game):
        self.game = game

    def execute(self):
        self.game.restart_game()
