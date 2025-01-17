import random
import arcade

SPRITE_SCALING_PLAYER = 0.5
SPRITE_SCALING_COIN = 0.2
COIN_COUNT = 50
MOVEMENT_SPEED = 5
DEAD_ZONE = 0.02


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


class Coin(arcade.Sprite):

    def __init__(self, filename, sprite_scaling):
        super().__init__(filename, sprite_scaling)

        self.change_y = 0
        self.change_x = 0

    def update(self):
        # move the coin
        self.center_x += self.change_x
        self.center_y += self.change_y

        # bounce if out of bounds
        if self.left < 0:
            self.change_x *= -1
        if self.right > SCREEN_WIDTH:
            self.change_x *= -1
        if self.bottom < 0:
            self.change_y *= -1
        if self.top > SCREEN_HEIGHT:
            self.change_y *= -1


class MyGame(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Sprite Example")

        # sprite lists
        self.player_list = None
        self.coin_list = None

        # player info
        self.player_sprite = None
        self.score = 0

        arcade.set_background_color(arcade.color.AMAZON)

        joysticks = arcade.get_joysticks()
        if joysticks:
            self.joystick = joysticks[0]
            self.joystick.open()
            self.use_mouse = False
            print("Joystick initialized.")
        else:
            print("No joystick detected.")
            self.use_mouse = True
            self.joystick = None
            self.set_mouse_visible(False)

    def setup(self):
        # sprite lists
        self.player_list = arcade.SpriteList()
        self.coin_list = arcade.SpriteList()

        self.score = 0

        # set up the player
        self.player_sprite = arcade.Sprite("character.png", SPRITE_SCALING_PLAYER)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 50
        self.player_list.append(self.player_sprite)

        # create the coins

        for i in range(COIN_COUNT):
            coin = Coin("coin.png", SPRITE_SCALING_COIN)
            coin.center_x = random.randrange(SCREEN_WIDTH)
            coin.center_y = random.randrange(SCREEN_HEIGHT)
            coin.change_x = random.randrange(-3, 4)
            coin.change_y = random.randrange(-3, 4)
            self.coin_list.append(coin)

    def on_draw(self):
        arcade.start_render()

        self.coin_list.draw()
        self.player_list.draw()
        output = "Score: " + str(self.score)
        arcade.draw_text(output, 10, 20, arcade.color.RED, 14)

    def on_mouse_motion(self, x: int, y: int, dx: int, dy: int):
        if self.use_mouse:
            self.player_sprite.center_x = x
            self.player_sprite.center_y = y
            self.check_player_pos()

    def check_player_pos(self):
        if self.player_sprite.left <= 1:
            self.player_sprite.left = 1
        if self.player_sprite.right >= SCREEN_WIDTH:
            self.player_sprite.right = SCREEN_WIDTH

        if self.player_sprite.bottom <= 1:
            self.player_sprite.bottom = 1
        if self.player_sprite.top >= SCREEN_HEIGHT:
            self.player_sprite.top = SCREEN_HEIGHT

    def update(self, delta_time: float):
        """ Movement and game logic """
        self.coin_list.update()
        # self.player_sprite.update()

        hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.coin_list)
        # loop thru the hit sprites, remove them and update score
        for coin in hit_list:
            coin.remove_from_sprite_lists()
            self.score += 1

        if self.joystick:
            # set dead zone to stop any drift from centered joystick
            if abs(self.joystick.x) < DEAD_ZONE:
                pass
            else:
                self.player_sprite.center_x += self.joystick.x * MOVEMENT_SPEED
                self.check_player_pos()

            if abs(self.joystick.y) < DEAD_ZONE:
                pass
            else:
                self.player_sprite.center_y += -self.joystick.y * MOVEMENT_SPEED
                self.check_player_pos()


def main():
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
