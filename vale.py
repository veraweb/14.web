import turtle

# Configuración inicial
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Feliz San Valentín ")

# Crear un objeto Turtle
pen = turtle.Turtle()
pen.shape("turtle")
pen.speed(2)

# Función para dibujar un corazón con dos colores
def draw_heart():
    # Mitad izquierda del corazón (amarillo)
    pen.color("yellow")
    pen.begin_fill()
    pen.left(50)
    pen.forward(133)
    pen.circle(50, 200)
    pen.right(140)
    pen.circle(50, 200)
    pen.forward(133)
    pen.end_fill()

    # Mitad derecha del corazón (verde)
    pen.color("green")
    pen.begin_fill()
    pen.left(50)
    pen.forward(133)
    pen.circle(50, 200)
    pen.right(140)
    pen.circle(50, 200)
    pen.forward(133)
    pen.end_fill()

# Mover el lápiz a la posición adecuada
pen.up()
pen.goto(0, -50)
pen.down()

# Dibujar el corazón
draw_heart()

# Escribir el mensaje
pen.up()
pen.goto(-80, -150)
pen.color("white")
pen.write("mi bebe  hermosa TE amo ", font=("Arial", 24, "bold"))

# Ocultar el lápiz y finalizar
pen.hideturtle()
turtle.done()