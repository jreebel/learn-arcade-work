import arcade

WIDTH = 20
HEIGHT = 20
MARGIN = 5
ROW_COUNT = 10
COLUMN_COUNT = 10

SCREEN_WIDTH = (COLUMN_COUNT * WIDTH) + (MARGIN * ((COLUMN_COUNT - 1) + 2))
SCREEN_HEIGHT = (ROW_COUNT * HEIGHT) + (MARGIN * ((ROW_COUNT - 1) + 2))


class MyGame(arcade.Window):
    """
    Main application class.
    """

    def __init__(self, width, height):
        super().__init__(width, height)

        arcade.set_background_color(arcade.color.BLACK)

        # create 10 x 10 array, fill with zeroes
        self.grid = []
        for row in range(ROW_COUNT):
            self.grid.append([])
            for column in range(COLUMN_COUNT):
                self.grid[row].append(0)

    def on_draw(self):
        """
        Render the screen.
        """
        arcade.start_render()

        for row in range(ROW_COUNT):
            y = (MARGIN + HEIGHT) * row + MARGIN + HEIGHT / 2
            for column in range(COLUMN_COUNT):
                x = (MARGIN + WIDTH) * column + MARGIN + WIDTH / 2

                if self.grid[row][column] == 1:
                    color = arcade.color.GREEN
                else:
                    color = arcade.color.WHITE

                arcade.draw_rectangle_filled(x, y, WIDTH, HEIGHT, color)

    def on_mouse_press(self, x, y, button, key_modifiers):
        """
        Called when the user presses a mouse button.
        """
        # print("Clicked on", x, y)
        row = y // (WIDTH + MARGIN)
        col = x // (HEIGHT + MARGIN)
        # print(f"row {row}  column {col}")
        self.grid[row][col] = 1


def main():
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.run()


if __name__ == "__main__":
    main()
