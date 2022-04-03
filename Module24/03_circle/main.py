import math

class Circle:
    index = 0
    center = [0, 0]
    rad = 1

    def __init__(self, index, center, rad):
        self.index = index
        self.center = center
        self.rad = rad

    def info(self):
        print('Круг {}:\nЦентр круга: ({},{})\nРадиус: {}'.format(
            self.index, self.center[0], self.center[1], self.rad))

    def square(self):
        i_area = math.pi * self.rad ** 2
        print('Площадь круга:', round(i_area, 2))

    def perimeter(self):
        i_perim = 2 * math.pi * self.rad
        print('Периметр окружности:', round(i_perim, 2))

    def increase(self, K):
        self.rad *= K
        print('\nНовые параметры окружности:')
        self.info()

def distance(coord1, coord2):
    horizontal = abs(coord1[0] - coord2[0])
    vertical = abs(coord1[1] - coord2[1])
    dist = math.sqrt(horizontal ** 2 + vertical ** 2)
    return dist


import random
circles = [Circle(index, [random.randint(0, 100), random.randint(0, 100)], random.randint(1, 10))
           for index in range(1, 6)]
while True:
    circle_choise = int(input('Выберите номер окружности (от 1 до 5): '))
    if circle_choise > 5 or circle_choise < 1:
        print('Такой окружности не существует. Выход из программы')
        break
    else:
        for i_circle in circles:
            if i_circle.index == circle_choise:
                the_circle = i_circle
                break
        while True:
            action = int(input('\nВыберите действие: (1- Площадь круга; 2- Периметр окружности; 3 - увеличить в К раз; '
                           '4 - определить, пересекается ли с другой окружностью?: '))
            if action == 1:
                the_circle.info()
                the_circle.square()
            elif action == 2:
                the_circle.info()
                the_circle.perimeter()
            elif action == 3:
                K = int(input('Введите число раз, в которое должна увеличиться окружность: '))
                print('Начальные параметры:')
                the_circle.info()
                the_circle.increase(K)
            elif action == 4:
                intersections = []
                for i_circle in circles:
                    if i_circle.index != the_circle.index:
                        i_dist = distance(the_circle.center, i_circle.center)
                        if i_dist < (the_circle.rad + i_circle.rad):
                            intersections.append(i_circle.index)
                if intersections != []:
                    print('Окружность имеет пересечения со следующими окружностями:', intersections, end='\n')
                    for index in intersections:
                        i_circle = circles[index - 1]
                        i_circle.info()
                        print('Расстояние между центрами: {}, Радиусы: {}; {}\nСумма радиусов: {}\n'.format(
                            round(i_dist, 1), the_circle.rad, i_circle.rad, the_circle.rad + i_circle.rad))
                else:
                    print('Пересечений с другими окружностями не обнаружено')
            else:
                print('Неверная команда.')
                break


