from turtle import Turtle
STARTING_POS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.turties = []
        self.create_snake()
        self.head = self.turties[0]

    def create_snake(self):
        for turty_pos in STARTING_POS:
            self.add_segment(turty_pos)

    def add_segment(self, position):
        turt = Turtle("square")
        turt.penup()
        turt.goto(position)
        turt.color("white")
        self.turties.append(turt)

    def extend(self):
        self.add_segment(self.turties[-1].position())

    def move(self):

        for num in range(len(self.turties) - 1, 0, -1):
            new_x = self.turties[num - 1].xcor()
            new_y = self.turties[num - 1].ycor()
            self.turties[num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
