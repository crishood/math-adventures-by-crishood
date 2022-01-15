# Welcome to the path 
print('Python funciona en este entorno de desarrollo, bien jugado Cris')

from turtle import *
color('yellow', 'green')
begin_fill()
while True:
    forward(200)
    left(170)
    if abs(pos()) < 1:
        break
end_fill()
done()