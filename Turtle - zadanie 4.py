import math
import turtle  # import turtle

#tworzę instancje turtle o nazwie 'pen'
pen = turtle.Turtle()

#1. Pierwszy fraktal

class Triangle:
    def __init__(self, length):
        self.set = pen.setheading(180)
        self.length = length

    def draw_triangle(self):
         for i in range(3):
            for i in range(3):
                pen.rt(120)
                pen.fd(self.length)
            pen.rt(120)
            r = 80
            pen.circle(r)


# *** Wywołanie fraktala ***

#tr = Triangle(80)
#tr.draw_triangle()



#2. Drugi fraktal

class Tree:
    def __init__(self):
        pen.speed(-1)
        pen.setheading(90)
        pen.penup()
        pen.goto(0, -200)
        pen.pendown()
        pen.shape("circle")

    def draw_branch(self, t , len):
        if len == 0: return
        nt = t.clone()
        nt.forward(50)
        nt.left(20)
        self.draw_branch(nt, len - 1)
        nt.right(40)
        self.draw_branch(nt, len - 1)

# *** Wywołanie fraktala ***

#tree = Tree()
#tree.draw_branch(pen,7)
#window = turtle.Screen()
#window.exitonclick()



#3.Trzeci fraktal

class Circle:
    def __init__(self, radius):
        #r - promień okręgu
        self.radius = radius

    def draw_circles(self, radius):
        pen.speed(10)
        # Pętla do drukowania koncentrycznych okręgów
        for i in range(50):
            pen.circle(radius * i)
            pen.up()
            pen.sety((radius * i) * (-1))
            pen.down()


# *** Wywołanie fraktala ***

#circle = Circle(5)
#cir = circle.radius = 5
#circle.draw_circles(cir)




#4.Czwarty fraktal

class Star:
    def __init__(self,x,y,direction,r):
        self.x = x
        self.y = y
        self.direction = direction
        self.r = r

    def print_star(self): # x,y to centrum
        pen.up()
        pen.goto(self.x, self.y)
        pen.seth(self.direction)
        pen.fd(self.r)
        pen.right(180-18)
        pen.down()
        length = self.r*math.sin(math.pi*2/5)/(1+math.sin(math.pi/10))
        for _ in range(5):
            pen.fd(length)
            pen.left(72)
            pen.fd(length)
            pen.right(180-36)


# *** Wywołanie fraktala ***

star = Star(4,5,90,200)
star.print_star()



turtle.exitonclick()
