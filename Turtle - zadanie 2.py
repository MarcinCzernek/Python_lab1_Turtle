#import turtle
import turtle

#tworzę instancje turtle o nazwie 'pen'
pen = turtle.Turtle()

#kursor jest niewidoczny
pen.hideturtle()
#prędkość poruszania się kursora - najszybsza
pen.speed(0)

#Funkcja rysująca jeden kwadrat
def square(size):
    for i in range(4):
        pen.forward(size)
        pen.left(90)

#Funkcja za pomocą rekurencji, wywołuje w sobie funkcję, tworząc kwadraty o malejącym rozmiarze
def new_nested_square(size, shrinkFactor, minimumSize):
    if size < minimumSize:
        pass
    else:
        square(size)
        new_nested_square(size*shrinkFactor, shrinkFactor, minimumSize)

#wywołanie metody
new_nested_square(300, 0.90, 1)

#Ekran turtle zostanie wyłączony, po kliknięciu myszką na niego, a nie zaraz po narysowaniu kwadratu
turtle.exitonclick()
