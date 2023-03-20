import random
import arcade
from sys import exit
from time import sleep

SPRITE_SCALING_PLAYER = 0.5
SPRITE_SCALING_COIN = 0.3
COIN_COUNT = 50
MOVEMENT_SPEED = 5
DEAD_ZONE = 0.02
PLAYER_CENTER_OFFSET_X = 32
PLAYER_CENTER_OFFSET_Y = 64


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


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
            coin = arcade.Sprite("coin.png", SPRITE_SCALING_COIN)
            coin.center_x = random.randrange(SCREEN_WIDTH)
            coin.center_y = random.randrange(SCREEN_HEIGHT)
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

    def update(self, delta_time: float):
        """ Movement and game logic """
        self.coin_list.update()
        self.player_sprite.update()

        coins_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.coin_list)
        # loop thru the hit sprites, remove them and update score
        for coin in coins_hit_list:
            coin.remove_from_sprite_lists()
            self.score += 1

        if self.joystick:
            # set dead zone to stop any drift from centered joystick
            if abs(self.joystick.x) < DEAD_ZONE:
                pass
            else:
                self.player_sprite.center_x += self.joystick.x * MOVEMENT_SPEED
                if self.player_sprite.center_x <= 1:
                    self.player_sprite.center_x = PLAYER_CENTER_OFFSET_X
                if self.player_sprite.center_x >= SCREEN_WIDTH:
                    self.player_sprite.center_x -= PLAYER_CENTER_OFFSET_X

            if abs(self.joystick.y) < DEAD_ZONE:
                pass
            else:
                self.player_sprite.center_y += -self.joystick.y * MOVEMENT_SPEED
                if self.player_sprite.center_y <= 1:
                    self.player_sprite.center_y = PLAYER_CENTER_OFFSET_Y
                if self.player_sprite.center_y >= SCREEN_HEIGHT:
                    self.player_sprite.center_y -= PLAYER_CENTER_OFFSET_Y


def main():
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
