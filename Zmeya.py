from tkinter import *
import random

"""Константы"""
w = 800
h = 600
size = 20
lenght = 3
root = Tk()
root.title("Zmeyka")
root.resizable(False, False)


class Snake:
    """Класс базы змеи."""
    def __init__(self):
        """На выходе функция выдаёт массив квадратов змеи."""
        self.lenght = lenght
        self.coord = [[100, 100]] 
        self.squares = []
        square = c.create_rectangle(100, 100, 100 + size, 100 + size, fill = "blue")
        self.squares.append(square)


class Food:
    """Генерация еды для змеи в случайном месте на поле."""
    def __init__(self):
        """Функция определяет случайные координаты на поле
        и на выходерасиут там красный квадрат(еду)"""
        x = random.randint(0,w / size - 5) * size
        y = random.randint(0,h / size - 5) * size
        self.coord = [x,y]
        c.create_rectangle(x, y, x + size, y + size, fill = "red")


def move (snake, food):
    """Движение змеи.На вход получает параметры классов Snake и Food
        На выходе определяет окончание игры и задаёт условия перемещения. """
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
    """Процесс поедания"""
    if x == food.coord[0] and y == food.coord[1]:
        global score
        score += 1
        lscore.config(text = "Score: {}".format(score))
        c.delete("food")
        food = Food()
    """Убираем лишний сегмент змеи"""
    else:
        x, y = snake.coord[-1]
        square = c.create_rectangle(x, y, x + size, y + size, fill = "black")
        del snake.coord[-1]
        c.delete(snake.squares[-1])
        del snake.squares[-1]
    if (check(snake)):
        game_over()
    else:
        root.after(100, move, snake, food)


def change_direction(new):
    """Измение направления движения. На входе принимает параметры перемещения и выдаёт изменение направления движения."""
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
    """Проверка соблюдения правил. На вход подаются параметры змеи. На выход устанавливаются параметры окончания игры."""
    x, y = snake.coord[0]
    if x < 0 or x >= w:
        return True
    elif y < 0 or y >= h:
        return True
    for lenght in snake.coord[1:]:
        if x == lenght[0] and y == lenght[1]:
            return True


def game_over():
    """При окончании игры. На выходе убирает все элементы с поля и выводит надпись об окончании игры."""
    c.delete(ALL)
    c.create_text(400, 300, font = ('Arial', 15), text = "Game over", fill = "red")
    
    
score = 0
direction = "down"
lscore = Label(root, text = "Score: {}".format(score), font = ('Arial', 40))
lscore.pack()
c = Canvas(root, height = h, width = w, bg = "black")
c.pack()
"""Использует lambda в привязке,чтобы принять дополнительное событие только
при использовании командыbind,но не передавать его последней команде
https://coderoad.ru/7299955/Tkinter-%D0%BF%D1%80%D0%B8%D0%B2%D1%8F%D0%B7%D0%BA%D0%B0-%D1%84%D1%83%D0%BD%D0%BA%D1%86%D0%B8%D0%B8-%D1%81-%D0%B0%D1%80%D0%B3%D1%83%D0%BC%D0%B5%D0%BD%D1%82%D0%B0%D0%BC%D0%B8-%D0%BA-%D0%B2%D0%B8%D0%B4%D0%B6%D0%B5%D1%82%D1%83"""
root.bind("s", lambda event: change_direction("down"))
root.bind("w", lambda event: change_direction("up"))
root.bind("d", lambda event: change_direction("right"))
root.bind("a", lambda event: change_direction("left"))
snake = Snake()
food = Food()
move(snake, food)
root.mainloop()

