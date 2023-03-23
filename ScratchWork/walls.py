import arcade

SPRITE_SCALING_BOX = 0.5
SPRITE_SCALING_PLAYER = 0.5

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

MOVEMENT_SPEED = 5


class MyGame(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Sprites and Walls")

        # sprite lists
        self.player_list = None
        self.wall_list = None

        self.physics_engine = None

    def setup(self):
        arcade.set_background_color(arcade.color.AMAZON)
        self.player_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList()

        self.score = 0
        self.player_sprite = arcade.Sprite("character.png", SPRITE_SCALING_PLAYER)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 64
        self.player_list.append(self.player_sprite)

        # manually create a box at 300, 200
        wall = arcade.Sprite(":resources:images/tiles/boxCrate_double.png",
                             SPRITE_SCALING_BOX)
        wall.center_x = 300
        wall.center_y = 200
        self.wall_list.append(wall)

        # manually create another box at 364, 200
        wall = arcade.Sprite(":resources:images/tiles/boxCrate_double.png",
                             SPRITE_SCALING_BOX)
        wall.center_x = 364
        wall.center_y = 200
        self.wall_list.append(wall)

        # create a row of walls using a loop
        for x in range(173, 650, 64):
            wall = arcade.Sprite(":resources:images/tiles/boxCrate_double.png",
                                 SPRITE_SCALING_BOX)
            wall.center_x = x
            wall.center_y = 350
            self.wall_list.append(wall)

        # create a block of walls using a list of coordinates
        coordinate_list = [[400, 500],
                           [470, 500],
                           [400, 570],
                           [470, 570]]
        for coordinate in coordinate_list:
            wall = arcade.Sprite(":resources:images/tiles/boxCrate_double.png",
                                 SPRITE_SCALING_BOX)
            wall.center_x = coordinate[0]
            wall.center_y = coordinate[1]
            self.wall_list.append(wall)

        # physics engine references to sprite and walls it can't run into
        self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite, self.wall_list)

    def on_key_press(self, key: int, modifiers: int):
        if key == arcade.key.UP:
            self.player_sprite.change_y = MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.player_sprite.change_y = - MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.player_sprite.change_x = MOVEMENT_SPEED
        elif key == arcade.key.LEFT:
            self.player_sprite.change_x = -MOVEMENT_SPEED

    def on_key_release(self, key: int, modifiers: int):
        if key == arcade.key.UP or key == arcade.key.DOWN:
            self.player_sprite.change_y = 0
        elif key == arcade.key.RIGHT or key == arcade.key.LEFT:
            self.player_sprite.change_x = 0

    def on_draw(self):
        arcade.start_render()
        self.wall_list.draw()
        self.player_list.draw()

    def update(self, delta_time):
        self.physics_engine.update()

def main():
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
