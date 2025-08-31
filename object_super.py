class Prudact:
    def __init__(self, name , group, brand , price):
        self.name = name
        self.group = group
        self.brand = brand
        self.price = price

    def save(self):
        print(f"{self.name} has been saved")

class Electronic:
    def __init__(self, voltag ,name, group, brand , price):
        self.voltag = voltag
        self.name = name
        self.group = group
        self.brand = brand
        self.price = price


class Clothes(Prudact):
    def size(self):
        print(f"{self.name} size")

class Foods(Prudact):
    def ex_data(self):
        print(f"{self.name} ex_data")

    def pn_data(self):
        print(f"{self.name} pn_data")


class Health(Prudact):
    def ex_data(self):
        print(f"{self.name} ex_data")

class Laptops(Prudact,Electronic):
    pass

class Mobile(Prudact, Electronic):
    pass

class Icecream(Foods,Prudact):
    pass


class Drink(Foods,Prudact):
    pass

class Shampoo(Health,Prudact):
    pass

class Cream(Health,Prudact):
    pass
