from tkinter import *
import random


w = 800
h = 600
size = 20
root = Tk()
root.title("Zmeyka")
root.resizable(False, False)


class Snake:
    """Класс содержит функцию __init__, создающую змею"""
    def __init__(self):
        """функция принимает на входе
        self - представляет экземпляр самого объекта
        переменные:
        self.lenght - длина змеи
        self.coord - массив с координатами положения частей змеи
        self.squares - массив, содержащий квадраты змеи
        с - поле
        square - переменная,добавляемая в массив. Необходима для отрисовки квадрата на поле
        Функция на выходе возвращает массив,с отрисованными квадратами"""
        self.lenght = 1
        self.coord = [[100, 100]] 
        self.squares = []
        square = c.create_rectangle(100, 100, 100 + size, 100 + size, fill = "blue")
        self.squares.append(square)


class Food:
    """Класс содержит функцию __init__, которая генерирует еду"""
    def __init__(self):
        """Функция принимает на входе
        self - представляет экземпляр самого объекта 
        переменные:
        x - переменная, характеризующуя координату случайно появляющегося квадрата по ширине
        y - переменная, характеризующуя координату случайно появляющегося квадрата по высоте
        self.coord - массив,содержащий координаты квадрата еды
        с - Поле
        на выходе фунция рисует на поле квадрат еды"""
        x = random.randint(0,w / size - 5) * size
        y = random.randint(0,h / size - 5) * size
        self.coord = [x,y]
        c.create_rectangle(x, y, x + size, y + size, fill = "red")


def move (snake, food):
    """Движение змеи.На вход получает параметры классов Snake и Food
       x и y - переменные, обозначающие координаты головы змие
       snake.coord - массив класса Snake
       snake.squares - массив класса Snake, заполняемый квадратами с новыми координатами
       score - глобальная переменная, необходимая для отображения счёта
       lscore - текстовое сообщение
       с - поле
       На выходе функция выдаёт массив с новыми отрисованными квадратами, изменённый счёт и вызывает функцию end, при нарушении правил игры."""
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
        end()
    else:
        root.after(100, move, snake, food)


def change_direction(new):
    """На входе принимает параметр перемещения
    direction - глобальная переменная, обозначающая действующее направление движения змеи
    на выходе функция выдаёт новое направления движения."""
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
    """На вход подаются параметры змеи
    x и y - переменный,обозначающие координаты головы змеи
    w - константа
    h - константа
    lenght - параметр класса Snake
    snake.coord - массив с координатами квадратов змеи
    На выходе функция выдаёт корректность выполнения требований для продолжения игры"""
    x, y = snake.coord[0]
    if x < 0 or x >= w:
        return True
    elif y < 0 or y >= h:
        return True
    for lenght in snake.coord[1:]:
        if x == lenght[0] and y == lenght[1]:
            return True


def end():
    """с - поле
    На выходе убирает все элементы с поля и выводит надпись об окончании игры."""
    c.delete(ALL)
    c.create_text(400, 300, font = ('Arial', 15), text = "Game over", fill = "red")
    
  
score = 0
direction = "right"
lscore = Label(root, text = "Score: {}".format(score), font = ('Arial', 40))
lscore.pack(side = TOP)
c = Canvas(root, height = h, width = w, bg = "black")
c.pack(side = BOTTOM)
#Использует lambda в привязке,чтобы принять дополнительное событие толькопри использовании команды bind,но не передавать его последней команде https://coderoad.ru/7299955/Tkinter-%D0%BF%D1%80%D0%B8%D0%B2%D1%8F%D0%B7%D0%BA%D0%B0-%D1%84%D1%83%D0%BD%D0%BA%D1%86%D0%B8%D0%B8-%D1%81-%D0%B0%D1%80%D0%B3%D1%83%D0%BC%D0%B5%D0%BD%D1%82%D0%B0%D0%BC%D0%B8-%D0%BA-%D0%B2%D0%B8%D0%B4%D0%B6%D0%B5%D1%82%D1%83
root.bind("s", lambda event: change_direction("down"))
root.bind("w", lambda event: change_direction("up"))
root.bind("d", lambda event: change_direction("right"))
root.bind("a", lambda event: change_direction("left"))
snake = Snake()
food = Food() 
move(snake, food)
root.mainloop()

