# Квадратный остров Коха

from funcs import main

axiom = 'F+F+F+F'
rules = {'F': 'F-F+F+FFF-F-F+F'}
iterations = 3
angle = 90

main(iterations, axiom, rules, angle, lenght=8, size=2, y_offset=0, x_offset=-400, offset_angle=0, wight=450, height=450)
