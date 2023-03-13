""" This is a sample program
    sufrom the second lab video
"""

# load the library containing graphics functions
import arcade

arcade.open_window(600, 600, "Drawing Example")
arcade.set_background_color(arcade.csscolor.SKY_BLUE)

# prepare to draw
arcade.start_render()

# drawing code here
# rectangle left at 0, right at 599, top at 300, bottom at 0
arcade.draw_lrtb_rectangle_filled(0, 599, 300, 0, arcade.csscolor.GREEN)

# tree trunk center 100, 320, width of 20 height of 60
arcade.draw_rectangle_filled(100, 320, 20, 60, arcade.csscolor.SIENNA)
arcade.draw_circle_filled(100, 350, 30, arcade.csscolor.DARK_GREEN)

# draw another tree
arcade.draw_rectangle_filled(200, 320, 20, 60, arcade.csscolor.SIENNA)
arcade.draw_ellipse_filled(200, 370, 60, 80, arcade.csscolor.DARK_GREEN)

# arc is like ellipse with a starting and ending angle
# another tree with an arc for a top
arcade.draw_rectangle_filled(300, 320, 20, 60, arcade.csscolor.SIENNA)
arcade.draw_arc_filled(300, 340, 60, 100, arcade.csscolor.DARK_GREEN, 0, 180)

# Use a triangle to draw a pine tree
arcade.draw_rectangle_filled(400, 320, 20, 60, arcade.csscolor.SIENNA)
arcade.draw_triangle_filled(400, 400, 370, 320, 430, 320, arcade.csscolor.DARK_GREEN)

# use a polygon to draw the top
arcade.draw_rectangle_filled(500, 320, 20, 60, arcade.csscolor.SIENNA)
arcade.draw_polygon_filled(((500, 400),
                           (480, 360),
                           (470, 320),
                           (530, 320),
                           (520, 360)
                           ), arcade.csscolor.DARK_GREEN)

# the sun
arcade.draw_circle_filled(500, 550, 40, arcade.color.YELLOW)
arcade.draw_line(500, 550, 400, 550, arcade.color.YELLOW, 3)
arcade.draw_line(500, 550, 600, 550, arcade.color.YELLOW, 3)
arcade.draw_line(500, 550, 500, 450, arcade.color.YELLOW, 3)
arcade.draw_line(500, 550, 500, 650, arcade.color.YELLOW, 3)

arcade.draw_line(500, 550, 550, 600, arcade.color.YELLOW, 3)
arcade.draw_line(500, 550, 550, 500, arcade.color.YELLOW, 3)
arcade.draw_line(500, 550, 450, 600, arcade.color.YELLOW, 3)
arcade.draw_line(500, 550, 450, 500, arcade.color.YELLOW, 3)

arcade.draw_text("Arbor Day!", 150, 230, arcade.color.BLACK, 24)

# stop drawing
arcade.finish_render()

arcade.run()
