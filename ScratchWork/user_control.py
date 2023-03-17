import arcade

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480


class Ball:
    def __init__(self, position_x, position_y, radius, color):
        self.position_x = position_x
        self.position_y = position_y
        self.radius = radius
        self.color = color

    def draw(self):
        arcade.draw_circle_filled(self.position_x,
                                  self.position_y,
                                  self.radius,
                                  self.color)


class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        # call parent class init
        super().__init__(width, height, title)

        arcade.set_background_color(arcade.color.ASPARAGUS)

        # create a ball
        self.ball = Ball(50, 50, 15, arcade.color.AUBURN)

    def on_draw(self):
        # overriding default method in parent
        arcade.start_render()

        self.ball.draw()


def main():
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, "Drawing Example")

    arcade.run()


if __name__ == '__main__':
    main()
