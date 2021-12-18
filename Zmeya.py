from tkinter import *
import random

"""Константы"""
w = 800
h = 600
size = 20
speed = 100
lenght = 3
window = Tk()
window.title("Zmeyka")
window.resizable(False, False)


class Snake:
    
    def __init__(self):
        self.lenght = lenght
        self.coord = [[100, 100]] 
        self.squares = []

        square = c.create_rectangle(100, 100, 100 + size, 100 + size, fill = "blue")
        self.squares.append(square)


class Food:
    def __init__(self):
        x = random.randint(0,w / size - 5) * size
        y = random.randint(0,h / size - 5) * size

        self.coord = [x,y]

        c.create_rectangle(x, y, x + size, y + size, fill = "red")


def move (snake, food):
    for x, y in snake.coord:
        square = c.create_rectangle(x, y, x + size, y + size, fill = "green")
    x, y = snake.coord[0]

    if direction == 'down':
        y += size
    elif direction == 'up':
        y -= size
    elif direction == 'left':
        x -= size
    elif direction == 'right':
        x += size

    snake.coord.insert(0, (x,y))
    square = c.create_rectangle(x, y, x + size, y + size, fill = "blue")
    snake.squares.insert(0, square)

    if x == food.coord[0] and y == food.coord[1]:
        global score
        score += 1
        lscore.config(text = "Score: {}".format(score))
        c.delete("food")

        food = Food()
    else:
        x, y = snake.coord[-1]
        square = c.create_rectangle(x, y, x + size, y + size, fill = "black")

        
        del snake.coord[-1]
        c.delete(snake.squares[-1])
        del snake.squares[-1]

    if (check(snake)):
        game_over()
    else:
        window.after(speed, move, snake, food)


def change_direction(new):
    global direction

    if (new == "down"):
        if direction != "up":
            direction = new
    elif (new == "up"):
        if direction != "down":
            direction = new
    elif (new == "right"):
        if direction != "left":
            direction = new
    elif (new == "left"):
        if direction != "right":
            direction = new


def check(snake):
    x, y = snake.coord[0]

    if x < 0 or x >= w:
        return True
    elif y < 0 or y >= h:
        return True
    for lenght in snake.coord[1:]:
        if x == lenght[0] and y == lenght[1]:
            return True


def game_over():
    c.delete(ALL)
    c.create_text(400, 300, font = ('Arial', 15), text = "Game over", fill = "red")
    c.create_text(400, 350 , font = ('Arial', 15), text = "Try again", fill = "red")
    
    
    

score = 0
direction = "down"

lscore = Label(window, text = "Score: {}".format(score), font = ('Arial', 40))
lscore.pack()

c = Canvas(window, height = h, width = w, bg = "black")
c.pack()

window.geometry("800x650")

window.bind("s", lambda event: change_direction("down"))
window.bind("w", lambda event: change_direction("up"))
window.bind("d", lambda event: change_direction("right"))
window.bind("a", lambda event: change_direction("left"))

snake = Snake()
food = Food()

move(snake, food)

window.mainloop()

