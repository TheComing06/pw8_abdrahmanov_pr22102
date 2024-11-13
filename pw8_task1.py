class Soda:
    def __init__(self, added):
        self.additive = added

    def show_my_drink(self):
        if self.additive == "":
            print('Обычная газировка')
        else:
            print(f'Газировка и {self.additive}')

a = input("Введите название добавки(если есть):")
cola = Soda(a)
cola.show_my_drink()