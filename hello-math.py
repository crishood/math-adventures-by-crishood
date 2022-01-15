# Welcome to the path 
print('Python funciona en este entorno de desarrollo y ahora puedes usar turtle, bien jugado Cris, además de eso acabo de configurar las llaves de seguridad de mi entorno de WSL')

from turtle import *
color('yellow', 'green')
shape('turtle')
begin_fill()
while True:
    forward(200)
    left(170)
    if abs(pos()) < 1:
        break
end_fill()
done()
