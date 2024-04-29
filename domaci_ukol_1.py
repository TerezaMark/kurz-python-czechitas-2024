from dataclasses import dataclass

@dataclass
class Item:
    name: str
    price: float

    def __str__(self):
        return f"{self.name}: {self.price} Kč."
    

@dataclass
class Pizza(Item):
    ingredients: dict

    def add_extra(self, ingredient: str, quantity: int, price_per_ingredient: int):
        if ingredient in self.ingredients:
            self.ingredients[ingredient] += quantity
        else:
            self.ingredients[ingredient] = quantity
            
    def __str__(self):
         return f"Pizza {self.name} s ingrediencemi {self.ingredients} stojí {self.price} Kč."


@dataclass
class Drink(Item):
     volume: int

     def __str__(self):
          return f"Nápoj {self.name} o objemu {self.volume} ml stojí {self.price} Kč."
     

@dataclass
class Order:
     customer_name: str
     delivery_address: str
     items: list
     status: str = "nová"

     def mark_delivered(self):
        self.status = "Doručeno"

     def __str__(self):
          return f"Zákazník {self.customer_name} objednal na adresu {self.delivery_address} tyto položky: {self.items}. Stav objednávky: {self.status}."
     

@dataclass
class DeliveryPerson:
    name: str
    phone_number: str
    available: bool = True
    current_order: Order = None

    def assign_order(self, order):
        if self.available == True:
            self.current_order = order
            self.current_order.status = "Na cestě"
            self.available = False
        else:
            print("Doručovatel má přiřazenou jinou objednávku.")

    def complete_delivery(self):
        self.current_order.status = "Doručeno"
        self.available = True

    def __str__(self):
        return f"Doručovatel {self.name}, tel. číslo {self.phone_number}, dostupnost: {self.available}, objednávka: {self.current_order}."
        
