from modul_5_1 import House

# импортируем предидущую задачу и создаём наследственный класс
class House1(House):
        def __len__(self):
                return self.number_of_floors


        def __str__(self):
                return f'Название: {self.name}, кол-во этажей: {self.number_of_floors}'


h1 = House1('ЖК Эльбрус', 10)
h2 = House1('ЖК Акация', 20)
print(h1)
print(h2)
print(len(h1))
print(len(h2))