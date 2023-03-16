import arcade

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480


class Ball:
    def __init__(self, position_x, position_y, change_x, change_y, radius, color):
        self.position_x = position_x
        self.position_y = position_y
        self.change_x = change_x
        self.change_y = change_y
        self.radius = radius
        self.color = color

    def draw(self):
        arcade.draw_circle_filled(self.position_x, self.position_y, self.radius, self.color)

    def update(self):
        """ control ball's movement """
        self.position_x += self.change_x
        self.position_y += self.change_y

        # if ball at edge of screen, reverse direction
        if self.position_x < self.radius:
            self.change_x *= -1

        if self.position_x > SCREEN_WIDTH - self.radius:
            self.change_x *= -1

        if self.position_y < self.radius:
            self.change_y *= -1

        if self.position_y > SCREEN_HEIGHT - self.radius:
            self.change_y *= -1


class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        # call parent class init
        super().__init__(width, height, title)

        arcade.set_background_color(arcade.color.ASPARAGUS)

        # create a list of balls
        self.ball_list = []

        ball = Ball(50, 50, 3, 3, 15, arcade.color.AUBURN)
        self.ball_list.append(ball)
        ball = Ball(100, 150, 2, 3, 15, arcade.color.PURPLE_MOUNTAIN_MAJESTY)
        self.ball_list.append(ball)
        ball = Ball(150, 250, -3, -1, 15, arcade.color.AUBURN)
        self.ball_list.append(ball)

    def on_draw(self):
        # overriding default method in parent
        arcade.start_render()

        for ball in self.ball_list:
            ball.draw()

    def update(self, delta_time: float):
        # overriding default method in parent
        for ball in self.ball_list:
            ball.update()


def main():
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, "Drawing Example")

    arcade.run()


if __name__ == '__main__':
    main()
