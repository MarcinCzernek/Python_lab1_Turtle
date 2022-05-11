import turtle              # import turtle
pen = turtle.Turtle()      # tworzy instancję turtle o nazwie pen

# ustawia szybkość kursora, (1–10)
pen.speed(0)
# ustawia kierunek
pen.setheading(90)
#kieruje kursor do góry
pen.penup()
#kieruje kursor do pozycji bezwzględnej
pen.goto(-300, -300)
#kieruje kursor w dół
pen.pendown()

#funkcja rysująca pojedynczy kwadrat
def draw_triangle(length):
    pen.setheading(180)      # ustawia kierunek kursora na lewo
    for i in range(3):       # rysuje 3 boki
        pen.rt(120)          # bróć kursor o 120 stopni zgodnie z ruchem wskazówek zegara
        pen.fd(length)       # rysuje bok
                             # kursor będzie skierowany w lewo (180)

#funkcja rysująca kwadrat sierpińskiego za pomocą rekurencji
def sierpinski_order_n_recursive(n , length):
    pen.speed(0) # ustawia szybkość rysowania, (1–10)
    #n liczba trójkątów wewnątrz 1 trójkątu
    if n == 1:
        draw_triangle(length)
    else:
        sierpinski_order_n_recursive(n - 1, length)
        pen.rt(120) #pen.rt(angle) obraca się w prawo domyslnie 90
        pen.fd(length * 2 ** (n - 2)) #pen.fd()  # kursor rusza na przód
        sierpinski_order_n_recursive(n -1, length)
        pen.lt(120) #pen.lt(angle) obraca kursor w lewo domyślnie 90
        pen.fd(length * 2 ** (n - 2))
        sierpinski_order_n_recursive(n - 1, length)
        pen.fd(length * 2 ** (n - 2))

#wywołanie metody
sierpinski_order_n_recursive(7,10)
#Ekran turtle zostanie wyłączony, po kliknięciu myszką na niego, a nie zaraz po narysowaniu kwadratu
turtle.exitonclick()