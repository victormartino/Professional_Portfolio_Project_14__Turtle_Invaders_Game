from turtle import Turtle

wall_x_position = -390
wall_y_position = -100
TOTAL_WALL_BRICKS = 100
BRICK_WIDTH = 5
BRICKS_PER_WALL_ROW = TOTAL_WALL_BRICKS // 5  # Use integer division
WALL_X_SPACING = 226  # I tried some different numbers until I was happy with the result

class Walls(Turtle):
    def __init__(self):
        super().__init__()
        self.all_walls = []
        self.create_walls()

    def create_walls(self):
        for wall in range(4):  # Create four walls
            wall_bricks = []  # List to store bricks in the current wall
            new_x_position = wall_x_position
            new_y_position = wall_y_position

            for i in range(TOTAL_WALL_BRICKS):  # Create bricks in the current wall
                brick = Turtle()
                brick.shape("square")
                brick.penup()
                brick.shapesize(0.1, 0.1)
                brick.color("green")
                brick.goto(new_x_position, new_y_position)
                new_x_position += BRICK_WIDTH

                if (i + 1) % BRICKS_PER_WALL_ROW == 0:
                    new_x_position = wall_x_position
                    new_y_position -= BRICK_WIDTH

                wall_bricks.append(brick)  # Add the brick to the current wall
            self.all_walls.append(wall_bricks)  # Add the current wall to the list of all walls

        # Move the remaining three walls horizontally
        new_wall_x_increment = WALL_X_SPACING
        for wall in self.all_walls[1:]:  # Skip the first wall
            for brick in wall:
                brick.goto(brick.pos()[0] + new_wall_x_increment, brick.pos()[1])
            new_wall_x_increment += WALL_X_SPACING
