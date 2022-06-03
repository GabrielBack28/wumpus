import turtle
import random
import numpy as np

window = turtle.Screen()
window.bgcolor("black")
window.title("Wumpus World")
window.setup(width=1.0, height=1.0, startx=None, starty=None)
width = 20
height = 10
gold_qty = 3
abyss_qty = 5
gold_won = []
maze = []


class MazePosition:
    wumpus = False
    abyss = False
    bad_smell = False
    breeze = False
    gold = False


class Obstacle:
    width = 0
    height = 0


class MazeSquare(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("white")
        self.penup()
        self.speed(0)


class GoldSquare(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("yellow")
        self.penup()
        self.speed(0)


class AbyssSquare(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("black")
        self.penup()
        self.speed(0)


class BreezeSquare(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("gray")
        self.penup()
        self.speed(0)


class WumpusSquare(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("blue")
        self.penup()
        self.speed(0)


class BadSmellSquare(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("green")
        self.penup()
        self.speed(0)


class AgentSquare(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("brown")
        self.penup()
        self.speed(0)


def get_screen_x(x):
    return -588 + (x * 24)


def get_screen_y(y):
    return 288 - (y * 24)


def define_obstacle(obstacle_class, perception_class, coordinate_x, coordinate_y):
    screen_x = get_screen_x(coordinate_x)
    screen_y = get_screen_y(coordinate_y)
    obstacle_class.goto(screen_x, screen_y)
    obstacle_class.stamp()

    if coordinate_x + 1 <= width - 1:
        screen_x_right = get_screen_x(coordinate_x + 1)
        perception_class.goto(screen_x_right, screen_y)
        perception_class.stamp()

    if coordinate_x - 1 >= 0:
        screen_x_left = get_screen_x(coordinate_x - 1)
        perception_class.goto(screen_x_left, screen_y)
        perception_class.stamp()

    if coordinate_y + 1 <= height - 1:
        screen_y_right = get_screen_y(coordinate_y + 1)
        perception_class.goto(screen_x, screen_y_right)
        perception_class.stamp()

    if coordinate_y - 1 >= 0:
        screen_y_left = get_screen_y(coordinate_y - 1)
        perception_class.goto(screen_x, screen_y_left)
        perception_class.stamp()


def setup_maze():
    for x in range(width):
        maze.append([])
        for y in range(height):
            screen_x = get_screen_x(x)
            screen_y = get_screen_y(y)
            maze_square.goto(screen_x, screen_y)
            maze_square.stamp()
            maze[x].append(MazePosition())


def setup_obstacles():
    wumpus_width = random.randint(0, width - 1)
    wumpus_height = random.randint(0, height - 1)
    screen_x = get_screen_x(wumpus_width)
    screen_y = get_screen_y(wumpus_height)
    wumpus_square.goto(screen_x, screen_y)
    wumpus_square.stamp()
    maze[wumpus_width][wumpus_height].wumpus = True

    for x in range(gold_qty):
        gold_width = random.randint(0, width - 1)
        gold_height = random.randint(0, height - 1)
        screen_x = get_screen_x(gold_width)
        screen_y = get_screen_y(gold_height)
        gold_square.goto(screen_x, screen_y)
        gold_square.stamp()
        maze[gold_width][gold_height].gold = True

    for x in range(abyss_qty):
        abyss_width = random.randint(0, width - 1)
        abyss_height = random.randint(0, height - 1)
        screen_x = get_screen_x(abyss_width)
        screen_y = get_screen_y(abyss_height)
        gold_square.goto(screen_x, screen_y)
        gold_square.stamp()
        maze[abyss_width][abyss_height].abyss = True


maze_square = MazeSquare()
abyss_square = AbyssSquare()
breeze_square = BreezeSquare()
wumpus_square = WumpusSquare()
bad_smell_square = BadSmellSquare()
agent_square = AgentSquare()
gold_square = GoldSquare()
wumpus = Obstacle()
agent = Obstacle()
abyss = []
golds = []
setup_maze()
setup_obstacles()

window.exitonclick()
