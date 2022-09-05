# Снежинка Коха

from funcs import main

axiom = 'F--F'
rules = {'F': 'F+F--F+F'}
iterations = 4
angle = 60

main(iterations, axiom, rules, angle, lenght=8, size=2, y_offset=-100, x_offset=100, offset_angle=0, wight=450, height=450)
