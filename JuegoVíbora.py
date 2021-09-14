"""Snake, classic arcade game.

Exercises

1. How do you make the snake faster or slower?
2. How can you make the snake go around the edges?
3. How would you move the food?
4. Change the snake to respond to mouse clicks.

"""

from random import randrange
from random import choice
from turtle import *

from freegames import square, vector

food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)

colorList = ['gray', 'blue', 'black', 'yellow', 'purple']
snakeColor = choice(colorList)
foodColor = choice(colorList)

while snakeColor == foodColor:
    foodColor = choice(colorList)

def change(x, y):
    "Change snake direction."
    aim.x = x
    aim.y = y

def inside(head):
    "Return True if head inside boundaries."
    return -200 < head.x < 190 and -200 < head.y < 190


def move():
    global snakeColor, foodColor
    "Move snake forward one segment."
    head = snake[-1].copy()
    head.move(aim)

    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return

    snake.append(head)

    foodXlist = [food.x]
    foodYlist = [food.y]
    counter = -1
    
    if head == food:
        counter += 1        
        print('Snake:', len(snake))
        food.x = (choice([-1, 0, 1]) * 10) + foodXlist[counter]
        food.y = (choice([-1, 1]) * 10) + foodYlist[counter]
        # food.x = randrange(-15, 15) * 10
        # food.y = randrange(-15, 15) * 10
        if not inside(food):
            food.x = 10
            food.y = 10
            
        foodXlist.append(food)
        foodYlist.append(food)

    else:
        snake.pop(0)

    clear()
    
    for body in snake:
        square(body.x, body.y, 9, snakeColor)
        
    square(food.x, food.y, 9, foodColor)
    update()
    ontimer(move, 100)


setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
move()
done()