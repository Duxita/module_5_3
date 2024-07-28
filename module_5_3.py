class House:
    def __init__(self,name,num):
        self.name = name
        self.number_of_floors = num
    def go_to (self,new_floor):
        self.new_floor = new_floor
        if new_floor >= 1 and new_floor <= self.number_of_floors:
            for floor in range(1,new_floor +1):
                print(floor)
        if new_floor < 1 or new_floor > self.number_of_floors:
                print("Такого этажа не существует")
    def __len__(self):
        return self.number_of_floors
    def __str__(self):
        return self.name
    def __eq__(self, other):
        return isinstance(other, House) and self.number_of_floors == other.number_of_floors
    def __lt__(self, other):
        return isinstance(other, House) and self.number_of_floors < other.number_of_floors
    def __le__(self, other):
        return isinstance(other, House) and self.number_of_floors <= other.number_of_floors
    def __gt__(self, other):
        return isinstance(other, House) and self.number_of_floors > other.number_of_floors
    def __ge__(self, other):
        return isinstance(other, House) and self.number_of_floors >= other.number_of_floors
    def __ne__(self, other):
        return isinstance(other, House) and self.number_of_floors != other.number_of_floors
    def __add__(self, value):
        if isinstance(value, int):
            self.number_of_floors += value
            return self
    def __iadd__(self, value):
        return self.__add__(value)
    def __radd__(self, value):
        return self.__add__(value)

h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

print(f'Название:{h1},кол-во этажей:{len(h1)}')
print(f'Название:{h2},кол-во этажей:{len(h2)}')
print(h1 == h2) # __eq__

h1 = h1 + 10 # __add__
print(f'Название:{h1},кол-во этажей:{len(h1)}')
print(h1 == h2)

h1 += 10 # __iadd__
print(f'Название:{h1},кол-во этажей:{len(h1)}')

h2 = 10 + h2 # __radd__
print(f'Название:{h2},кол-во этажей:{len(h2)}')

print(h1 > h2) # __gt__
print(h1 >= h2) # __ge__
print(h1 < h2) # __lt__
print(h1 <= h2) # __le__
print(h1 != h2) # __ne__