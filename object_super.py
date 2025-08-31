class Product:
    def __init__(self, name , brand , price):
        self.name = name
        self.group = "product"
        self.brand = brand
        self.price = price

    # def save(self):
    #     print(f"{self.name} has been saved")
    def __repr__(self):
        return f"{self.__dict__}"

class Electronic(Product):
    def __init__(self, voltage ,name,  brand , price):
        super().__init__(name, brand, price)
        self.voltage = voltage
        self.group += "electronic"



class Clothes(Product):
    def __init__(self, name,  brand , price,size):
        super().__init__(name, brand, price)
        self.size = size
        self.group += "clothes"



class Food(Product):
    def __init__(self, name,  brand , price,ex_data,p_data):
        super().__init__(name, brand, price)
        self.ex_data = ex_data
        self.p_data = p_data
        self.group += "food"


class Health(Product):
    def __init__(self, name,  brand , price,ex_data,p_data):
        super().__init__(name, brand, price)
        self.ex_data = ex_data
        self.p_data = p_data
        self.group += "health"


class Laptop(Electronic):
    def __init__(self, name,  brand , price,ram,cpu):
        super().__init__(name, brand, price)
        self.ram = ram
        self.cpu = cpu
        self.group+= "laptop"


class Mobile( Electronic):
    def __init__(self, name,  brand , price,inch):
        super().__init__(name, brand, price)
        self.inch = inch
        self.group+= "mobile"


class Icecream(Food):
    def __init__(self, name,  brand , price,ex_data,p_data):
        super().__init__(name, brand, price)
        self.ex_data = ex_data
        self.p_data = p_data
        self.group += "icecream"




class Drink(Food):
    def __init__(self, name,  brand , price,ex_data,p_data):
        super().__init__(name, brand, price)
        self.ex_data = ex_data
        self.p_data = p_data
        self.group += "drink"


class Shampoo(Health,):
    def __init__(self, name,  brand, price, ex_data, p_data):
        super().__init__(name, brand, price)
        self.ex_data = ex_data
        self.p_data = p_data
        self.group += "shampoo"


class Cream(Health,):
    def __init__(self, name,  brand, price, ex_data, p_data):
        super().__init__(name, brand, price)
        self.ex_data = ex_data
        self.p_data = p_data
        self.group += "cream"


class Asus(Laptop):
    def __init__(self, name,  brand , price,ram,cpu):
        super().__init__(name,  brand , price,ram,cpu)
        self.group += "asus"

class Acer(Laptop):
    def __init__(self, name,  brand , price,ram,cpu):
        super().__init__(name,  brand , price,ram,cpu)
        self.group += "acer"


class Samsung(Mobile):
    def __init__(self, name, brand, price, inch):
        super().__init__( name,  brand , price,inch)
        self.group += "samsung"


class Iphone(Mobile):
    def __init__(self, name, brand, price, inch):
        super().__init__( name,  brand , price,inch)
        self.group += "Iphone"

samsung_mob=Samsung("a22","s",200,13)
print(samsung_mob)
iphone_mob=Iphone("13","promax",200,13)
print(iphone_mob)
asus_laptop=Asus("surface","pro",200,8,7)
print(asus_laptop)
acer_laptop= Acer ("del","a22",100,6,7)
print(acer_laptop)

