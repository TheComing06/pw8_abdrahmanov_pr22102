class KgToPounds:
    def __init__(self, kg):
        self.__kg = kg

    @property
    def kg(self):
        return self.__kg

    #@kg.toPounds
    #def to_pounds(self):
    #    return self.__kg * 2.205
    
    @kg.setter
    def set_kg(self, new_kg):
        if type(new_kg) == int:
            self.__kg = new_kg
        else:
            raise ValueError('Килограммы задаются только числами')

    @kg.getter
    def get_kg(self):
        print(self.__kg * 2.205)
    
kg = int(input("Введите количество килограмм:"))

kilo = KgToPounds(kg)
kilo.set_kg(kg)
kilo.get_kg()