# Task 5
# Напишите программу, которая принимает на вход координаты двух точек 
# и находит расстояние между ними в 2D пространстве.
# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

print('input coordinates of 1st point')
x1, y1 = int(input('x: ')), int(input('y: '))
print('input coordinates of 2nd point')
x2, y2 = int(input('x: ')), int(input('y: '))
print('distance between points is: ', round(((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5, 2))

