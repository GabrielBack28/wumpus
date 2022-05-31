import turtle
import random

window = turtle.Screen()
window.bgcolor("black")
window.title("Wumpus World")
window.setup(width=1.0, height=1.0, startx=None, starty=None)
width = 20
height = 10
gold_qty = 3
abyss_qty = 5
gold_won = []

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


# def restrict_position(): restringir onde pode renderizar os quadrados


def setup_maze():
    for x in range(width):
        for y in range(height):
            screen_x = get_screen_x(x)
            screen_y = get_screen_y(y)
            maze_square.goto(screen_x, screen_y)
            maze_square.stamp()

    agent.width = 0
    agent.height = 0
    screen_x = get_screen_x(agent.width)
    screen_y = get_screen_y(agent.height)
    agent_square.goto(screen_x, screen_y)

    for x in range(gold_qty):
        gold_width = random.randint(0, width - 1)
        gold_height = random.randint(0, height - 1)
        screen_x = get_screen_x(gold_width)
        screen_y = get_screen_y(gold_height)
        gold_square.goto(screen_x, screen_y)
        gold_square.stamp()
        new_gold = Obstacle()
        new_gold.height = gold_height
        new_gold.width = gold_width
        golds.append(new_gold)

    for x in range(abyss_qty):
        abyss_width = random.randint(0, width - 1)
        abyss_height = random.randint(0, height - 1)
        if not (abyss_height == wumpus.height and abyss_width == wumpus.width):
            new_abyss = Obstacle()
            new_abyss.height = abyss_height
            new_abyss.width = abyss_width
            abyss.append(new_abyss)
            define_obstacle(abyss_square, breeze_square, abyss_width, abyss_height)

    wumpus.width = random.randint(0, width-1)
    wumpus.height = random.randint(0, height-1)
    define_obstacle(wumpus_square, bad_smell_square, wumpus.width, wumpus.height)


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

agent_square.goto(get_screen_x(1), get_screen_y(0))
agent_square.goto(get_screen_x(2), get_screen_y(0))

window.exitonclick()
