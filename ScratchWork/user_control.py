import arcade

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
MOVEMENT_SPEED = 5
DEAD_ZONE = 0.02


class Ball:
    def __init__(self, position_x, position_y, change_x, change_y, radius, color):
        self.position_x = position_x
        self.position_y = position_y
        self.change_x = change_x
        self.change_y = change_y
        self.radius = radius
        self.color = color

        self.explosion_sound = arcade.load_sound(":resources:sounds/explosion2.wav")
        self.explosion_sound_player = None

    def draw(self):
        arcade.draw_circle_filled(self.position_x,
                                  self.position_y,
                                  self.radius,
                                  self.color)

    def update(self):
        boom = False
        self.position_x += self.change_x
        self.position_y += self.change_y

        # don't go off screen
        if self.position_x < self.radius:
            self.position_x = self.radius
            boom = True

        if self.position_x > SCREEN_WIDTH - self.radius:
            self.position_x = SCREEN_WIDTH - self.radius
            boom = True

        if self.position_y < self.radius:
            self.position_y = self.radius
            boom = True

        if self.position_y > SCREEN_HEIGHT - self.radius:
            self.position_y = SCREEN_HEIGHT - self.radius
            boom = True

        if boom:
            if not self.explosion_sound_player or not self.explosion_sound_player.playing:
                self.explosion_sound_player = arcade.play_sound(self.explosion_sound)


class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        # call parent class init
        super().__init__(width, height, title)

        # make the mouse pointer disappear when over our window
        self.set_mouse_visible(False)

        # check for game controller hardware
        joysticks = arcade.get_joysticks()
        if joysticks:
            self.joystick = joysticks[0]
            self.joystick.open()
            print("Joystick initialized.")
        else:
            print("No joystick detected.")

        arcade.set_background_color(arcade.color.ASPARAGUS)

        # create a ball
        self.ball = Ball(50, 50, 0, 0, 15, arcade.color.AUBURN)

    def on_draw(self):
        # overriding default method in parent
        arcade.start_render()
        self.ball.draw()

    def update(self, delta_time: float):
        if self.joystick:
            # set dead zone to stop any drift from centered joystick
            if abs(self.joystick.x) < DEAD_ZONE:
                self.ball.change_x = 0
            else:
                self.ball.change_x = self.joystick.x * MOVEMENT_SPEED

            if abs(self.joystick.y) < DEAD_ZONE:
                self.ball.change_y = 0
            else:
                self.ball.change_y = -self.joystick.y * MOVEMENT_SPEED

        self.ball.update()

    # Use arrow keys to control ball
    def on_key_press(self, key: int, modifiers: int):
        if key == arcade.key.LEFT:
            self.ball.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.ball.change_x = MOVEMENT_SPEED
        elif key == arcade.key.UP:
            self.ball.change_y = MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.ball.change_y = -MOVEMENT_SPEED

    def on_key_release(self, key: int, modifiers: int):
        if key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.ball.change_x = 0
        if key == arcade.key.UP or key == arcade.key.DOWN:
            self.ball.change_y = 0


    # # Use mouse to control ball
    # def on_mouse_motion(self, x: int, y: int, dx: int, dy: int):
    #     # make the ball foolow the mouse position
    #     self.ball.position_x = x
    #     self.ball.position_y = y
    #
    # def on_mouse_press(self, x: int, y: int, button: int, modifiers: int):
    #     if button == arcade.MOUSE_BUTTON_LEFT:
    #         print("Left mouse button pressed at", x, y)
    #     if button == arcade.MOUSE_BUTTON_RIGHT:
    #         print("Right mouse button pressed at", x, y)
    #     if button == arcade.MOUSE_BUTTON_MIDDLE:
    #         print("Middle mouse button pressed at", x, y)


def main():
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, "Drawing Example")

    arcade.run()


if __name__ == '__main__':
    main()
