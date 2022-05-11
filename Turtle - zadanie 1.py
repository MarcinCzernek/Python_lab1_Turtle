#import turtle
import turtle

#tworzę instancje turtle o nazwie 'pen'
pen = turtle.Turtle()

#Wybieram kształt rysującego kursora
pen.shape('turtle')
drawing_area = turtle.Screen()
#Obrót kursora w lewo
pen.left(90)
#Ruch i rysowanie linni 1 boku kwadratu
pen.forward(200)
#Obrót kursora w prawo
pen.right(90)
#Ruch i rysowanie linni 2 boku kwadratu
pen.forward(200)
pen.right(90)
#Ruch i rysowanie linni 3 boku kwadratu
pen.forward(200)
pen.right(90)
#Ruch i rysowanie linni 4 boku kwadratu
pen.forward(200)
pen.right(90)

#Ekran turtle zostanie wyłączony po kliknięciu myszką na niego a nie zaraz po narysowaniu kwadratu
turtle.exitonclick()
