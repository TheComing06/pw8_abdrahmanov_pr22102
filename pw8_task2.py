class TriangleChecker:
    def __init__(self, a, b, c):
        self.sideA = a
        self.sideB = b
        self.sideC = c

    def is_triangle(self):
        try:
            int(self.sideA)
            int(self.sideB)
            int(self.sideC)

            if int(self.sideA) == 0 or int(self.sideB) == 0 or int(self.sideC) == 0:
                print("Жаль, но из этого треугольник не сделать!")
            elif int(self.sideA) < 0 or int(self.sideB) < 0 or int(self.sideC) < 0:
                print("С отрицательными числами ничего не выйдет!")
            else:
                print("Ура, можно построить треугольник!")

        except ValueError:
            print("Нужно вводить только числа!")
        

a = input("Введите отрезок А:")
b = input("Введите отрезок B:")
c = input("Введите отрезок C:")

triangle = TriangleChecker(a, b, c)
triangle.is_triangle()