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


